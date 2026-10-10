# Square → GnuCash Reconciliation Utility

A privacy-first, 100% client-side conversion engine that transforms authentic **Square CSV exports** (`Transactions.csv` and `Balance Transfers.csv`) into balanced, multi-split **GnuCash CSV journal entries**.

---

## 1. What This Solves

Importing Square sales into GnuCash manually requires tedious arithmetic and split-entry manipulation:
- **Processing Fees**: Square deducts 2.6% + 10¢–30¢ per swipe before depositing funds into the bank account.
- **Sales Taxes & Tips**: Cannot be booked directly as revenue; must be separated into liability accounts.
- **Batch Reconciliation**: Daily bank deposits group multiple transactions together.

This tool automates double-entry balancing:
$$\sum \text{Debits} + \sum \text{Credits} = 0.00$$

### Accounting Mapping Logic
| Component | GnuCash Account Default | Type | Direction |
|---|---|---|---|
| **Net Deposit** | `Assets:Current Assets:Square Clearing` | Asset | Debit (+) |
| **Square Fees** | `Expenses:Bank Charges:Square Processing Fees` | Expense | Debit (+) |
| **Discounts** | `Expenses:Sales Discounts` | Contra/Expense | Debit (+) |
| **Gross Sales** | `Income:Sales` | Income | Credit (-) |
| **Sales Tax** | `Liabilities:Sales Tax Payable` | Liability | Credit (-) |
| **Tips** | `Liabilities:Tips Payable` | Liability | Credit (-) |

---

## 2. Supported Authentic Square Export Formats

1. **Square Transactions CSV** (Dashboard → Transactions → Export → Transactions CSV)
   - Headers detected: `Date`, `Time`, `Gross Sales`, `Discounts`, `Net Sales`, `Tax`, `Tip`, `Fees`, `Net Total`, `Transaction Status`.
2. **Square Balance / Transfers CSV** (Dashboard → Balance → View all transfers → Export)
   - Headers detected: `Deposit Date`, `Collected`, `Fees`, `Deposited`, `Deposit ID`.

---

## 3. How to Run

### In the Browser (Client-Side, Zero Server Uploads)
Simply open `index.html` in your browser:
```bash
open /Users/thagreat/.gemini/antigravity/scratch/square-to-gnucash/index.html
```
- No server installation or internet connection required.
- Financial data never leaves the browser sandbox.

### Command Line / Automated Testing
Run the Python test suite:
```bash
python3 -m unittest test_converter.py
```

---

## 4. GnuCash Import Step-by-Step

1. In GnuCash, select **File → Import → Import Transactions from CSV**.
2. Select the exported `.csv` file.
3. In the CSV Import Assistant:
   - Check **"Multi-split"**.
   - Set Account column to `Account`.
   - Set Deposit column to `Deposit`.
   - Set Withdrawal column to `Withdrawal`.
4. Click **Apply**.
