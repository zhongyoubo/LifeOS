# LifeOS Pilot-1 Automated Validation Toolchain

Pilot-1 separates Baseline/LifeOS generation, randomization, evaluation, aggregation, and reporting to reduce experimental bias.

## Flow

```text
cases.jsonl
   ↓
Runner A: Baseline
Runner B: LifeOS
   ↓
raw_outputs.jsonl
   ↓
randomize.py
   ├─ evaluator_pack.jsonl
   └─ reveal_key.json
   ↓
External Evaluators
   ↓
evaluations/*.jsonl
   ↓
aggregate.py
   ↓
summary.json
   ↓
report-template.md
```

## Constraints

- Same model, same user input, same available context.
- Use comparable token budgets and generation settings when possible.
- Baseline must not read LifeOS material; LifeOS uses a frozen Skill version.
- Runners do not evaluate outputs.
- The randomizer does not edit answers; it only anonymizes and maps A/B.
- Evaluators must not access the reveal key.
- Reveal only after all evaluations are locked.
- Change LifeOS only after the whole Pilot round is complete.

## File Formats

`cases.jsonl`
```json
{"case_id":"AB01","prompt":"..."}
```

`raw_outputs.jsonl`
```json
{"case_id":"AB01","baseline":"...","lifeos":"..."}
```

`evaluator_pack.jsonl`
```json
{"case_id":"AB01","response_a":"...","response_b":"..."}
```

`evaluations/*.jsonl`
```json
{"case_id":"AB01","evaluator_id":"E01","a":{"clarity":4,"context_fit":4,"insight":4,"decision_support":4,"actionability":5,"autonomy":5,"process_cost":2},"b":{"clarity":3,"context_fit":3,"insight":3,"decision_support":3,"actionability":4,"autonomy":5,"process_cost":2},"overall":"A","understands_situation":"A","next_action":"A","would_use":"A","reason":"..."}
```

## Pilot-1 Gate

- At least 10 cases; 20 recommended.
- At least 3 independent evaluators; 5 recommended.
- Overall LifeOS preference ≥ 60%.
- LifeOS should outperform Baseline on at least two of Clarity / Context Fit / Actionability.
- Autonomy must not be lower than Baseline.
- Process Cost must not systematically worsen.
- P0 = 0.

Pilot-1 is a stricter product/framework validation than Pilot-0, not final scientific proof of effectiveness.
