# Evaluator Guide — LifeOS v0.1.2 Human Validation

[English](./evaluator-guide.md) | **简体中文**

## 原则

Evaluator 的职责是记录 Evidence，不是帮助 Candidate 通过 Gate。

优先记录：用户真实行为、实际接受的行动、后续结果、独立完成部分、反证、负面效果。

不要把“用户喜欢回答”直接等同于 Outcome、Autonomy 或 Transfer。

## Candidate 观察

**C1**：策略是否与 Intent / Target Depth / Gap / Use Context 匹配？Success Evidence 是否能实际验证？

**C2**：帮助是否与当前任务表现匹配？是否重复讲用户已会的内容？新领域/高风险时是否错误 Step Back？

**C3**：是否改善关键判断？是否识别重要未知/反证/可逆性？是否导致过度分析？

## Evidence 边界

```text
Target Evidence ≠ Capability Evidence
Transfer Lesson ≠ Transfer Evidence
Judgment Evidence ≠ Outcome Evidence
```

Transfer Evidence 必须来自后续独立行为。

## 评分

评分必须基于本 Case，不形成全局用户能力等级。无法判断时记录 N/A / unknown，不要猜测。

Process Cost 5 表示低无效负担/投入值得；1 表示明显繁琐或妨碍行动。

## P0 / P1

发现 P0 立即标记并停止相关 Candidate 的继续使用，进入分析。P1 必须进入 remediation，不得在最终报告中被平均分掩盖。

## Anti-bias

- 不因开发者期待而提高分数；
- 不因一次成功推断长期能力；
- 不因一次失败否定整个 Candidate；
- 不把缺少 Transfer Opportunity 当作 Transfer Failure；
- 不因为 Candidate 已投入大量设计成本而倾向 KEEP；
- 对 Quick Control 特别关注 framework burden。

## 最终裁决

分别对 C1 / C2 / C3 / Full Runtime 给出：KEEP、CHANGE、DOWNGRADE、REMOVE、UNCERTAIN/MORE EVIDENCE，并附支持与反对 Evidence。
