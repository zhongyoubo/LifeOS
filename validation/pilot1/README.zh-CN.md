# LifeOS Pilot-1 自动化验证工具链

Pilot-1 的目标是把 Baseline / LifeOS 生成、随机化、评估、聚合和报告拆成独立步骤，减少实验偏差。

## 流程

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
report-template.zh-CN.md
```

## 实验约束

- 同模型、同用户输入、同可用上下文。
- 尽可能使用相同 token budget 与 generation settings。
- Baseline 不读取 LifeOS 资料；LifeOS 使用冻结版本 Skill。
- Runner 不负责评价。
- Randomizer 不修改回答内容，只做匿名映射。
- Evaluator 不得访问 reveal key。
- 所有评价锁定后才能揭盲。
- LifeOS 更新只能发生在整轮 Pilot 完成后。

## 文件格式

### `cases.jsonl`

```json
{"case_id":"AB01","prompt":"..."}
```

### `raw_outputs.jsonl`

```json
{"case_id":"AB01","baseline":"...","lifeos":"..."}
```

### `evaluator_pack.jsonl`

```json
{"case_id":"AB01","response_a":"...","response_b":"..."}
```

### `evaluations/*.jsonl`

```json
{"case_id":"AB01","evaluator_id":"E01","a":{"clarity":4,"context_fit":4,"insight":4,"decision_support":4,"actionability":5,"autonomy":5,"process_cost":2},"b":{"clarity":3,"context_fit":3,"insight":3,"decision_support":3,"actionability":4,"autonomy":5,"process_cost":2},"overall":"A","understands_situation":"A","next_action":"A","would_use":"A","reason":"..."}
```

## Pilot-1 Gate

- 至少 10 个 Case，推荐 20 个。
- 至少 3 位独立 Evaluator，推荐 5 位。
- Overall Preference ≥ 60%。
- Clarity / Context Fit / Actionability 至少两项平均优于 Baseline。
- Autonomy 不低于 Baseline。
- Process Cost 不得出现明显系统性恶化。
- P0 = 0。

Pilot-1 不是医学或社会科学意义上的最终有效性证明，而是比 Pilot-0 更严格的产品/框架验证。
