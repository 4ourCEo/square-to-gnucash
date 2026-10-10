#!/usr/bin/env python3
"""
Square-to-GnuCash Reconciliation Engine
Converts authentic Square export CSVs (Transactions or Transfers/Balance)
into balanced, multi-split GnuCash CSV journal entries.
"""

import csv
import re
from datetime import datetime
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP

def clean_currency(val: str) -> Decimal:
    """Parse currency string like '$1,234.50' or '-$0.45' or '(12.50)' to Decimal."""
    if not val:
        return Decimal("0.00")
    s = str(val).strip()
    is_negative = False
    if s.startswith("(") and s.endswith(")"):
        is_negative = True
        s = s[1:-1]
    s = s.replace("$", "").replace(",", "").strip()
    if s.startswith("-"):
        is_negative = True
        s = s[1:].strip()
    if not s:
        return Decimal("0.00")
    try:
        amt = Decimal(s)
        return -amt if is_negative else amt
    except Exception:
        return Decimal("0.00")

def normalize_date(date_str: str) -> str:
    """Normalize date strings to YYYY-MM-DD for GnuCash import."""
    d = date_str.strip().split(" ")[0] # strip time if present
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%m/%d/%y", "%d/%m/%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(d, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return d

class SquareGnuCashConverter:
    DEFAULT_ACCOUNTS = {
        "bank_or_clearing": "Assets:Current Assets:Square Clearing",
        "processing_fee": "Expenses:Bank Charges:Square Processing Fees",
        "gross_sales": "Income:Sales",
        "sales_tax": "Liabilities:Sales Tax Payable",
        "tips": "Liabilities:Tips Payable",
        "discounts": "Expenses:Sales Discounts"
    }

    def __init__(self, account_mapping=None):
        self.accounts = dict(self.DEFAULT_ACCOUNTS)
        if account_mapping:
            self.accounts.update(account_mapping)

    def detect_format(self, headers):
        """Detect whether CSV is Square Transactions export or Balance/Transfer export."""
        header_set = {h.strip() for h in headers}
        if "Gross Sales" in header_set or "Net Sales" in header_set:
            return "transactions"
        elif "Deposit ID" in header_set or "Deposited" in header_set or "Collected" in header_set:
            return "transfers"
        return "unknown"

    def process_transactions_csv(self, rows, aggregate_by_deposit_or_day=False):
        """
        Process Square Transactions CSV.
        Headers typically: Date, Time, Gross Sales, Discounts, Net Sales, Gift Card Sales,
        Tax, Tip, Partial Accounting, Fees, Net Total, Transaction Status, etc.
        """
        entries = []
        if aggregate_by_deposit_or_day:
            grouped = defaultdict(lambda: {
                "gross_sales": Decimal("0.00"),
                "discounts": Decimal("0.00"),
                "tax": Decimal("0.00"),
                "tip": Decimal("0.00"),
                "fees": Decimal("0.00"),
                "net_total": Decimal("0.00"),
                "count": 0
            })
            for row in rows:
                if row.get("Transaction Status", "").strip().lower() in ("failed", "canceled"):
                    continue
                dt = normalize_date(row.get("Date", ""))
                group_key = dt
                g = grouped[group_key]
                g["gross_sales"] += clean_currency(row.get("Gross Sales", "0"))
                g["discounts"] += clean_currency(row.get("Discounts", "0")) # often negative in Square
                g["tax"] += clean_currency(row.get("Tax", "0"))
                g["tip"] += clean_currency(row.get("Tip", "0"))
                # Square fees are usually negative in export
                fee = clean_currency(row.get("Fees", "0"))
                g["fees"] += abs(fee)
                g["net_total"] += clean_currency(row.get("Net Total", "0"))
                g["count"] += 1

            for dt, totals in sorted(grouped.items()):
                entries.append(self._build_journal_entry(
                    date=dt,
                    description=f"Square Daily Summary ({totals['count']} transactions)",
                    net_deposited=totals["net_total"],
                    fees=totals["fees"],
                    gross_sales=totals["gross_sales"],
                    tax=totals["tax"],
                    tip=totals["tip"],
                    discounts=abs(totals["discounts"])
                ))
        else:
            for i, row in enumerate(rows):
                if row.get("Transaction Status", "").strip().lower() in ("failed", "canceled"):
                    continue
                dt = normalize_date(row.get("Date", ""))
                tx_id = row.get("Transaction ID", f"TX-{i+1}")
                desc = row.get("Description", "") or f"Square Sale {tx_id}"
                gross = clean_currency(row.get("Gross Sales", "0"))
                disc = abs(clean_currency(row.get("Discounts", "0")))
                tax = clean_currency(row.get("Tax", "0"))
                tip = clean_currency(row.get("Tip", "0"))
                fees = abs(clean_currency(row.get("Fees", "0")))
                net = clean_currency(row.get("Net Total", "0"))

                # Check if net = gross - disc + tax + tip - fees
                calc_net = gross - disc + tax + tip - fees
                if net == Decimal("0.00") and calc_net != Decimal("0.00"):
                    net = calc_net

                entries.append(self._build_journal_entry(
                    date=dt,
                    description=desc,
                    net_deposited=net,
                    fees=fees,
                    gross_sales=gross,
                    tax=tax,
                    tip=tip,
                    discounts=disc
                ))
        return entries

    def process_transfers_csv(self, rows):
        """
        Process Square Transfers/Settlement CSV.
        Headers: Deposit Date, Payment Date, Type, Transaction ID, Payment ID,
        Collected, Fees, Deposited, Deposit ID, Location
        """
        grouped = defaultdict(lambda: {
            "date": "",
            "collected": Decimal("0.00"),
            "fees": Decimal("0.00"),
            "deposited": Decimal("0.00"),
            "count": 0
        })

        for row in rows:
            dep_id = row.get("Deposit ID", "").strip() or "TRANSFER-" + normalize_date(row.get("Deposit Date", ""))
            g = grouped[dep_id]
            dep_date = normalize_date(row.get("Deposit Date", ""))
            if not g["date"] and dep_date:
                g["date"] = dep_date
            g["collected"] += clean_currency(row.get("Collected", "0"))
            g["fees"] += abs(clean_currency(row.get("Fees", "0")))
            g["deposited"] += clean_currency(row.get("Deposited", "0"))
            g["count"] += 1

        entries = []
        for dep_id, totals in sorted(grouped.items()):
            dt = totals["date"] or datetime.now().strftime("%Y-%m-%d")
            desc = f"Square Deposit {dep_id} ({totals['count']} items)"
            entries.append(self._build_journal_entry(
                date=dt,
                description=desc,
                net_deposited=totals["deposited"],
                fees=totals["fees"],
                gross_sales=totals["collected"],
                tax=Decimal("0.00"),
                tip=Decimal("0.00"),
                discounts=Decimal("0.00")
            ))
        return entries

    def _build_journal_entry(self, date, description, net_deposited, fees, gross_sales, tax, tip, discounts):
        """
        Builds a balanced multi-split journal entry.
        In GnuCash double-entry:
        - Debits (Assets increase, Expenses increase) are POSITIVE amounts.
        - Credits (Liabilities increase, Income increase) are NEGATIVE amounts (or positive credits).
        Balanced condition:
          Debit Bank/Clearing (+net_deposited)
        + Debit Fees (+fees)
        + Debit Discounts (+discounts)
        - Credit Gross Sales (-gross_sales)
        - Credit Tax (-tax)
        - Credit Tips (-tip)
        = 0.00
        """
        splits = []
        # Debit: Bank or Clearing account receives net deposit
        if net_deposited != Decimal("0.00"):
            splits.append({
                "account": self.accounts["bank_or_clearing"],
                "memo": "Net funds transferred/cleared",
                "amount": net_deposited # Debit
            })

        # Debit: Processing fee expense
        if fees != Decimal("0.00"):
            splits.append({
                "account": self.accounts["processing_fee"],
                "memo": "Square transaction processing fee",
                "amount": fees # Debit
            })

        # Debit: Discounts (reduces revenue / contra-revenue or expense)
        if discounts != Decimal("0.00"):
            splits.append({
                "account": self.accounts["discounts"],
                "memo": "Discounts applied",
                "amount": discounts # Debit
            })

        # Credit: Gross sales revenue
        if gross_sales != Decimal("0.00"):
            splits.append({
                "account": self.accounts["gross_sales"],
                "memo": "Gross merchandise/service sales",
                "amount": -abs(gross_sales) # Credit
            })

        # Credit: Sales tax payable liability
        if tax != Decimal("0.00"):
            splits.append({
                "account": self.accounts["sales_tax"],
                "memo": "Sales tax collected",
                "amount": -abs(tax) # Credit
            })

        # Credit: Tips payable liability
        if tip != Decimal("0.00"):
            splits.append({
                "account": self.accounts["tips"],
                "memo": "Tips collected for staff",
                "amount": -abs(tip) # Credit
            })

        # Balance verification & rounding adjustment
        total_sum = sum(s["amount"] for s in splits)
        if total_sum != Decimal("0.00"):
            # Small 1-cent discrepancy adjustment on gross sales or rounding fee
            if abs(total_sum) <= Decimal("0.05"):
                for s in splits:
                    if s["account"] == self.accounts["gross_sales"]:
                        s["amount"] -= total_sum
                        break
            else:
                raise ValueError(f"Transaction does not balance: discrepancy of {total_sum}")

        return {
            "date": date,
            "description": description,
            "splits": splits
        }

    def export_to_gnucash_csv(self, entries, file_obj):
        """
        Writes GnuCash official Multi-Split CSV format:
        Header: Date,Description,Account,Deposit,Withdrawal,Memo
        First line of transaction has Date & Description;
        subsequent splits can leave Date & Description empty or repeated.
        """
        writer = csv.writer(file_obj)
        writer.writerow(["Date", "Description", "Account", "Deposit", "Withdrawal", "Memo"])

        for entry in entries:
            is_first = True
            for s in entry["splits"]:
                amt = s["amount"]
                # In GnuCash CSV Importer:
                # If Deposit/Withdrawal columns are used:
                # Positive amount is Deposit (Debit for asset/expense), Negative is Withdrawal (Credit)
                deposit_str = f"{amt:.2f}" if amt > 0 else ""
                withdrawal_str = f"{abs(amt):.2f}" if amt < 0 else ""

                date_val = entry["date"] if is_first else ""
                desc_val = entry["description"] if is_first else ""

                writer.writerow([
                    date_val,
                    desc_val,
                    s["account"],
                    deposit_str,
                    withdrawal_str,
                    s.get("memo", "")
                ])
                is_first = False
