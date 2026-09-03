#!/usr/bin/env python3
import argparse
import glob
import json
from collections import defaultdict

VALUE_METRICS = ["clarity", "context_fit", "insight", "decision_support", "actionability", "autonomy"]
ALL_METRICS = VALUE_METRICS + ["process_cost"]
PAIRWISE = ["overall", "understands_situation", "next_action", "would_use"]


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


def main():
    p = argparse.ArgumentParser(description="Aggregate blinded LifeOS Pilot-1 evaluator scores after reveal.")
    p.add_argument("--key", required=True, help="reveal_key.json")
    p.add_argument("--evaluations", default="evaluations/*.jsonl")
    p.add_argument("--out", default="summary.json")
    args = p.parse_args()

    key = load_json(args.key)["cases"]
    score_sums = defaultdict(lambda: defaultdict(float))
    score_counts = defaultdict(lambda: defaultdict(int))
    pairwise = defaultdict(lambda: defaultdict(int))
    evaluator_ids = set()
    case_ids = set()

    files = sorted(glob.glob(args.evaluations))
    if not files:
        raise SystemExit("No evaluation files found")

    for path in files:
        for row in load_jsonl(path):
            cid = row["case_id"]
            if cid not in key:
                raise ValueError(f"Unknown case_id {cid}")
            evaluator_ids.add(row["evaluator_id"])
            case_ids.add(cid)
            side_to_condition = key[cid]
            for side_key, side_label in [("a", "A"), ("b", "B")]:
                condition = side_to_condition[side_label]
                for metric in ALL_METRICS:
                    score_sums[condition][metric] += float(row[side_key][metric])
                    score_counts[condition][metric] += 1
            for field in PAIRWISE:
                choice = row[field].strip().upper()
                if choice == "TIE":
                    pairwise[field]["tie"] += 1
                elif choice in ("A", "B"):
                    pairwise[field][side_to_condition[choice]] += 1
                else:
                    raise ValueError(f"Invalid pairwise choice {choice} in {field}")

    means = {}
    for condition in ("baseline", "lifeos"):
        means[condition] = {}
        for metric in ALL_METRICS:
            n = score_counts[condition][metric]
            means[condition][metric] = round(score_sums[condition][metric] / n, 3) if n else None

    deltas = {}
    for metric in ALL_METRICS:
        deltas[metric] = round(means["lifeos"][metric] - means["baseline"][metric], 3)

    overall = pairwise["overall"]
    decisive = overall["lifeos"] + overall["baseline"]
    lifeos_win_rate_decisive = round(overall["lifeos"] / decisive, 3) if decisive else None
    lifeos_preference_all = round(overall["lifeos"] / (decisive + overall["tie"]), 3) if (decisive + overall["tie"]) else None

    summary = {
        "evaluation_files": files,
        "evaluators": sorted(evaluator_ids),
        "evaluator_count": len(evaluator_ids),
        "case_count": len(case_ids),
        "means": means,
        "lifeos_minus_baseline": deltas,
        "pairwise": {k: dict(v) for k, v in pairwise.items()},
        "overall_lifeos_win_rate_decisive": lifeos_win_rate_decisive,
        "overall_lifeos_preference_all": lifeos_preference_all,
        "notes": {
            "positive_delta_is_better_for": VALUE_METRICS,
            "negative_delta_is_better_for": ["process_cost"]
        }
    }

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
