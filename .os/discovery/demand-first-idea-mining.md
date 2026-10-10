# Demand-First Idea Mining — Discovery Playbook

> **Status:** Reusable discovery playbook. This is Layer 5 content, not kernel.
>
> This document **does not** add a gate, a score, an evidence tier, a decision
> state, or a second approval path. It generates opportunity candidates and the
> evidence that feeds the existing pipeline. The OS remains the sole authority
> for deciding whether an opportunity moves forward.

```
DISCOVER → CAPTURE EVIDENCE → CREATE OPPORTUNITY RECORD
        → existing Opportunity/validation gate → evidence eligibility
        → distribution/reachability → economics → risk → decision routing
```

The vocabulary used below (`evidence_type`, `record_type`, `source_type`,
`verification_status`, `current_state`, `gates`, `validation.plan.json`, the
`PASS | FAIL | BLOCKED | REQUIRES_APPROVAL` gate results, and the existing
transition targets) is the vocabulary defined in `KERNEL.md`, the
`.os/README.md` scaffold reference, and the runtime. Treat it as authoritative.

---

## Purpose

Generate opportunity candidates from **demonstrated market demand** rather than
speculative product ideas.

This method feeds the existing OS gates and evaluation systems. It does not
independently approve an idea, set thresholds, or override a gate result.

## Governing principle

Stop beginning idea generation with:

> "What should we build?"

Prefer:

> **"Where are people already spending time, money, or effort to work around a
> broken process?"**

The OS favors **demonstrated demand over originality**. Originality is not
required. Existing competitors can be positive market evidence. The presence of
a workaround can be evidence of unresolved demand.

## Default discovery question

Where are people already spending time, money, or effort to work around a broken
process?

## Hunt for revenue mechanisms, not only software ideas

The OS must no longer ask only *"what software should we build?"* It must also
ask:

> **What painful recurring business outcome can we monetize quickly, validate
> manually, and later automate?**

The target operating loop:

```
FIND PAID PAIN → VALIDATE MANUALLY → GET CASH SIGNAL → STANDARDIZE DELIVERY
→ AUTOMATE → PRODUCTIZE → RECURRING REVENUE
```

A candidate may be a productized service, a fractional retainer, an intent
utility, a lead-generation mechanism, a platform add-on, or a micro-SaaS. Do not
force every opportunity into a subscription SaaS box. **Pre-code validation
remains mandatory** regardless of model.

## Discovery source hierarchy

Prefer higher-signal sources. This is a **priority heuristic**, not a rule that
forbids lower tiers — lower tiers remain useful but should not dominate.

### Tier 1 — High-signal proximity
- founder/operator work experience
- repeated client or agency work
- internal tools built for one employer or client
- recurring workflows personally observed
- direct-network domain problems
- spouse/partner/domain-expert access where relevant

### Tier 2 — Existing payment / proven category
- existing software spend
- employee labor
- contractor / VA labor
- consulting spend
- expensive or bloated incumbents
- repeated custom builds
- platform ecosystems and app marketplaces
- negative competitor reviews
- pricing pain
- niche / regional gaps

### Tier 3 — Intent and market signals
- commercial search intent
- calculators, estimators, quote/sizing tools
- "how much does X cost", "template", "generator", "compare", "near me"
- category-specific buying queries

### Tier 4 — Cold public-signal mining
- Hacker News, Reddit, forums, GitHub issues, comments, general communities

Tier 4 is the only lane the shipped automated runner (`python3 -m discovery`)
currently reaches. It is **supplemental** and does not replace Tier 1–3 evidence.
Do not encode percentages or ranking claims from external source videos as fact
unless independently verified.

## Discovery priority order

When hunting for the next revenue opportunity, look in this order (a heuristic,
not a constitutional rule):

```
1. existing work / repeated client problems
2. existing spend / proven categories
3. repeated paid service workflows
4. platform ecosystems
5. high-intent search
6. competitor complaints
7. public forums / HN / Reddit
```

## Discovery signals

Search for evidence of:

1. recurring manual workarounds
2. repetitive copy/paste
3. spreadsheets acting as software
4. fragmented Notion, document, or email workflows
5. custom scripts people built because existing software is inadequate
6. repeated customer complaints
7. active attempts to solve the problem
8. existing paid competitors
9. missing functionality users repeatedly request
10. identifiable and reachable users
11. clear money, time, throughput, revenue, compliance, or frustration impact
12. an inexpensive experiment capable of testing willingness to pay

Each signal is a **hypothesis generator**, not evidence. To count, it must be
captured as evidence in the existing ledger and evaluated by the existing gates.

---

## Discovery Method 1 — Workaround Mining

Look for users tolerating inefficient multi-step workflows.

Examples:

- maintaining several spreadsheets
- copying information between systems
- manually reconciling records
- using Notion as a substitute for purpose-built software
- combining several tools to perform one job
- maintaining custom scripts
- repeating the same administrative task frequently

A workaround is **not automatically** a business opportunity. Treat it as an
evidence signal that must enter the normal OS evaluation process.

## Discovery Method 2 — Complaint Mining

Search sources such as:

- Reddit
- Discord communities
- GitHub issues
- YouTube comments
- product reviews
- app marketplaces
- forums
- support communities
- industry groups
- competitor review pages

Look for language such as:

- "Does anyone know a way to..."
- "I wish this could..."
- "Why doesn't this..."
- "Is there anything that..."
- "I currently have to..."
- "This would be perfect if..."
- "I stopped using it because..."
- "It costs too much just to..."
- "Why do I need three tools to..."

Repeated complaint patterns are stronger evidence than one isolated request.

**Separate these tiers, and record the tier — do not blur them:**

| Tier | Meaning | Typical evidence handling |
| --- | --- | --- |
| Isolated annoyance | one person, one complaint | `ANECDOTE`; cannot justify a gate |
| Repeated inconvenience | a pattern across users | `MARKET`/`CUSTOMER` candidate; needs a source |
| Costly operational pain | measurable time/money loss | `CUSTOMER` when observed; `MARKET` when recorded |
| Urgent commercial pain | blocks revenue/renewal/compliance | strongest candidate; seek `TRANSACTION`/`CONTRACTUAL` |

## Discovery Method 3 — Competitor Gap Mining

Do not treat competition as automatic disqualification. Existing paid
competitors can prove:

- buyers exist
- the category is understood
- customers already allocate budget
- a workflow has enough value to support a market

Analyze competitor weaknesses, especially recurring 1-star, 2-star, and 3-star
review complaints. Look for gaps such as:

- overpriced enterprise plans
- unnecessary complexity
- poor UI
- slow workflows
- missing integrations
- ignored feature requests
- poor support
- narrow platform support
- bad onboarding
- weak mobile experience
- a segment the incumbent does not serve well

The opportunity is not "competitor exists therefore clone it." The opportunity is:

> **validated demand + observable gap + reachable buyer + better wedge.**

## Discovery Method 4 — Underserved Adjacent Market Mining

The transfer pattern:

```
Validated solution in Market A
→ similar unresolved problem in Market B
```

Example pattern: a successful folder-management utility exists for one AI chat
platform; a different AI platform has similar user behavior but lacks the same
solution.

That can be a valid opportunity candidate. However, adjacent-market transfer
requires independent evidence that:

- the underlying problem is substantially similar
- the new audience actually experiences the pain
- the audience is reachable
- the incumbent solution does not adequately serve them
- users show evidence of wanting or attempting a solution

**Do not permit blind cloning.** The Market A result is precedent, not proof of
Market B demand.

## Discovery Method 5 — High-Intent Search Mining

Search intent can reveal demand that forums miss. Use category-specific buying
queries, not vanity terms:

```
"<vertical> calculator"          "<vertical> cost estimator"
"<workflow> generator"           "<equipment> sizing calculator"
"<service> price calculator"     "<task> template"
"<process> checklist"            "<industry> quote calculator"
"<metric> ROI calculator"
```

For each search-driven opportunity evaluate, and record as evidence:

- evidence of search demand (observed, not assumed)
- commercial intent (does the searcher intend to buy, hire, or transact?)
- buyer relevance
- competition and how the intent is served today
- monetization fit (which archetype and first cash path)
- lead value, where lead-based
- maintenance burden, SEO difficulty, and whether a single-purpose tool
  delivers meaningful value

**Search volume is not proof of a business.** Do not build because a query looks
popular; require a viable economic path and a manual willingness-to-pay test.
The OS does not build search-volume infrastructure.

## Discovery Method 6 — Fractional Operations / Recurring Data-Service Mining

Look for businesses where staff repeatedly:

- reconcile systems
- clean spreadsheets
- prepare weekly reports
- compare billing against operations
- track exceptions
- investigate margin leakage
- produce recurring management summaries
- monitor inventory discrepancies
- combine exports from multiple tools
- answer the same operational questions every week

For each candidate determine:

```
1. Can we sell the result manually?
2. Is the work recurring?
3. Can parts of delivery be standardized?
4. Can a large share of delivery eventually be automated?
5. Does recurring automation create retention?
6. Is there a credible path from service → product?
```

If the answer is no, flag **high owner-dependence**.

The desirable progression:

```
manual recurring pain → paid service → repeatable delivery → reusable scripts
→ automated reporting → recurring retainer → product/software
```

The goal is never a permanent founder-dependent consulting job.

## Discovery Method 7 — Repeated Custom Work → Productization

Treat repeated **paid** custom work as a strong productization signal.

Look for:

- custom workflows built multiple times
- the same spreadsheet cleanup repeated for multiple clients
- repeated reporting deliverables
- recurring integrations
- agencies repeatedly solving the same backend problem
- consultants reusing the same internal scripts

Pattern:

```
repeated paid custom work + same core workflow + similar buyer
= productization candidate
```

Productization is a signal, not an automatic decision. Still evaluate market
size, recurring value, distribution, implementation burden, support burden, and
defensibility. There is no universal repeat count; "built 3+ times" is a useful
signal, not a law.

## Discovery Method 8 — Proven Category Entry

Entering a proven category can work when there is a sharp wedge.

```
proven category + visible buyer spend + hated/expensive/bloated incumbent + sharp wedge
= candidate
```

Possible wedges: narrow vertical focus; lower complexity; pricing; regional or
payment support; workflow specialization; better implementation; better
integration; an underserved segment.

**"Cheaper clone" alone is not a moat.** Require a wedge a buyer can name.

## Discovery Method 9 — Observable Revenue / Operations Leakage Mining

Look for recurring, **observable** leakage where value or cash silently escapes:
unbilled or under-billed usage, drifted prices, missed renewals, unclaimed
credits/rebates, unreconciled payments, unclaimed SLA/service credits, idle
seats/licenses, inventory shrinkage, unreturned deposits, unbilled change orders,
missed warranty claims, unreconciled access (see Method 6).

Prefer leaks that are observable **before** outreach (public rate cards, contracts,
filings, listings, job posts). Capture the pattern and the economic **class** (time,
rework, blocked revenue, compliance exposure, retained cost); **do not invent dollar
values**. These examples illustrate a pattern — they are **not** one-industry rules,
and AI voice is not a default remedy.

---

## Revenue archetypes

Classify every candidate by the revenue mechanism it would use — not only by
whether it is "software." An archetype is a lens for the offer; it is not a gate
and does not override the existing pipeline.

| # | Archetype | What it is | Typical first cash path |
| --- | --- | --- | --- |
| 1 | Vertical software / micro-SaaS | Recurring software solving one narrow workflow | paid pilot / pre-sale |
| 2 | Productized service | Repeatable service: fixed scope, repeatable delivery, narrow buyer, standardized outputs | fixed-fee engagement |
| 3 | Fractional operations / data service | Recurring operational visibility or reconciliation (KPI reporting, margin reconciliation, multi-system cleanup, discrepancy detection, executive summaries, alerts) | recurring retainer |
| 4 | Intent utility | Focused web utility tied to commercial/search intent (calculator, estimator, quote/sizing tool, checklist, ROI tool) | lead sale / paid utility feature / service upsell |
| 5 | Lead-generation utility | Utility whose primary engine is qualified lead capture, pay-per-call, or referral economics | lead commission / pay-per-call |
| 6 | Platform / marketplace add-on | Built inside an existing ecosystem (marketplaces, chat, accounting, vertical apps) | app subscription / setup fee |
| 7 | Repeated custom work → productization | The same deliverable built or sold repeatedly | first: service; later: product |

The OS must ask, for every candidate: **which revenue mechanism pays first, and
can it be validated manually before any software is built?**

---

## Proof-First logic

The offer must be designable around a **provable outcome**, not activity.

- **Finish line** — define the specific, verifiable end state the buyer pays for
  (the "done" moment). Vague scope produces no proof and no payment.
- **Early win** — a small, fast, visible result that proves movement before the
  finish line. This is a design principle, not a fixed delivery window.
- **Proof mechanism** — the artifact or measurement that demonstrates the outcome
  happened (before/after view, reconciliation, signed-off evidence, a named
  metric). Tie payment to proof where the model allows it.
- **Minimal support requirement** — the least client input or access needed to
  produce the proof. Prefer async exports, samples, and non-invasive access over
  dependencies that stall delivery.
- **Follow-on / recurring value** — name the recurring need that justifies a
  retainer after the first win (cadence, refresh, monitoring, ongoing
  reconciliation). If none exists, the follow-on is one-off.

**No universal timeline.** Do not hard-code a "7–14 day" delivery or first-value
rule. Timelines are declared per opportunity and in
`validation/validation.plan.json` before results are measured.

**No low-ticket front-door requirement.** Do not require a cheap entry offer. The
fastest cash path may be a full-priced engagement; price is a per-opportunity
hypothesis, not a doctrine.

## Observable Loss logic

Prefer candidates where failure or loss is **observable**.

- **Capturable failure** — the candidate should let a review capture observable
  failure: failed reconciliations, missed SLAs, expired permits/credentials,
  churn, chargebacks, margin leakage, unreconciled accounts, unshipped
  obligations, audit exceptions.
- **Economic consequence without invented numbers** — record the consequence as a
  class (time lost, rework, blocked revenue, compliance exposure, retained cost).
  Do **not** invent dollar values. Use a figure only when it is sourced; otherwise
  the value stays `UNKNOWN`.
- **Pre-outreach observability** — where possible, confirm the loss is observable
  *before* contacting anyone (public records, filings, listings, job posts,
  reviews). This strengthens a candidate without spending on outreach.
- **Patterns, not one-industry rules** — revenue-leak examples are illustrations
  of a pattern. Do not promote a single industry example into a universal rule.
- **AI voice is not the default** — do not default to AI voice agents or any
  single technology. Select the mechanism that fits the observed loss.

## Client Value-Capture Fit

A correct deliverable to an unready client captures no value.

- **Client readiness** — does the client have the capability, attention, and
  authority to act on the deliverable?
- **Downstream bottlenecks** — identify what happens after delivery (legal
  review, IT approval, staffing, budget cycle) that could block value capture.
- **Provider control vs client control** — separate outcomes the provider
  controls (delivery quality, timeliness, evidence, the proof artifact) from
  outcomes the client controls (execution, adoption, approvals, resourcing).
- **Client failure is not automatically offer failure** — if a client fails to
  realize value, analyze whether the cause is provider-controlled or
  client-controlled before concluding the offer failed.
- **No unsupported failure-rate statistics.** Do not encode claims such as
  "80–90% of clients fail"; such a figure is doctrine only with local evidence.

## Build-and-Release delivery logic

Separate building from running.

- **One-time implementation vs recurring value** — distinguish the one-time
  build/implementation from the recurring value (monitoring, refresh, ongoing
  reconciliation, reporting).
- **Explicit delivery boundaries** — state what is in and out of scope per
  engagement so proof and expectations are shared.
- **Retainers require recurring value** — a recurring retainer is justified only
  by a recurring need. One-off work is priced as one-off.
- **Provider vs client outcomes** — recurring value must be provider-deliverable,
  not dependent on client behavior the provider cannot influence.
- **No universal pricing assumptions** — do not assume a price level, a
  percentage, or a "retain only 20%" style rule. Pricing is a per-opportunity
  hypothesis declared before measuring.

## Cash-flow-backed sourcing

Where money already flows is stronger evidence than novelty.

- **Existing revenue/spend as category evidence** — a category with real
  budget in motion (software, labor, agency, contractor, consultant) is
  inherently higher-signal than an unproven category.
- **Asking price alone is not business quality** — a high acquisition/list asking
  price is a signal to investigate, not proof of a good business.
- **Product Hunt engagement is not payment evidence** — launches, upvotes, and
  attention are not revenue; treat them as competitor/market evidence only.
- **A proven category still needs a sharp wedge** — proven category + visible
  spend + hated/expensive incumbent + nameable wedge.
- **Cheap-clone logic is rejected as sufficient moat** — "we're cheaper" is not a
  wedge.
- **Distribution, churn, support, and execution burden remain in scope** for
  every cash-flow-backed candidate.

---

## Opportunity Intake Record

Every idea discovered through this method must be converted into a structured
Opportunity Record before evaluation. The OS already has the durable structure it
needs — the **append-only evidence ledger** (`evidence/evidence.jsonl`, KC-05) and
the falsifiable **thesis** (`thesis.json`). The Opportunity Record below is the
human-facing worksheet that maps onto those existing artifacts. It introduces no
new schema and no new document type.

Capture:

### Signal
What behavior, complaint, workaround, review, or observed pattern revealed the
opportunity?
→ capture as evidence `claim` + `source`.

### Evidence Type
- customer evidence
- market evidence
- competitor evidence
- behavioral evidence
- economic evidence
- distribution evidence

→ map to the existing `evidence_type` (`TRANSACTION | CONTRACTUAL | CUSTOMER |
MARKET | ANECDOTE | ASSUMPTION`) and `source_type` (`INTERVIEW | RECORD |
AGREEMENT | CHARGE | PUBLICATION | OBSERVATION | OTHER`). Competitor/behavioral
evidence is usually `MARKET`/`CUSTOMER` with `source_type: OBSERVATION`.

### Existing Workaround
How are users currently solving the problem?
Examples: spreadsheet, manual labor, copy/paste, custom script, VA, agency,
several software tools, existing competitor.
→ record as an observed `CUSTOMER`/`MARKET` evidence item.

### Frequency
How often does the problem occur?
Examples: many times per day, daily, weekly, occasionally, one-time project.
→ state it in the `claim`; do not treat frequency as a gate threshold.

### Existing Alternatives
What products, services, agencies, scripts, or manual processes currently compete
with the opportunity?
→ this is the competitive/alternative landscape; feeds the offer and the
"existing spend" signal.

### Complaint Pattern
What repeatedly frustrates users? Separate: feature request, mild annoyance, time
loss, direct cost, revenue loss, operational bottleneck, compliance/risk exposure.
→ use the tier table in Method 2; a *feature request* is the weakest signal.

### Reachable Buyer
Define the buyer narrowly. Capture: role, business type, industry, platform,
community, where they can actually be reached.
→ do not accept "small businesses" or similarly vague audience definitions. The
reachable-buyer path is recorded in `distribution.json`
(`first_customer_path`, `validation_distribution.channels`).

### Economic Pain
Does the problem: make money, lose money, save money, save meaningful time,
increase throughput, block revenue, delay projects, cause rework, create
compliance/operational risk, or cause sufficiently intense frustration to justify
payment?
→ captured as evidence, and later reflected in `economics.json` (owner time,
margins, cost structure).

### Existing Spend
Proof users already spend money or labor trying to solve the issue: software
subscription, employee hours, contractor, agency, VA, consultant, custom
development, paid workaround, lost margin, lead acquisition, operational
overhead.
→ existing spend is `MARKET`/`CUSTOMER` at minimum; a real charge is
`TRANSACTION` and is the strongest demand signal.

### Finished Outcome
What exact business result is purchased? State the finished outcome (for example:
"audit-ready access-evidence pack", "reconciled margin report", "approved
subcontractor packet"), never "an AI tool."

### Proof-First Win
Design the offer around a provable outcome:
- finish line (the verifiable "done" moment the buyer pays for)
- early win (a small, visible result before the finish line)
- proof mechanism (the artifact/measurement that shows it happened)
- minimal support requirement (least client input/access needed)
- follow-on / recurring value (the recurring need that justifies a retainer)
→ no hard-coded delivery window; no required low-ticket front door.

### Observable Loss
What observable failure or loss does this address? Capture the pattern (failed
reconciliation, missed SLA, expired credential, churn, chargeback, margin
leakage, audit exception) and its economic **class** (time, rework, blocked
revenue, compliance exposure, retained cost). Record a dollar value only if it is
sourced; otherwise `UNKNOWN`. Note whether the loss is observable **before**
outreach.

### Business Model Fit
Which model best matches buyer behavior, monetization, distribution, founder
resources, validation speed, automation path, and owner independence?

```
software subscription | productized service | fractional retainer |
lead generation | affiliate | pay-per-call | platform app | hybrid
```

Do not force every opportunity into SaaS. The chosen model should fit the
opportunity, not a default.

### Fastest Cash Path
How could this generate its **first dollar**? Record the concrete mechanism:
fixed-fee audit | paid pilot | lead commission | affiliate conversion | manual
concierge delivery | productized service | pre-sale | setup fee | recurring
retainer. A hoped-for future subscription is not a first cash path.

### Manual Validation Path
Can real willingness to pay be tested **before** building software? Describe the
cheapest manual/concierge test that produces either a payment or a clear refusal.

### Automation Path
If validation succeeds, which repeated work can be automated? Identify the
repeatable step(s) that could later be scripted, standardized, or productized.
If nothing can be automated, say so explicitly.

### Recurring Revenue Path
Why would the buyer keep paying? Name the recurring need (audit cadence, monthly
close, weekly reporting, continuous monitoring). If the need is one-off, record
that — do not invent recurrence.

### Owner-Dependence Check
Ask: *if this works, do I own a business or have I created another job for
myself?* Use existing qualitative conventions (no new numeric score):

```
FOUNDERS' MANUAL WORK REQUIRED:   LOW | MEDIUM | HIGH
AUTOMATION POTENTIAL:             LOW | MEDIUM | HIGH
FULFILLMENT STANDARDIZATION:      LOW | MEDIUM | HIGH
RECURRING REVENUE:                LOW | MEDIUM | HIGH
```

A manual service can still pass validation **if it is clearly a bridge to
automation**; flag high owner-dependence when delivery cannot be standardized.

### Client Value-Capture Risk
Can the client actually capture the value?
- client readiness (capability, attention, authority to act)
- downstream bottlenecks after delivery (legal, IT, staffing, budget cycle)
- what the **provider** controls vs what the **client** controls
- qualitative risk: `LOW | MEDIUM | HIGH`
→ a client-side failure is not automatically an offer failure; analyze the cause
before concluding the offer is wrong. Do not encode unsupported failure-rate
statistics.

### Fastest Validation
The cheapest experiment capable of testing willingness to pay. Prefer: manual
service, concierge MVP, landing page plus outreach, pre-sale, paid audit, paid
pilot, done-for-you version, prototype shown directly to target users.
→ write it into `validation/validation.plan.json` (`hypothesis`, `method`,
`success_threshold`, `failure_threshold`, `evidence_required`, `deadline`,
`resulting_decision`). Avoid production engineering before demand is tested (see
the pre-BUILD refusal rule in `KERNEL.md` §4 and `distribution.json`).

**Validation strength is evidence-based, not a call count.** Do not require a
fixed number of calls. Obtain direct buyer evidence strong enough to justify
code before product build. Depending on the opportunity this may be 5
interviews, 10 outreach conversations, 1 paid pilot, 2 proposal requests, 1
deposit, successful lead conversions, or a productized manual-service sale.
**Payment-level evidence is stronger than conversation count.**

### Opportunity Record template

```markdown
## Opportunity: <one-line name>
- Signal (what made us notice):
- Revenue archetype:                 # vertical software | productized service | fractional ops/data | intent utility | lead-gen utility | platform add-on | repeated-work productization
- Evidence type(s):                  # TRANSACTION | CONTRACTUAL | CUSTOMER | MARKET | ANECDOTE | ASSUMPTION
- Existing workaround:
- Frequency:
- Existing alternatives:
- Complaint pattern / tier:          # annoyance | repeated inconvenience | operational pain | commercial pain
- Reachable buyer (narrow):
    - role:
    - business type / industry:
    - platform / community:
    - where reachable:
- Economic pain:
- Existing spend:
- Finished outcome:                  # the purchased business result (not a tool)
- Proof-first win:                    # finish line + early win + proof mechanism + minimal support + follow-on
- Observable loss:                    # observable failure pattern + economic class (no invented dollars)
- Business model fit:                # software subscription | productized service | fractional retainer | lead gen | affiliate | pay-per-call | platform app | hybrid
- Fastest cash path:                 # first dollar: audit | pilot | concierge | pre-sale | retainer | lead commission | ...
- Manual validation path:            # cheapest willingness-to-pay test, pre-code
- Automation path:                   # what repeated work can be automated; or "none"
- Recurring revenue path:            # why the buyer keeps paying; or "one-off"
- Owner-dependence check:
    - founders' manual work required:  # LOW | MEDIUM | HIGH
    - automation potential:            # LOW | MEDIUM | HIGH
    - fulfillment standardization:     # LOW | MEDIUM | HIGH
    - recurring revenue:               # LOW | MEDIUM | HIGH
- Client value-capture risk:         # LOW | MEDIUM | HIGH (provider- vs client-controlled; downstream bottlenecks)
- Fastest validation:                # cheapest willingness-to-pay test
- Falsification (what would kill this):
- Missing evidence / unknowns:
- Evidence refs:                     # ev_<ulid> ... (from evidence/evidence.jsonl)
- Thesis ref:                        # thesis.json
```

---

## Evidence discipline

If the OS already has an evidence schema, use it. It does:
`record_type` is `FACT | INTERPRETATION | FORECAST`; `verification_status` is
`VERIFIED | PENDING | DISPUTED | REJECTED`; `correction` is `NONE | CORRECTION |
SUPERSEDES | INVALIDATED | DISPUTED`. The discovery tags map as follows:

| Discovery tag | OS equivalent |
| --- | --- |
| `OBSERVED` | `record_type: FACT`, `verification_status: VERIFIED`, with a real `source` |
| `INFERRED` | `record_type: INTERPRETATION` (a reasoned conclusion from facts) |
| `CLAIMED` | `verification_status: PENDING` (or `DISPUTED`), `source_type: OTHER` |
| `UNKNOWN` | **no ledger record** — or `ASSUMPTION`, which scores **0** toward any gate |

Rules:

- Do not upgrade an inference into a fact.
- Unknown evidence stays unknown.
- Never manufacture validation because an idea fits our interests.
- When external evidence is later gathered, preserve source references
  (`source`, `source_type`) and content hashes; corrections append, never delete.
- Assumptions score 0, and anecdotes cannot independently justify a gate
  (`KERNEL.md` §5). Gate-qualifying types are `TRANSACTION | CONTRACTUAL |
  CUSTOMER | MARKET`.

The system must be able to answer:

- What made us notice this idea?
- What evidence supports the problem?
- Who has the problem?
- What are they doing today?
- What are they already paying?
- How do we reach them?
- What would falsify the opportunity?
- What is the cheapest test?
- What evidence would justify proceeding?

---

## Discovery-to-Evaluation Routing

This discovery method does not decide whether to build. Every opportunity flows
into the existing evaluation system. Expected route:

```
DISCOVER
→ CAPTURE EVIDENCE            (evidence/evidence.jsonl, KC-05)
→ CREATE OPPORTUNITY RECORD   (worksheet + thesis.json)
→ RUN EXISTING OPPORTUNITY FILTER / VALIDATION GATE   (gates.json → VALIDATION)
→ RUN EVIDENCE GATE           (qualifying + eligible evidence only, KC-06/KC-09)
→ RUN DISTRIBUTION / REACHABILITY CHECK   (distribution.json)
→ RUN ECONOMICS               (economics.json)
→ RUN RISK CHECKS             (risk.json)
→ DECISION
```

### Decision vocabulary — preserve the existing labels

The OS expresses outcomes through its existing transition targets and gate
results. Do **not** create alternate decision states.

| Meaning | Existing OS label |
| --- | --- |
| Advance / test commercially | transition `DISCOVERY → VALIDATION` (deterministic) |
| Evidence insufficient, keep testing | remain in `DISCOVERY`/`VALIDATION`; gate result `BLOCKED`, with missing requirements listed |
| Proven / proceed to build | `VALIDATION` gate `PASS` → transition `VALIDATION → OFFER` |
| Re-work the opportunity | transition to `RE_ENGINEERING` |
| Abandon | transition to `KILLED` (HUMAN_ONLY) |

If a project declares its own outcome labels in `gates.json` (for example
`PASS | CONTINUE | REENGINEER`), keep **those** labels. Do not introduce a second
set.

### Bad idea vs. unvalidated idea

The OS must distinguish:

```
bad idea          -> evidence exists and contradicts the thesis
                     (route to RE_ENGINEERING or KILLED)
unvalidated idea  -> no evidence yet, but a cheap validation path exists
                     (keep in DISCOVERY/VALIDATION; open a validation experiment)
```

Do not reject solely because evidence is absent if a cheap validation path
exists. `BLOCKED` (missing evidence) is not `FAIL` (contradicting evidence).

---

## Hard rules

These are **discovery principles**, not constitutional rules. They inform
practice and the playbook; they do not modify the kernel or its gates.

1. Evidence of demand is more valuable than idea novelty.
2. Competitors are not automatic disqualification.
3. Repeated workarounds are evidence worth investigating.
4. Repeated complaints are stronger than isolated requests.
5. Reachability is part of opportunity quality.
6. Existing buyer effort or spend is meaningful evidence.
7. Prefer cheap payment-intent tests before software development.
8. Do not confuse interest with willingness to pay.
9. Do not confuse a requested feature with a viable business.
10. Do not allow an LLM to infer market demand without evidence.
11. Unknown evidence stays unknown.
12. Never manufacture validation because an idea fits our interests.
13. A technically easy idea can still be commercially weak.
14. A crowded category can still be attractive if there is a sharp underserved wedge.
15. "Nobody has built this" is not automatically a positive signal.
16. Hunt for revenue mechanisms, not only software ideas.
17. When evidence is comparable, prefer the opportunity with the faster and cheaper first cash path.
18. Repeated paid custom work is a productization signal, not automatically a business.
19. Search intent is a demand signal, not proof of a business; a viable economic path is required.
20. A productized service or fractional retainer can be a valid first model — do not force SaaS.
21. Evaluate owner dependence: a manual service must be a clear bridge to automation, not a permanent job.
22. Do not treat search volume, affiliate economics, or lead economics as proven without evidence.
23. Design offers around a provable outcome (finish line + early win + proof mechanism); activity is not payment.
24. Match effort to the minimal support requirement; prefer async, non-invasive client input.
25. Prefer candidates with observable loss; record the economic consequence without inventing dollar values.
26. A recurring retainer must be backed by recurring value; one-off work is priced one-off.
27. Separate provider-controlled outcomes from client-controlled outcomes; a client failure is not automatically an offer failure.
28. Existing revenue/spend is category evidence; a high asking price or launch traction is not payment evidence.
29. Do not hard-code universal delivery windows, low-ticket front doors, or "retain X%" pricing rules.
30. AI voice (or any single technology) is not the default solution.

---

## Discovery prompts

The OS stores no separate prompt library; these are reusable research prompts
that live with the discovery method. Run them against the target buyer group and
capture outputs as evidence, not as conclusions.

### Workaround Prompt
Find processes where people currently use spreadsheets, repetitive copy/paste,
custom scripts, several disconnected tools, or manual labor to complete a
recurring task. Identify the user, frequency, cost, workaround, and evidence
source.

### Complaint Prompt
Find recurring complaints from a narrow buyer group. Group complaints by repeated
pattern rather than collecting random feature requests. Identify which complaints
create measurable money, time, throughput, or operational pain.

### Competitor Gap Prompt
Find existing paid products serving the target workflow. Analyze recurring
low-star complaints and ignored requests. Identify whether there is a narrow
segment or use case the incumbent serves poorly.

### Adjacent Market Prompt
Find a proven solution in one market or platform that may solve a similar problem
for an underserved adjacent audience. Require independent evidence that the
adjacent audience experiences the same pain.

### High-Intent Search Prompt
List category-specific buying queries for the target workflow
(`"<vertical> calculator"`, `"<industry> cost estimator"`, `"<process>
checklist"`). For each, assess commercial intent, how the intent is served today,
monetization fit, and whether a single-purpose utility delivers meaningful value.
Record search demand as evidence; do not assume it.

### Fractional Service Prompt
Find businesses that repeatedly reconcile systems, clean spreadsheets, prepare
weekly reports, compare billing against operations, track exceptions, or produce
recurring management summaries. Determine whether the result can be sold
manually, is recurring, can be standardized, and can later be automated.

### Repeated-Work Prompt
Find custom work a provider has delivered multiple times to different clients
(the same spreadsheet cleanup, report, or integration). Treat repetition + shared
workflow + similar buyer as a productization candidate; still evaluate
distribution, implementation burden, support burden, and defensibility.

### Proven-Category Wedge Prompt
Find a proven category with visible buyer spend and a hated, expensive, or
bloated incumbent. Identify a sharp wedge (narrow vertical, lower complexity,
pricing, regional/payment support, specialization, better implementation or
integration). Reject "cheaper clone" as a standalone moat.

### Observable Loss Prompt
Find recurring failures or leakage that are observable before outreach: failed
reconciliations, missed SLAs, expired credentials/permits, churn, chargebacks,
margin leakage, unreconciled accounts, audit exceptions. Capture the pattern and
its economic **class**; do not invent dollar values.

### Proof-First Offer Prompt
For a candidate, define the finish line the buyer pays for, a small early win, the
proof mechanism that demonstrates the outcome, the minimal support requirement,
and the follow-on recurring value. Reject offers that cannot produce provable
outcomes.

---

## Concept translation — SJCodes 5-point filter → existing gates

**Do not add the 5-point filter as another numerical scoring framework.** The
concepts it carries are already owned by the existing OS; map them as follows:

| Concept | Existing OS mechanism |
| --- | --- |
| Real problem | `thesis.json` (statement + falsification) and `VALIDATION` gate clauses |
| Identifiable user | evidence `source`/`source_type` + Opportunity Record "Reachable Buyer" |
| Reachable user | `distribution.json` (`first_customer_path`, `validation_distribution.channels`) |
| Active workaround | `CUSTOMER`/`MARKET` evidence with `source_type: OBSERVATION` |
| Existing demand | qualifying `MARKET`/`CUSTOMER` evidence; existing spend as `TRANSACTION` |
| Payment-level pain | `TRANSACTION`/`CONTRACTUAL` evidence (highest tiers) |
| Fast MVP validation | `validation/validation.plan.json` + capability `VALIDATION.DISPOSABLE_ARTIFACT` (tied to a documented uncertainty) |
| Fastest cash path | `validation/validation.plan.json` (`method` + `success_threshold`) — the first-cash test |
| Revenue archetype / business model | a classification lens (`thesis.json` + `economics.json`); **not** a gate or score |
| Recurring revenue / owner independence | `economics.json` (owner/founder time at target revenue) + the `OWNER_DEPENDENCE` policy domain (KERNEL §2) |
| Proof-first win (finish line / early win / proof mechanism) | `validation/validation.plan.json` (`method`) + qualifying `TRANSACTION`/`CUSTOMER` evidence of the proven outcome |
| Observable loss | an evidence `claim` with `source_type: RECORD`/`OBSERVATION` — capture the economic class, never an invented figure |
| Client value-capture risk | `risk.json` + `distribution.json` (provider- vs client-controlled outcomes) |
| Build-and-release (one-time vs recurring) | `economics.json` + declared delivery scope in the offer / `validation.plan.json` |

There is **one** evaluator (the Gate Engine) and **one** decision path. This
playbook produces inputs for them; it never scores or approves on its own.

---

## OS behavior on raw idea intake

After this playbook, when the OS is given a raw idea, it should **not** immediately
brainstorm features. It should first attempt to determine:

1. what observable problem exists
2. who experiences it
3. what they do now
4. whether demand already exists
5. what alternatives exist
6. whether users are reachable
7. whether the pain has economic weight
8. what evidence is missing
9. what the cheapest validation experiment is

Only then should it route the idea into the current evaluation gates. If the idea
has no evidence yet, the system should say so. It should not reject solely
because evidence is absent if a cheap validation path exists. Instead it should
distinguish **bad idea** from **unvalidated idea** and route accordingly using the
existing OS terminology.

---

## Anti-patterns (explicitly out of scope)

- A second scoring model, scorecard, or weighting scheme.
- A new gate, evidence tier, approval level, or decision state.
- Treating a workaround, a complaint, or "nobody built this" as approval.
- Promoting an `ANECDOTE` or `ASSUMPTION` into gate-qualifying evidence.
- Blind adjacent-market cloning without independent audience evidence.
- Production engineering before a demand test (violates the pre-BUILD refusal rule).
- Editing the frozen kernel (`KERNEL.md` / `KERNEL_COMPLETENESS.md`) because a
  framework is novel. New frameworks enter through the Knowledge Ingestion Gate
  (`KERNEL.md` §11, policy domain `KNOWLEDGE_INGESTION`) and inform practice.
- Treating search volume as demand, or building an intent utility with no
  economic path.
- Assuming affiliate, pay-per-call, or lead-generation economics without evidence.
- A generic "cheaper clone" with no nameable wedge.
- Productizing simply because work repeats, without evaluating distribution,
  implementation burden, support burden, or defensibility.
- Adding a numeric score for archetypes or owner dependence (use qualitative
  LOW/MEDIUM/HIGH conventions only).
- Hard-coding a universal delivery window (e.g. "first value in 7–14 days") or a
  mandatory low-ticket front-door offer.
- Inventing dollar values for loss, leakage, or savings.
- Treating a client's failure to execute as automatic proof the offer failed.
- Encoding unsupported client failure-rate statistics (e.g. "80–90% of clients fail").
- Treating launch/Product Hunt engagement or a high asking price as payment evidence.
- Defaulting to AI voice (or any single technology) as the solution.
- Assuming a universal retainer percentage (e.g. "retain only 20%").
