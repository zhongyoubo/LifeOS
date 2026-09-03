# Pilot-1 Generation Run 01

- Model: GPT-5.6 Sol
- Cases: 20 standard scenarios
- Conditions: Baseline vs frozen LifeOS v0.1.1
- Pairing: same model family and same user prompt
- Randomization seed: stored in reveal key
- Status: GENERATED / READY FOR EXTERNAL BLIND EVALUATION

## Important methodological limitation

Both conditions were generated inside the same ChatGPT execution environment. This preserves matched-model generation, but it is not an independent runner and the generator knows the LifeOS condition. Therefore this run can support blind external evaluation of outputs, but should not be described as a fully independent randomized controlled experiment.

The evaluator pack is randomized per case and contains no condition labels. Evaluators must not read `reveal_key.json` before submitting scores.

## Files

- `raw_outputs.jsonl` — unblinded paired outputs; coordinator only
- `evaluator_pack.jsonl` — blinded evaluator material
- `reveal_key.json` — hidden mapping; coordinator only
