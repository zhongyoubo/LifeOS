# Blind / Human A/B Validation Protocol

[English](./blind-ab-protocol.md) | **简体中文**

本协议用于验证：LifeOS 是否比优秀通用 AI 多提供稳定、可复用、值得维护的结构性价值。

## 1. 冻结基线

测试开始后，以下内容冻结，不允许根据单个结果即时修改：

- `docs/spec-v0.1.md`
- `docs/architecture.md`
- `skills/lifeos/SKILL.md`
- Foundation Models
- Core OS
- Validation Rubric

任何框架修改必须等一轮测试结束后进入下一版本。

## 2. A/B 条件

### A — Baseline

使用同一基础模型，以优秀通用 AI 助手方式回答，不提供 LifeOS Skill、LifeOS 文档或 LifeOS 名称。

### B — LifeOS

使用相同基础模型和相同用户输入，但加载冻结的 LifeOS v0.1.1 Skill。

除 LifeOS Framework 外，模型、上下文长度、工具权限、用户输入应尽可能保持一致。

## 3. Blind 规则

Evaluator 不知道哪一份是 A、哪一份是 B。随机标记为 Response X / Response Y。

如果输出中的固定标题暴露 LifeOS，应在评分副本中中性化标题，但不能改变内容。

## 4. 场景

第一轮至少使用 20 个标准场景。更理想的是加入 10–20 个未参与框架设计的新场景，防止对测试集过拟合。

真实用户测试时，优先使用用户自己的真实问题，而不是要求用户适应预设案例。

## 5. 评分

使用现有六维 Rubric：

- Clarity
- Context Fit
- Insight
- Decision Support
- Actionability
- Autonomy

每个 Evaluator 同时回答：

1. 哪个回答更有帮助：X / Y / Tie？
2. 哪个回答更容易实际执行？
3. 哪个回答增加了不必要复杂度？
4. 是否愿意在类似问题中再次使用这种帮助方式？

## 6. Evaluator

建议至少 3 类：

- Framework-independent human evaluator；
- 真实目标用户；
- 独立 AI evaluator，仅作为补充，不代替人类。

作者本人评分只能作为调试信号，不能作为 Public Validation 证据。

## 7. Release Gate

建议 Public Validation PASS 至少满足：

- ≥ 30 个场景或真实用户案例；
- ≥ 3 名独立人类 Evaluator；
- LifeOS 在总体偏好中胜率显著高于随机水平；
- Clarity / Context Fit / Actionability 至少两项稳定优于 Baseline；
- Autonomy 不劣于 Baseline；
- Complexity Penalty 不显著增加；
- 无 P0；
- 新出现的 P1 已形成明确整改方案。

不要只依赖平均总分。若 LifeOS 只通过增加篇幅获得高分，但用户更难使用，则验证失败。

## 8. 输出

每轮生成：

```text
validation/runs/blind-ab-XX/
├── manifest.md
├── anonymized-responses/
├── scores.csv or scores.md
├── evaluator-notes.md
└── final-report.md
```

最终报告必须区分：

```text
Framework Coherence
Real-world Utility
Incremental Value over Baseline
Complexity Cost
Safety / Autonomy
```

## 9. 版本纪律

```text
v0.1.1 Frozen Baseline
        ↓
Blind A/B Run
        ↓
Findings
        ↓
v0.1.2 Changes
        ↓
Regression
        ↓
Next Blind Run
```

测试过程中不移动球门。先收集证据，再修改框架。
