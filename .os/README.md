# `.os/` — Sovereign Builder OS Governing Kernel

Governance record for **this project**, implementing the layer model from
*Sovereign Builder OS Kernel v2.1* and the *Kernel Completeness Contract v1.0*.
The runtime that reads and enforces these files lives in `kernel/` (see the repo
README and `docs/runtime.md`).

```
Constitution → Policy → Routing → Memory → Gates → State → Execution
```

**Core invariant:** execution never changes project state by itself. State
changes only after evidence is recorded, gates are evaluated, approval policy is
applied, and the transition is explicitly ratified — and the audit event is
written *before* `project.json` is updated.

## Layout

| Path | Purpose | Spec |
| --- | --- | --- |
| `project.json` | Canonical Project Record (state, gate, capabilities, version set, revision) | §6 / KC-03 |
| `thesis.json` | Project thesis + falsification condition | §3 |
| `gates.json` | Declarative gate definitions (clauses, thresholds, freshness, approval, target) | KC-08 |
| `policies.json` | Cross-cutting policy rules (DENY / REQUIRES_APPROVAL / ALLOW) | KC-02 |
| `economics.json` | Economics incl. owner/founder time at target revenue | §2 |
| `risk.json` | Legal / platform / security / operational / concentration risk register | §2 |
| `distribution.json` | Validation vs. scale distribution state and channels | §4 |
| `habits.md` | **Generated projection** over approved habits (see `knowledge/`) | §7 / KC-23 |
| `approvals.jsonl` | Append-only approval log | KC-10 |
| `events/runtime.jsonl` | Append-only runtime event ledger (audit trail) | KC-14 |
| `knowledge/knowledge.jsonl` | Append-only knowledge ledger — source of truth for habits | KC-23 |
| `migrations/migrations.jsonl` | Append-only migration audit log | KC-22 |
| `validation/validation.plan.json` | Active validation plan (single object) | §6 |
| `validation/experiments.jsonl` | Append-only experiment log | §6 |
| `validation/customer-signals.jsonl` | Append-only customer signal log | §5 |
| `evidence/evidence.jsonl` | Append-only evidence ledger | KC-05 |
| `decisions/decisions.jsonl` | Append-only decision ledger | KC-07 |
| `discovery/demand-first-idea-mining.md` | Reusable **Demand-First Idea Mining** discovery playbook (feeds the gates; not a gate) | Playbook |

`.os/` is version-controlled — institutional memory must be auditable history.

## Canonical Project Record — `project.json` (KC-03)

Required: `project_id`, `name`, `current_state`, `kernel_version`,
`policy_version`, `compatibility_version`, `revision`, `active_capabilities`.
Optional: `previous_state`, `state_entered_at`, `blocked`, `blocking_reason`,
`attestations` (boolean readiness facts a gate may require), `constitution_version`,
`design_engine_version`.

`revision` is a monotonic counter incremented on every state change; it is the
optimistic-concurrency token and the precondition an action declares.

## Gate definitions — `gates.json` (KC-08)

Gate criteria live in data, not code. Each gate is `{gate_id,
transition_target, approval_requirement, clauses[]}`. Clause kinds:

- `evidence_count` — `operator` one of `>= > == <= <`, `threshold`, `evidence_at_least`,
  optional `freshness_window_days`, `required_evidence_ids`, `deadline`,
  `allow_disputed`, `allow_pending` (both default false: disputed/pending evidence
  is excluded unless the gate policy explicitly admits it).
- `attestation` — `operator: is_true`, `field` naming a boolean in
  `project.attestations`.

Unknown operators, unknown kinds, and missing thresholds are rejected before
evaluation.

## Policy — `policies.json` (KC-02)

Cross-cutting rules evaluated **before** state/gate/capability execution. A DENY
can never be weakened by a lower layer.

```json
{
  "kernel_version": "2.1",
  "policy_version": "1.0",
  "policies": [
    {
      "policy_id": "POL-CAPITAL-LIMIT",
      "version": "1.0",
      "domain": "CAPITAL",
      "effect": "DENY",
      "match": { "side_effect_class": ["CAPITAL"], "params": { "amount_gte": 10000 } },
      "reason": "…"
    }
  ]
}
```

- `domain`: `CAPITAL | SECURITY | EVIDENCE | PERMISSIONS | LEGAL | OWNER_DEPENDENCE | KNOWLEDGE_INGESTION`.
- `effect`: `ALLOW | DENY | REQUIRES_APPROVAL`. Precedence: **DENY > REQUIRES_APPROVAL > ALLOW**.
- `match`: any of `intent`, `capability`, `side_effect_class`, `state` (lists), and
  `params` conditions (`<param>_gt|gte|lt|lte|eq`). All specified keys must match.

## Evidence — `evidence/evidence.jsonl` (KC-05 / KC-06)

```json
{
  "evidence_id": "ev_<ulid>",
  "timestamp": "ISO-8601",
  "evidence_type": "TRANSACTION | CONTRACTUAL | CUSTOMER | MARKET | ANECDOTE | ASSUMPTION",
  "record_type": "FACT | INTERPRETATION | FORECAST",
  "source": "…",
  "source_type": "INTERVIEW | RECORD | AGREEMENT | CHARGE | PUBLICATION | OBSERVATION | OTHER",
  "verification_status": "VERIFIED | PENDING | DISPUTED | REJECTED",
  "claim": "…",
  "content_hash": "sha256:<hex>",
  "valid_until": "ISO-8601 | null",
  "correction": "NONE | CORRECTION | SUPERSEDES | INVALIDATED | DISPUTED",
  "supersedes_id": "ev_<ulid> | null",
  "recorded_by": "human:operator"
}
```

A gate counts only evidence that is **VERIFIED**, of a qualifying type
(`TRANSACTION`/`CONTRACTUAL`/`CUSTOMER`/`MARKET`), at or above the clause's
`evidence_at_least` tier, not superseded/invalidated/disputed, and not stale.
Assumptions score 0; anecdotes cannot independently justify a gate.
`SUPERSEDES`/`INVALIDATED` require `supersedes_id`.

## Approvals — `approvals.jsonl` (KC-10)

An approval is bound to one exact operation by `action_hash` and `scope`; it is
never a general permission.

```json
{
  "approval_id": "appr_<ulid>",
  "timestamp": "ISO-8601",
  "action_hash": "sha256:<hex>",
  "action_ref": { "…": "…" },
  "scope": { "kind": "capability | transition", "…": "…" },
  "actor": "human:operator",
  "decision_owner": "HUMAN | AUTOMATED_POLICY | AGENT_RECOMMENDATION",
  "reason": "…",
  "policy_version": "2.1",
  "approval_level": "AUTO_APPROVE | HUMAN_APPROVE | HUMAN_ONLY | DENY",
  "risk_class": "STANDARD | GUARDED",
  "status": "GRANTED | REVOKED | EXPIRED | REJECTED",
  "expires_at": "ISO-8601 | null",
  "revokes_id": "appr_<ulid> (revocation records only)"
}
```

## Runtime events — `events/runtime.jsonl` (KC-14)

```json
{
  "event_id": "evt_<ulid>",
  "event_type": "STATE_CHANGED",
  "timestamp": "ISO-8601",
  "kernel_version": "2.1",
  "correlation_id": "cmd_<ulid>",
  "causation_id": "evt_<ulid> | null",
  "project_revision": 1,
  "actor": "human:operator",
  "subject": { "…": "…" },
  "payload": { "…": "…" }
}
```

`correlation_id` groups every event of one command; `causation_id` links an event
to the event that caused it.

## Knowledge — `knowledge/knowledge.jsonl` (KC-23)

Append-only. This is the **source of truth** for habits; `habits.md` is a
projection rendered from it (`python3 -m kernel <root> habits`). Promotion:
`OBSERVATION → CANDIDATE_HABIT → REVIEW → APPROVED_HABIT` (+ `CONFLICT_REVIEW`,
`DEMOTED`, `REOPENED`). One observation cannot promote; a candidate needs
repeated supporting evidence; promotion needs a human/policy review.

```json
{
  "knowledge_id": "kn_<ulid>",
  "habit_key": "lowercase-slug",
  "event_type": "OBSERVATION | CANDIDATE_HABIT | REVIEW_DECISION | HABIT_APPROVED | HABIT_DEMOTED | CONFLICT_DETECTED",
  "timestamp": "ISO-8601",
  "statement": "…",
  "supporting_ids": ["ev_<ulid>", "dec_<ulid>"],
  "actor": "human:operator",
  "kernel_version": "2.1",
  "policy_version": "1.0",
  "scope": "… | null",
  "exceptions": "… | null",
  "decision": "APPROVE | REJECT | CONFLICT (REVIEW_DECISION only)"
}
```

## Migrations — `migrations/migrations.jsonl` (KC-22)

Append-only audit log of explicit schema migrations. Migrations are versioned,
backed up (`.os/.backups/<stamp>/`), reversible on failure, and idempotent.
There is no auto-migration on startup.

## Discovery — `discovery/` (playbook, not a gate)

`discovery/demand-first-idea-mining.md` is a reusable playbook for generating
opportunity candidates from **demonstrated demand** (workarounds, complaints,
competitor gaps, adjacent markets, high-intent search, fractional/recurring data
services, repeated custom work, and proven categories with a sharp wedge) before
they enter evaluation. It hunts for **revenue mechanisms, not only software
ideas**, and classifies candidates by archetype (vertical software, productized
service, fractional operations/data service, intent utility, lead-generation
utility, platform add-on, repeated-work productization). It feeds the existing
pipeline — it does not add a gate, a score, an evidence tier, or a decision
state.

Expected route:

```
DISCOVER -> CAPTURE EVIDENCE -> CREATE OPPORTUNITY RECORD
         -> existing VALIDATION gate -> evidence eligibility -> distribution
         -> economics -> risk -> DECISION
```

Discovery findings are captured with the existing evidence schema
(`evidence/evidence.jsonl`); the cheapest willingness-to-pay test is written into
`validation/validation.plan.json`. Demand is only ever established by eligible,
verified evidence — never by the playbook itself. An unvalidated idea with a
cheap test stays in DISCOVERY/VALIDATION (`BLOCKED`, not rejected); only
contradicting evidence routes an idea to RE_ENGINEERING or KILLED.

## Identifier conventions

Every id is a fixed prefix plus a 26-character ULID (Crockford base32):

```
evidence ev_   decision dec_   approval appr_   event evt_
experiment exp_   transition tr_   command cmd_   action act_   knowledge kn_   project proj_
```

## Placeholder convention

Fields whose true value is unknown at scaffold time are `null`. They are **not**
defaults — declare them before measuring, per the anti-hindsight rule in §9.
