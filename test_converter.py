#!/usr/bin/env python3
import io
import csv
import unittest
from decimal import Decimal
from converter import SquareGnuCashConverter, clean_currency, normalize_date

class TestSquareGnuCashConverter(unittest.TestCase):

    def setUp(self):
        self.converter = SquareGnuCashConverter()

    def test_clean_currency(self):
        self.assertEqual(clean_currency("$12.50"), Decimal("12.50"))
        self.assertEqual(clean_currency("-$0.35"), Decimal("-0.35"))
        self.assertEqual(clean_currency("(1,250.00)"), Decimal("-1250.00"))
        self.assertEqual(clean_currency(""), Decimal("0.00"))
        self.assertEqual(clean_currency(None), Decimal("0.00"))

    def test_normalize_date(self):
        self.assertEqual(normalize_date("2026-10-08"), "2026-10-08")
        self.assertEqual(normalize_date("10/08/2026"), "2026-10-08")
        self.assertEqual(normalize_date("10/08/26 14:32:00"), "2026-10-08")

    def test_authentic_square_transactions(self):
        # Sample authentic Square Transactions export rows
        sample_transactions = [
            {
                "Date": "2026-10-01",
                "Time": "12:30:00",
                "Gross Sales": "$100.00",
                "Discounts": "$10.00",
                "Net Sales": "$90.00",
                "Tax": "$7.20",
                "Tip": "$15.00",
                "Fees": "-$3.15",
                "Net Total": "$109.05",
                "Transaction Status": "Complete",
                "Transaction ID": "sq_tx_101",
                "Description": "Coffee & Pastries"
            },
            {
                "Date": "2026-10-01",
                "Time": "13:15:00",
                "Gross Sales": "$25.00",
                "Discounts": "$0.00",
                "Net Sales": "$25.00",
                "Tax": "$2.00",
                "Tip": "$0.00",
                "Fees": "-$0.85",
                "Net Total": "$26.15",
                "Transaction Status": "Complete",
                "Transaction ID": "sq_tx_102",
                "Description": "Beans Bag"
            }
        ]

        entries = self.converter.process_transactions_csv(sample_transactions, aggregate_by_deposit_or_day=False)
        self.assertEqual(len(entries), 2)

        # Verify entry 1 balances exactly to 0.00
        e1 = entries[0]
        split_sum = sum(s["amount"] for s in e1["splits"])
        self.assertEqual(split_sum, Decimal("0.00"))

        # Verify entry 1 splits
        accounts = {s["account"]: s["amount"] for s in e1["splits"]}
        self.assertEqual(accounts["Assets:Current Assets:Square Clearing"], Decimal("109.05"))
        self.assertEqual(accounts["Expenses:Bank Charges:Square Processing Fees"], Decimal("3.15"))
        self.assertEqual(accounts["Expenses:Sales Discounts"], Decimal("10.00"))
        self.assertEqual(accounts["Income:Sales"], Decimal("-100.00"))
        self.assertEqual(accounts["Liabilities:Sales Tax Payable"], Decimal("-7.20"))
        self.assertEqual(accounts["Liabilities:Tips Payable"], Decimal("-15.00"))

        # Export to CSV check
        out = io.StringIO()
        self.converter.export_to_gnucash_csv(entries, out)
        csv_text = out.getvalue()
        self.assertIn("Assets:Current Assets:Square Clearing", csv_text)
        self.assertIn("109.05", csv_text)

    def test_daily_aggregation_mode(self):
        sample_transactions = [
            {
                "Date": "2026-10-02",
                "Gross Sales": "$50.00",
                "Discounts": "$0.00",
                "Tax": "$4.00",
                "Tip": "$5.00",
                "Fees": "-$1.70",
                "Net Total": "$57.30",
                "Transaction Status": "Complete"
            },
            {
                "Date": "2026-10-02",
                "Gross Sales": "$50.00",
                "Discounts": "$0.00",
                "Tax": "$4.00",
                "Tip": "$5.00",
                "Fees": "-$1.70",
                "Net Total": "$57.30",
                "Transaction Status": "Complete"
            }
        ]
        entries = self.converter.process_transactions_csv(sample_transactions, aggregate_by_deposit_or_day=True)
        self.assertEqual(len(entries), 1)
        e = entries[0]
        self.assertEqual(sum(s["amount"] for s in e["splits"]), Decimal("0.00"))
        accounts = {s["account"]: s["amount"] for s in e["splits"]}
        self.assertEqual(accounts["Income:Sales"], Decimal("-100.00"))
        self.assertEqual(accounts["Assets:Current Assets:Square Clearing"], Decimal("114.60"))
        self.assertEqual(accounts["Expenses:Bank Charges:Square Processing Fees"], Decimal("3.40"))

    def test_authentic_square_transfers(self):
        sample_transfers = [
            {
                "Deposit Date": "2026-10-03",
                "Payment Date": "2026-10-02",
                "Type": "Payment",
                "Transaction ID": "tx_201",
                "Payment ID": "pay_201",
                "Collected": "$120.00",
                "Fees": "-$3.80",
                "Deposited": "$116.20",
                "Deposit ID": "DEP-9988",
                "Location": "Main Store"
            },
            {
                "Deposit Date": "2026-10-03",
                "Payment Date": "2026-10-02",
                "Type": "Payment",
                "Transaction ID": "tx_202",
                "Payment ID": "pay_202",
                "Collected": "$80.00",
                "Fees": "-$2.50",
                "Deposited": "$77.50",
                "Deposit ID": "DEP-9988",
                "Location": "Main Store"
            }
        ]
        entries = self.converter.process_transfers_csv(sample_transfers)
        self.assertEqual(len(entries), 1) # grouped by Deposit ID
        e = entries[0]
        self.assertEqual(sum(s["amount"] for s in e["splits"]), Decimal("0.00"))
        accounts = {s["account"]: s["amount"] for s in e["splits"]}
        self.assertEqual(accounts["Assets:Current Assets:Square Clearing"], Decimal("193.70"))
        self.assertEqual(accounts["Expenses:Bank Charges:Square Processing Fees"], Decimal("6.30"))
        self.assertEqual(accounts["Income:Sales"], Decimal("-200.00"))

if __name__ == "__main__":
    unittest.main()
