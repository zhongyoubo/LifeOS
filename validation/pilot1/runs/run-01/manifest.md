# Pilot-1 Generation Run 01

- Model: GPT-5.6 Sol
- Cases: 20 standard scenarios
- Conditions: Baseline vs frozen LifeOS v0.1.1
- Pairing: same model family and same user prompt
- Randomization: independent per case
- Status: GENERATED / READY FOR EXTERNAL BLIND EVALUATION

## Important methodological limitation

Both conditions were generated inside the same ChatGPT execution environment. This preserves matched-model generation, but it is not an independent runner and the generator knows the LifeOS condition. Therefore this run can support blind external evaluation of outputs, but should not be described as a fully independent randomized controlled experiment.

The evaluator pack is randomized per case and contains no condition labels.

## Blinding rule

Because this repository is public, the Reveal Key is intentionally **not committed before scoring completes**. A SHA-256 commitment of the exact Reveal Key is committed instead, so the mapping cannot be changed after seeing evaluator results. After the evaluation lock, the Reveal Key can be published and verified against the commitment.

## Files

- `raw_outputs.jsonl` — unblinded paired outputs; framework coordinator / audit material; evaluators must not read it
- `evaluator_pack.jsonl` — blinded evaluator material
- `reveal-commitment.json` — cryptographic commitment to the hidden mapping
- Reveal Key — withheld until evaluation lock

## Evaluator boundary

For a valid blind evaluation, evaluators should receive only `evaluator_pack.jsonl` plus the evaluation rubric/schema. They must not inspect `raw_outputs.jsonl`, prior validation runs, LifeOS Skill files, or repository history before submitting scores.
