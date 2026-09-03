# C1 Isolation Test 01 — Learning Strategy Router

> 日期：2026-09-04  
> 状态：**Synthetic / Author-environment Candidate Isolation**  
> 对照：A = Frozen LifeOS v0.1.1 Learning；B = v0.1.1 + C1 Learning Strategy Router  
> 注意：本轮由同一执行/评估环境生成和分析，不是盲测或外部 Human Validation，因此只能作为设计筛选证据。

## 1. Test Question

C1 是否提供了超出现有 Learning System 的稳定增量价值？

现有 v0.1.1 已包含：

```text
Question → Map → Learn → Explain → Practice → Feedback → Correct → Apply → Transfer
```

因此 C1 必须证明的不是“这些学习方法有效”，而是：

> **它能否根据不同目标、深度、期限和使用场景，选择明显不同且更合适的学习路径。**

## 2. Evaluation Scale

1–5：

- Strategy Fit
- Context Fit
- Actionability
- Verification Fit
- Transfer Value
- Autonomy
- Process Cost（5 = 成本低/简洁，1 = 成本很高）

本轮评分用于发现设计差异，不视为独立效果量。

## 3. Results

| Case | A Avg | B Avg | Main Delta | Risk |
|---|---:|---:|---|---|
| L01 30-min AI Agent orientation | 4.3 | 4.7 | B 明确限制到 L0–L1，避免过度学习 | Low |
| L02 1-month architecture review | 4.0 | 4.8 | B 将目标路由到 L3 judgment + case/review practice | Low |
| L03 ML theory without projects | 4.4 | 4.8 | 两者都能发现实践不足；C1 增量较小 | Medium |
| L04 teach tomorrow | 4.1 | 4.8 | B 对 deadline/use-context 路由明显 | Low |
| L05 exam retention | 4.3 | 4.7 | 两者都已有 recall/spacing；增量有限 | Medium |
| L06 production backend capability | 4.0 | 4.8 | B 明确 L4 evidence 与真实工程反馈 | Low |
| L07 open-ended philosophy | 4.0 | 4.7 | B 避免把所有学习都工具化/项目化 | Low |

Indicative mean: A ≈ 4.16, B ≈ 4.76。

## 4. Case Findings

### L01 — Quick Orientation

A 能提供 Map → Explain → Example 的合理路径，但没有稳定机制决定“30 分钟只需要到什么深度”。

B 的关键增量不是多给方法，而是先确定：

```text
30 min + no coding + orientation
→ L0/L1
→ overview / concept map / core terms / examples
→ explain-back check
→ STOP
```

**Finding C1-F01:** `Required Depth + Stop` 是真实增量。

### L02 — Architecture Review

A 会自然建议建立知识地图、案例、实践，但“学习到什么算够”不够明确。

B 将成功证据定义为：能比较架构方案、识别 tradeoff、提出风险与判断依据，而不是“学完 Agent 知识”。

**Finding C1-F02:** `Success Evidence` 应成为 C1 核心，而不是可选字段。

### L03 — Theory Without Practice

A 已有“输出、实践、反馈、迁移”原则，因此能识别继续看课不是主要解法。

B 的 Gap Diagnosis（Knowledge / Model / Skill / Feedback / Transfer）使纠偏更明确，但增量没有 L02/L04 那么大。

**Finding C1-F03:** Gap Diagnosis 有价值，但不应扩张成独立复杂分类系统。

### L04 — Teach Tomorrow

B 明显根据 `deadline + teach use context` 改变路径：Explain → Gap Detection → Teach-back → likely Q&A，而不是系统学习整个领域。

**Finding C1-F04:** Use Context 是强路由变量。

### L05 — Exam Retention

v0.1.1 已明确 Active Recall 和 Spaced Repetition，因此 C1 不能声称这些方法本身是新增价值。

C1 的增量仅在于：考试场景自动选择 retention/testing stack，并以 mock/error evidence 验证。

**Finding C1-F05:** C1 文档应更明确区分“Router 增量”和“已有 Method”。

### L06 — Professional Capability

B 将目标从“学习后端知识”转换成“能独立处理新颖生产问题”的 L4 证据，进而选择真实项目、设计评审、故障案例和专家反馈。

**Finding C1-F06:** Goal Level 的最大价值是决定 Evidence，不是给用户贴学习等级。

### L07 — Open Philosophy Exploration

B 能识别无截止日期、兴趣驱动、开放探索，不强迫用户定义职业化 deliverable。

但若机械要求 `What must you be able to do?`，会把非功利学习错误工具化。

**Finding C1-F07 (P1):** Learning Diagnosis 必须允许 `explore` intent；Success Evidence 可表现为理解、问题质量、连接和持续探索，而不一定是任务绩效。

## 5. What C1 Actually Adds

本轮显示，C1 的稳定增量可以压缩成四件事：

```text
1. Target Depth
2. Use Context + Deadline
3. Gap Type
4. Success Evidence
        ↓
Minimum Useful Learning Strategy
```

而不是一个庞大的“学习方法库”。

现有 Learning System 继续负责通用循环：

```text
Map → Learn → Explain → Practice → Feedback → Apply → Transfer
```

C1 更适合负责循环之前的 **Strategy Selection**。

## 6. Failure / Complexity Analysis

### C1-R01 — Method Duplication
C1 列出的 Feynman、Recall、Spacing、Deliberate Practice 等大量方法已经存在于 Learning System。

Decision: **CHANGE** — Router 应引用 Method Families，而不是重复维护方法清单。

### C1-R02 — Level Reification
L0–L5 容易被误解成用户永久“学习能力等级”。

Decision: **CHANGE** — 改名/明确为 `Target Mastery Depth`，仅描述当前主题目标，不描述人的总体能力。

### C1-R03 — Over-diagnosis
简单学习请求若强制回答 8 个变量，会增加 Process Cost。

Decision: **KEEP WITH RULE** — Minimum Diagnosis only；已有信息足够则直接路由。

### C1-R04 — Utility Bias
开放式哲学、艺术、文化学习可能被“必须能做什么”错误工具化。

Severity: **P1**。

Decision: **CHANGE** — 增加 `explore / understand / perform / judge / create / teach` 等 intent，允许探索型成功标准。

### C1-R05 — False Precision
L0–L5 看似精确但真实掌握是多维的。

Decision: **CHANGE** — 等级只用于规划目标深度，验证仍以具体行为证据为准。

## 7. Candidate Decision

```text
C1 Learning Strategy Router

Incremental Value          PASS
Strategy Fit               PASS
Actionability              PASS
Verification Fit           PASS
Autonomy                   PASS / no observed regression
Process Cost               PASS WITH GUARDRAIL
Human Capability Evidence  NOT YET PROVEN

Decision: CHANGE
```

**不是 KEEP。** 原提案方向成立，但在进入 v0.1.2 Candidate Build 前应简化。

## 8. Recommended C1 v2 Shape

```text
Learning Request
      ↓
Intent
      ↓
Target Mastery Depth
      ↓
Current Gap
      ↓
Deadline / Use Context
      ↓
Success Evidence
      ↓
Minimum Useful Strategy
      ↓
Existing Learning Loop
      ↓
Evidence → Adapt → Transfer
```

最小输出：

```text
Goal
Target Depth
Recommended Strategy
Why
First Practice Action
Success Evidence
Checkpoint
```

Quick 场景可以进一步缩短。

## 9. Next Evidence Needed

本轮不能证明：

- 用户真的学得更好；
- 一周/一个月后保持更好；
- Transfer 更强；
- 外部评审更偏好 C1；
- 长期 Process Cost 更低。

因此下一步不应直接合并进冻结 Core，而应：

```text
C1 Isolation 01
      ↓
Revise Proposal → C1 v2
      ↓
Regression on L01–L07
      ↓
Human Learning Cases
      ↓
KEEP / DOWNGRADE / REMOVE
```

## 10. Conclusion

C1 的主要价值已经从“更多学习方法”收敛为：

> **根据学习意图、目标深度、当前差距、时间/使用场景和成功证据，为当前任务选择最小有效学习策略。**

这是对 v0.1.1 Learning System 的真实结构性补充，但 Human Capability / Transfer 的效果仍需真实用户证据。
