#!/usr/bin/env python3
import argparse
import hashlib
import json
import random
from pathlib import Path


def read_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


def write_jsonl(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main():
    p = argparse.ArgumentParser(description="Randomize LifeOS Pilot-1 Baseline/LifeOS outputs into anonymous A/B pairs.")
    p.add_argument("input", help="raw_outputs.jsonl")
    p.add_argument("--pack", default="evaluator_pack.jsonl")
    p.add_argument("--key", default="reveal_key.json")
    p.add_argument("--seed", type=int, required=True, help="Record and protect this seed until reveal.")
    args = p.parse_args()

    rng = random.Random(args.seed)
    pack = []
    key = {"seed_sha256": hashlib.sha256(str(args.seed).encode()).hexdigest(), "cases": {}}

    for row in read_jsonl(args.input):
        case_id = row["case_id"]
        baseline = row["baseline"]
        lifeos = row["lifeos"]
        lifeos_side = rng.choice(["A", "B"])
        if lifeos_side == "A":
            a, b = lifeos, baseline
        else:
            a, b = baseline, lifeos
        pack.append({"case_id": case_id, "response_a": a, "response_b": b})
        key["cases"][case_id] = {"A": "lifeos" if lifeos_side == "A" else "baseline", "B": "baseline" if lifeos_side == "A" else "lifeos"}

    write_jsonl(args.pack, pack)
    Path(args.key).write_text(json.dumps(key, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(pack)} cases to {args.pack}")
    print(f"Reveal key written to {args.key}; keep it hidden from evaluators.")


if __name__ == "__main__":
    main()
