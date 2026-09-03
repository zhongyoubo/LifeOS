#!/usr/bin/env bash
set -euo pipefail

MODEL="${MODEL:-}"
RUNNER_COMMAND="${RUNNER_COMMAND:-}"
SEED="${SEED:-lifeos-pilot1}"

if [[ -z "$MODEL" || -z "$RUNNER_COMMAND" ]]; then
  echo "Usage: MODEL=<model-id> RUNNER_COMMAND='<command>' bash validation/pilot1/run.sh" >&2
  echo "The command must read LIFEOS_SYSTEM_PROMPT and LIFEOS_USER_PROMPT and print one response." >&2
  exit 2
fi

python3 validation/pilot1/runner.py \
  --cases validation/pilot1/cases.jsonl \
  --skill skills/lifeos/SKILL.md \
  --out validation/pilot1/raw_outputs.jsonl \
  --model "$MODEL" \
  --command "$RUNNER_COMMAND"

python3 validation/pilot1/randomize.py \
  --input validation/pilot1/raw_outputs.jsonl \
  --pack validation/pilot1/evaluator_pack.jsonl \
  --key validation/pilot1/reveal_key.json \
  --seed "$SEED"

echo "Pilot-1 generation complete."
echo "Evaluator material: validation/pilot1/evaluator_pack.jsonl"
echo "Keep private: validation/pilot1/reveal_key.json"
