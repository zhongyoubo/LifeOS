# LifeOS Human Real-world Validation

> 目标：验证 LifeOS 不只是让 AI 回答看起来更好，而是能否帮助真实用户更清楚地判断、更容易行动、形成可迁移的经验，并且不增加不必要的依赖。

## 1. 核心研究问题

Human Validation 回答四个问题：

1. **Understanding** — 用户是否更清楚真正的问题？
2. **Decision / Action** — 用户是否更容易形成决定或可执行下一步？
3. **Follow-through / Outcome** — 用户是否真的行动，并产生有意义的结果？
4. **Autonomy / Learning** — 用户是否变得更能自己处理类似问题，而不是更依赖 LifeOS？

Pilot-1 主要测试 `LifeOS vs Baseline answer quality`；Human Validation 测试的是：

```text
Real Problem
    ↓
LifeOS Session
    ↓
Decision / Next Action
    ↓
Real-world Action
    ↓
7-day Follow-up
    ↓
Outcome + Learning + Autonomy
```

## 2. 参与者

第一轮建议：

- 5–10 位真实用户；
- 每人 1–2 个当前真实存在的问题；
- 优先覆盖职业、项目、管理、沟通、学习、个人方向、执行与复盘等不同场景；
- 不要求用户了解 LifeOS；
- 框架作者不能代替真实用户填写结果。

不要收集完成研究不需要的敏感身份信息。

## 3. Case Admission Gate

一个问题只有同时满足以下条件才进入 Human Validation：

- 是用户当前真实面对的问题，而不是虚构题；
- 用户希望在近期获得更清晰的判断或行动；
- 存在一个可观察的下一步或 checkpoint；
- 7–14 天内至少能观察到部分 follow-through；
- 不属于需要专业医疗、法律、紧急安全判断来替代专业人员的高风险场景。

## 4. 测试流程

### T0 — Before Session

记录：

- 问题原始描述；
- 当前 Clarity（1–5）；
- 当前 Decision Confidence（1–5）；
- 当前是否知道下一步；
- 当前最大未知；
- 用户希望得到什么帮助。

### T1 — LifeOS Session

使用冻结版本 LifeOS。不要为了某个用户临时修改框架。

必须保留：

- 原始用户输入；
- LifeOS 输出；
- 用户最终选择/决定；
- Next Action；
- Checkpoint / revisit condition。

### T2 — Immediate Post-session

用户自己评分：

- Clarity 1–5
- Context Fit 1–5
- Decision Confidence 1–5
- Actionability 1–5
- Autonomy 1–5
- Process Cost 1–5（低更好）
- Would Use Again 1–5

并回答：

- 这次对话最有价值的部分是什么？
- 哪些结构没有必要？
- 是否出现新的重要认识？
- 你现在准备做的第一步是什么？

### T3 — 7-day Follow-up

核心不是“你喜欢答案吗”，而是：

- 是否执行 Next Action？`yes / partial / no`
- 如果没有，为什么？
- 原问题是否发生变化？
- 结果是否比 7 天前更清楚？
- 哪个建议实际有效？
- 哪个建议实际无效？
- 是否需要再次依赖 LifeOS 才能继续？
- 用户是否能用自己的话解释学到的判断方法？

### T4 — Optional 30-day Follow-up

适用于职业、管理、长期项目、关系和学习等慢变量问题。

记录：

- Outcome Direction：`improved / unchanged / worse / unclear`
- Decision Regret：1–5
- Learning Transfer：是否在另一个问题中自行使用了相同原则？
- Dependency：是否觉得没有 LifeOS 就无法继续？

## 5. Primary Metrics

| Metric | Meaning | Direction |
|---|---|---|
| Clarity Delta | T1 后问题是否更清楚 | higher better |
| Decision Confidence Delta | 是否更能形成判断 | higher better |
| Action Initiation | 是否真正开始 | higher better |
| 7-day Follow-through | 是否执行承诺动作 | higher better |
| Outcome Direction | 现实结果是否改善 | improved better |
| Learning Transfer | 是否形成可迁移能力 | higher better |
| Autonomy | 是否保留用户判断权 | higher better |
| Process Cost | 框架是否太重 | lower better |
| Dependency Risk | 是否制造不必要依赖 | lower better |

## 6. Success Gate — Human Validation Round 1

建议只有同时满足以下条件才进入 `Validated Foundation` 候选：

- ≥5 位真实用户；
- ≥10 个真实问题；
- ≥80% Case 形成明确 Next Action 或明确“不行动/继续探索”的理由；
- ≥70% Case 在 7 天内出现 `yes` 或 `partial` follow-through；
- 平均 Clarity Delta > 0；
- 平均 Decision Confidence Delta ≥ 0；
- Autonomy 不恶化；
- Process Cost 没有系统性高负担；
- 没有 P0；
- 所有新 P1 都有明确 remediation plan。

这些阈值是第一轮工程门槛，不是科学定律。后续根据样本扩大调整。

## 7. Failure Classification

每个 Case 在结束时归类：

- `KEEP` — 明确创造增量价值；
- `CHANGE` — 有价值但成本/表达/流程需要调整；
- `REMOVE` — 结构没有证明价值；
- `ADD` — 暴露稳定能力缺口；
- `UNCERTAIN` — 证据不足。

同时标记严重度：`P0 / P1 / P2 / P3`。

## 8. Anti-Gaming Rules

- 不因为用户满意就自动算成功；
- 不因为输出更长就算更深入；
- 不把“用户执行了”自动等同于“建议正确”；
- 不把短期结果自动升级成永久 Self Model 标签；
- 不隐藏失败 Case；
- 不在测试中途修改冻结框架然后继续把结果算在同一批次；
- 框架作者的自评只能作为补充证据。

## 9. Evidence Standard

LifeOS 最终希望证明的不是：

> LifeOS 能生成一套漂亮的方法论。

而是：

> 在真实问题中，LifeOS 能以可接受的认知成本，提高理解、判断、行动和学习质量，同时增强而不是削弱人的自主性。
