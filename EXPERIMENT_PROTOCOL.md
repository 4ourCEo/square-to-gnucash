# Experiment Protocol & Scorecard: Square → GnuCash Reconciliation

**Project**: Jackson Street Commercial Validation Lab  
**Experiment Number**: EXP-001  
**Target Niche**: Square sellers using GnuCash for accounting  
**Observation Window**: October 10, 2026 – October 24, 2026 (14 Days)  
**Public URL**: [4ourenterprises.me/square-to-gnucash](http://4ourenterprises.me/square-to-gnucash/)  
**Git Commit Hash at Launch**: `f44ae5d`  

---

## 1. Commercial Hypothesis

Small businesses using GnuCash to record Square sales experience painful CSV manipulation when splitting processing fees, sales taxes, tips, and net bank deposits. 

We hypothesize that:
1. High-intent searchers will discover a free, privacy-first, client-side utility organically without paid advertising.
2. At least a fraction of active users have willingness to pay for saved rules, automated recurring sync, or multi-location reconciliation.

---

## 2. Hard Governance Rules

1. **Zero Ad Spend**: $0.00 may be spent on PPC, social ads, or paid promotion.
2. **Zero 1-on-1 Outbound**: No cold DMs, emails, or sales calls.
3. **Community Seeding Ceiling**: Maximum of 2 public forum answers in existing problem threads, adhering strictly to technical, privacy-first FOSS utility disclosure.
4. **Kill-Switch Mandate**: If targets are missed at 11:59 PM on October 24, 2026, the experiment is terminated immediately. No goalpost shifting.
5. **Mandatory Post-Mortem Pause**: A 48-hour cool-off period is required following an autopsy before any second experiment may be launched.

---

## 3. The 14-Day Evaluation Scorecard

| Metric | Target (Pass) | Failure (Kill Switch) | Actual (Oct 24) | Outcome |
|---|---|---|---|---|
| **Organic Conversions** (CSV Downloads) | $\ge 15$ | $< 15$ | _[TBD]_ | _[TBD]_ |
| **Paid Intent Signals** (Pro Modal Clicks) | $\ge 2$ | $< 2$ | _[TBD]_ | _[TBD]_ |
| **Early-Bird Email Leads** | $\ge 1$ | $0$ | _[TBD]_ | _[TBD]_ |
| **Ad Spend** | $\$0.00$ | $> \$0.00$ | $\$0.00$ | **PASS** |

---

## 4. Fork Action Protocols

### Fork A: Pass ($\ge 15$ Conversions and $\ge 2$ Intent Signals)
1. Do **not** build automated backend sync immediately.
2. Send a personal email to the early-bird leads with a manual payment link ($9.50 early-bird price) for early access to custom rules.
3. Verify actual monetary transfer before writing any backend infrastructure.

### Fork B: Fail ($< 15$ Conversions or $< 2$ Intent Signals)
1. Mark experiment as **TERMINATED**.
2. Archive the GitHub repository to read-only.
3. Complete the autopsy report below.
4. Enforce the mandatory 48-hour pause before selecting Experiment #2.

---

## 5. Experiment Autopsy Template (Pre-Committed)

*(To be filled on October 24, 2026 if Fork B is triggered)*

```markdown
### Autopsy: EXP-001 (Square to GnuCash)
- Final Traffic / Pageviews: [Count]
- Total CSV Conversions: [Count]
- Total Pro Intent Clicks: [Count]
- Root Cause Analysis:
  [ ] Zero organic discovery (Search volume insufficient or Google indexing lag)
  [ ] Problem exists but lack of recurring utility (One-off need)
  [ ] GnuCash user anti-payment friction (FOSS mindset absolute barrier)
  [ ] Product usability or formatting mismatch
- Capital Spent: $0.00
- Engineering Hours Spent: ~3 hours
- Key Takeaway for Jackson Street:
```
