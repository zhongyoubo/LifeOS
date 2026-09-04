#!/usr/bin/env python3
"""Aggregate LifeOS v0.1.2 Human Validation JSONL evidence.

Usage:
  python aggregate.py --cases cases.jsonl --sessions sessions-round-01.jsonl \
    --followups followups-round-01.jsonl --output summary.json

No third-party dependencies.
"""
import argparse, json
from collections import Counter, defaultdict
from pathlib import Path


def read_jsonl(path, optional=False):
    p = Path(path)
    if optional and not p.exists():
        return []
    rows = []
    with p.open(encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as e:
                raise SystemExit(f"{p}:{n}: invalid JSON: {e}")
            if str(row.get("case_id", "")).startswith("EXAMPLE-"):
                continue
            rows.append(row)
    return rows


def mean(values):
    vals = [v for v in values if isinstance(v, (int, float)) and not isinstance(v, bool)]
    return round(sum(vals) / len(vals), 3) if vals else None


def pct(num, den):
    return round(100 * num / den, 1) if den else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", default="cases.jsonl")
    ap.add_argument("--sessions", required=True)
    ap.add_argument("--followups")
    ap.add_argument("--output", default="summary.json")
    args = ap.parse_args()

    cases = read_jsonl(args.cases)
    sessions = read_jsonl(args.sessions)
    followups = read_jsonl(args.followups, optional=True) if args.followups else []

    users = {s.get("user_id") for s in sessions if s.get("user_id")}
    case_types = Counter(c.get("case_type") for c in cases)
    activation = Counter(x for s in sessions for x in s.get("candidate_activation", []))
    runtime = Counter(s.get("runtime_level") for s in sessions)
    outcomes = Counter(s.get("outcome_type") for s in sessions)

    clarity_delta = [s["clarity_after"] - s["clarity_before"] for s in sessions if isinstance(s.get("clarity_before"), int) and isinstance(s.get("clarity_after"), int)]
    confidence_delta = [s["confidence_after"] - s["confidence_before"] for s in sessions if isinstance(s.get("confidence_before"), int) and isinstance(s.get("confidence_after"), int)]

    actionable = sum(1 for s in sessions if s.get("outcome_type") in {"action", "explore", "wait", "no_action"} and bool(str(s.get("accepted_outcome", "")).strip()))
    action_followups = [f for f in followups if f.get("action_initiated") != "not_applicable"]
    follow_positive = sum(1 for f in action_followups if f.get("follow_through") in {"yes", "partial"})

    p0 = [item for row in sessions + followups for item in row.get("p0", [])]
    p1 = [item for row in sessions + followups for item in row.get("p1", [])]

    by_candidate = defaultdict(list)
    for s in sessions:
        for c in s.get("candidate_activation", []):
            by_candidate[c].append(s)

    candidate_metrics = {}
    metric_map = {"C1": "strategy_fit", "C2": "assistance_appropriateness", "C3": "calibration_quality"}
    for c in ("C1", "C2", "C3"):
        rows = by_candidate[c]
        candidate_metrics[c] = {
            "sessions": len(rows),
            "primary_metric": metric_map[c],
            "primary_metric_mean": mean([r.get(metric_map[c]) for r in rows]),
            "autonomy_mean": mean([r.get("autonomy") for r in rows]),
            "process_cost_mean": mean([r.get("process_cost") for r in rows]),
            "analysis_paralysis_count": sum(1 for r in rows if r.get("analysis_paralysis") is True),
        }

    quick_ids = {c.get("case_id") for c in cases if c.get("case_type") == "QUICK_CONTROL"}
    quick_sessions = [s for s in sessions if s.get("case_id") in quick_ids]
    quick_high_burden = sum(1 for s in quick_sessions if s.get("framework_burden") == "high")

    gate = {
        "users_ge_5": len(users) >= 5,
        "episodes_ge_15": len(sessions) >= 15,
        "actionable_or_justified_ge_80pct": (pct(actionable, len(sessions)) or 0) >= 80,
        "followthrough_ge_70pct": None if not action_followups else (pct(follow_positive, len(action_followups)) >= 70),
        "mean_clarity_delta_gt_0": (mean(clarity_delta) or 0) > 0,
        "p0_zero": len(p0) == 0,
        "p1_zero_unresolved": len(p1) == 0,
        "quick_no_high_framework_burden": quick_high_burden == 0 if quick_sessions else None,
    }
    evaluable = all(v is not None for v in gate.values())
    gate_pass = evaluable and all(gate.values())

    summary = {
        "baseline": "LifeOS v0.1.2 Human Validation Candidate Runtime",
        "counts": {"users": len(users), "registered_cases": len(cases), "sessions": len(sessions), "followups": len(followups)},
        "case_mix": dict(case_types),
        "candidate_activation": dict(activation),
        "runtime_levels": dict(runtime),
        "outcome_types": dict(outcomes),
        "metrics": {
            "clarity_delta_mean": mean(clarity_delta),
            "confidence_delta_mean": mean(confidence_delta),
            "autonomy_mean": mean([s.get("autonomy") for s in sessions]),
            "process_cost_mean": mean([s.get("process_cost") for s in sessions]),
            "actionable_or_justified_pct": pct(actionable, len(sessions)),
            "followthrough_yes_or_partial_pct": pct(follow_positive, len(action_followups)),
            "quick_high_framework_burden_count": quick_high_burden,
            "observed_transfer_count": sum(1 for f in followups if f.get("independent_reuse") is True and f.get("transfer_evidence")),
        },
        "candidate_metrics": candidate_metrics,
        "failures": {"p0_count": len(p0), "p0": p0, "p1_count": len(p1), "p1": p1},
        "gate": gate,
        "gate_evaluable": evaluable,
        "gate_pass": gate_pass,
        "note": "Automated gate is descriptive. Final KEEP/CHANGE/DOWNGRADE/REMOVE decisions require evidence review and cannot be inferred from averages alone."
    }

    Path(args.output).write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
