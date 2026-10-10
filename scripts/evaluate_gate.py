#!/usr/bin/env python3
"""
Sovereign Builder OS — Deterministic Gate Evaluator
Kernel v2.1 (Section 4 & 9)
Evaluates Phase Gate 1 against the immutable evidence ledger.
"""

import sys
import json
import hashlib
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
OS_DIR = ROOT / ".os"
EVIDENCE_FILE = OS_DIR / "evidence" / "evidence.jsonl"
GATES_FILE = OS_DIR / "gates.json"
ECON_FILE = OS_DIR / "economics.json"
PROJECT_FILE = OS_DIR / "project.json"

def compute_sha256(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()

def evaluate():
    print("=" * 60)
    print("SOVEREIGN BUILDER OS — PHASE GATE EVALUATOR (Kernel v2.1)")
    print("=" * 60)

    if not GATES_FILE.exists():
        print(f"Error: {GATES_FILE} not found.")
        sys.exit(1)

    with open(GATES_FILE, "r") as f:
        gates_data = json.load(f)

    gate_def = gates_data["gates"].get("GATE_COMMERCIAL_VALIDATION_14D")
    if not gate_def:
        print("Error: GATE_COMMERCIAL_VALIDATION_14D definition not found in gates.json")
        sys.exit(1)

    with open(ECON_FILE, "r") as f:
        econ_data = json.load(f)

    # Read and audit evidence
    events = []
    event_counts = {}
    tamper_detected = False

    if EVIDENCE_FILE.exists():
        with open(EVIDENCE_FILE, "r") as f:
            for idx, line in enumerate(f):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                    # Verify hash if present
                    if "hash" in record:
                        expected_hash = record["hash"]
                        payload_copy = {k: v for k, v in record.items() if k != "hash"}
                        canonical_json = json.dumps(payload_copy, sort_keys=True)
                        actual_hash = compute_sha256(canonical_json)
                        if expected_hash != actual_hash:
                            print(f"[!] Warning: Evidence line {idx+1} failed SHA-256 verification!")
                            tamper_detected = True
                    event_type = record.get("event")
                    event_counts[event_type] = event_counts.get(event_type, 0) + 1
                    events.append(record)
                except Exception as e:
                    print(f"[!] Error parsing evidence line {idx+1}: {e}")

    conversions = event_counts.get("csv_download", 0)
    intent_signals = event_counts.get("pro_intent_click", 0)
    leads_submitted = event_counts.get("pro_lead_submitted", 0)
    capital_spent = econ_data.get("capital_spent", 0.00)

    print(f"Observation Window: {gate_def['window_start']} → {gate_def['window_end']}")
    print(f"Total Evidence Records: {len(events)}")
    print(f"Tamper Check: {'PASS (Clean Hashed Ledger)' if not tamper_detected else 'FAIL (Hash Mismatch)'}")
    print("-" * 60)

    results = []
    all_passed = True

    for clause in gate_def["clauses"]:
        c_id = clause["clause_id"]
        kind = clause["kind"]
        operator = clause["operator"]
        threshold = clause["threshold"]
        desc = clause["description"]

        if kind == "evidence_count":
            event_type = clause.get("event_type")
            actual_val = event_counts.get(event_type, 0)
            if operator == ">=":
                passed = actual_val >= threshold
            elif operator == ">":
                passed = actual_val > threshold
            else:
                passed = False
        elif kind == "economic_ceiling":
            actual_val = capital_spent
            if operator == "==":
                passed = actual_val == threshold
            elif operator == "<=":
                passed = actual_val <= threshold
            else:
                passed = False
        else:
            actual_val = None
            passed = False

        status_str = "PASS" if passed else "FAIL"
        if not passed:
            all_passed = False
        results.append((c_id, desc, actual_val, operator, threshold, status_str))

    for c_id, desc, act, op, th, st in results:
        indicator = "✓" if st == "PASS" else "✗"
        print(f"[{indicator}] {c_id}: {desc}")
        print(f"    Required: {op} {th} | Actual: {act} | Verdict: {st}")

    print("-" * 60)
    final_verdict = "PASS" if (all_passed and not tamper_detected) else "FAIL"
    print(f"GATE VERDICT: {final_verdict}")
    target_state = gate_def["success_transition_target"] if final_verdict == "PASS" else gate_def["failure_transition_target"]
    print(f"TARGET STATE TRANSITION: {target_state}")
    print("=" * 60)

    # Ratify if flag passed
    if "--ratify" in sys.argv:
        with open(PROJECT_FILE, "r") as f:
            proj = json.load(f)
        old_state = proj.get("current_state")
        proj["previous_state"] = old_state
        proj["current_state"] = target_state
        proj["state_entered_at"] = datetime.utcnow().isoformat() + "Z"
        proj["revision"] = proj.get("revision", 0) + 1
        if final_verdict == "FAIL":
            proj["blocked"] = True
            proj["blocking_reason"] = f"Failed {gate_def['gate_id']} threshold evaluation."
        with open(PROJECT_FILE, "w") as f:
            json.dump(proj, f, indent=2)
        print(f"[Ratified] Project state updated from {old_state} → {target_state} (Revision {proj['revision']})")

    return 0 if final_verdict == "PASS" else 1

if __name__ == "__main__":
    evaluate()
