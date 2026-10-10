# Square → GnuCash Reconciliation OS
**Design Baseline · Sovereign Builder OS Kernel v2.1 · October 2026**

---

## 1. Product Decision

Build a zero-overhead, client-side financial reconciliation utility that converts raw Square transaction and transfer exports into mathematically balanced, multi-split GnuCash journal entries.

### The Smallest Useful MVP
The MVP begins with an unformatted Square export (`Transactions.csv` or `Balance Transfers.csv`) and ends with a validated GnuCash-compatible multi-split CSV file that imports cleanly via GnuCash's official CSV Import Assistant. It must:
1. Parse authentic Square exports with varying fee, tip, discount, and sales tax columns.
2. Group transactions either as **Daily Settlement Batches** (matching lump-sum bank deposits) or **Granular Per-Transaction Records**.
3. Enforce double-entry accounting balance where $\sum \text{Debits} + \sum \text{Credits} = 0.00$.
4. Process all financial records 100% locally in browser memory without sending customer or sales data to any remote server.

### What Is Explicitly Rejected
- **No Remote Backend or Database**: Financial data never leaves the client device. Zero server storage, zero database sync, zero credential custody.
- **No Premature OAuth Sync**: Direct Square API integration and token storage are rejected until willingness to pay is proven with real money.
- **No Monthly SaaS Billing Infrastructure**: GnuCash users choose FOSS specifically to escape monthly subscriptions ($30–$90/mo for QuickBooks/Xero). Recurring SaaS billing is rejected in favor of a free core utility + $19 one-time lifetime license intent testing.
- **No Paid User Acquisition**: $0.00 advertising spend. Zero paid search, zero social ads, zero 1-on-1 cold outreach.

---

## 2. System Architecture & Technical Topology

```
[Square POS Dashboard]
         │ (Manual CSV Export: Transactions.csv or Transfers.csv)
         ▼
[Client Browser Memory (Web Worker / FileReader)]
         │
         ├── 1. Currency Sanitization (strip $, commas, negative parentheses)
         ├── 2. Date Normalization (ISO-8601 YYYY-MM-DD)
         ├── 3. Header Detection (Transactions vs Balance Transfers)
         ├── 4. Double-Entry Split Balancer:
         │      • Debit: Assets:Current Assets:Square Clearing (Net Deposited)
         │      • Debit: Expenses:Bank Charges:Square Processing Fees (Fees)
         │      • Debit: Expenses:Sales Discounts (Discounts Applied)
         │      • Credit: Income:Sales (Gross Merchandise / Service Sales)
         │      • Credit: Liabilities:Sales Tax Payable (Sales Tax Collected)
         │      • Credit: Liabilities:Tips Payable (Staff Tips Collected)
         │
         ▼
[Live T-Account Equation Audit Card]
(Total Debits == Total Credits | Delta: $0.00)
         │
         ├── 5. Master-Detail Ledger Preview (Tabular Monospace Lining Figures)
         │
         ▼
[GnuCash Multi-Split CSV Export]
         │ (File -> Import -> Import Transactions from CSV)
         ▼
[GnuCash Desktop Accounting Ledger]
```

### Invariants
1. **Zero-Upload Invariant**: No transaction row, monetary amount, or customer record may be transmitted across the network.
2. **Mathematical Balance Invariant**: No journal entry may be exported if $\sum \text{Debits} \ne \sum \text{Credits}$. Discrepancies $> \$0.00$ immediately lock the export button.
3. **Double-Entry Sign Convention**:
   - In GnuCash CSV multi-split imports, asset and expense increases are **Deposits (Debits)**.
   - Income and liability increases are **Withdrawals (Credits)**.

---

## 3. Canonical Financial Data Model

### The Square Clearing Account Lifecycle
Square bundles multiple sales transactions into a lump-sum bank deposit 1–3 business days later after deducting processing fees. Recording gross sales directly to `Assets:Checking` corrupts bank statement reconciliation. 

The canonical Sovereign Builder OS accounting model routes through a clearing buffer:
1. **At Time of Sale / Daily Settlement**:
   - `Debit` `Assets:Square Clearing` (Net funds pending deposit)
   - `Debit` `Expenses:Square Processing Fees` (Square fee deducted)
   - `Credit` `Income:Sales` (Gross revenue)
   - `Credit` `Liabilities:Sales Tax Payable` (Taxes held in trust)
   - `Credit` `Liabilities:Tips Payable` (Tips held for staff)
2. **When Lump Bank Deposit Arrives in Checking**:
   - Recorded as a simple single-split transfer: `Debit` `Assets:Checking` $\rightarrow$ `Credit` `Assets:Square Clearing`.
   - Result: `Assets:Square Clearing` balance returns strictly to **$0.00**.

---

## 4. Interface & View Architecture

The interface follows a **High-Contrast Editorial Financial Theme** governed by five core rules:
1. **Progressive Disclosure**: Chart of Accounts mapping (`Assets:Square Clearing`, `Expenses:Fees`, etc.) is tucked into a collapsible settings drawer. The zero-state presents zero clutter.
2. **Live T-Account Equation**: An above-the-fold audit card displaying:
   $$\text{Total Debits} \quad = \quad \text{Total Credits} \quad \left(\Delta \$0.00\right)$$
3. **Tabular Numerals & Monospace Column Alignment**:
   `font-variant-numeric: tabular-nums lining-nums` across all currency values so decimals align with CPA accuracy.
4. **Collapsible Master-Detail Ledger**: Parent summary rows (Date, Description, Total Net) expand on click to reveal granular double-entry splits.
5. **Sticky Action Footer**: A persistent bottom reconciliation bar housing live transaction count, balance status, and primary export action.

---

## 5. Sovereign Risk, Policy, & Gate Ledger

### Phase Gate: GATE_COMMERCIAL_VALIDATION_14D
- **Window**: October 10, 2026 – October 24, 2026 (14 Days)
- **Target Pass Threshold**:
  - $\ge 15$ Unique CSV Conversions (Downloads)
  - $\ge 2$ Paid Intent Signals (Pro Modal Clicks / Early-Bird Signups)
  - $\$0.00$ Ad Spend
- **Failure Protocol (Fork B)**:
  - If targets are missed at 11:59 PM on October 24, 2026, the experiment is terminated immediately.
  - The repository is archived to read-only.
  - An autopsy report is generated documenting the falsification of the thesis.
  - A **mandatory 48-hour cool-off pause** is enforced before any subsequent venture may be explored.
