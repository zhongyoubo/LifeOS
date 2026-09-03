# C2 Isolation Test 01 — Capability Growth + Assistance Ladder

> 日期：2026-09-04  
> 状态：**Synthetic / Author-environment Candidate Isolation**  
> 对照：A = Frozen LifeOS v0.1.1；B = v0.1.1 + C2 Capability Growth / Assistance Ladder  
> 限制：本轮由同一执行/评估环境构造连续场景并分析，只能作为设计筛选证据，不是 Human Capability 的真实证明。

## 1. Test Question

C2 的核心主张是：

> LifeOS 应根据用户在特定能力、特定情境中的行为证据动态调整帮助，而不是每次都重新提供完整解决方案。

需要验证四件事：

```text
1. 用户已有能力时，是否减少重复帮助？
2. 用户能力证据不足时，是否提供足够结构？
3. 新领域 / 高风险 / 高不确定性时，帮助是否可以重新增加？
4. 是否避免把 Assistance Level 变成用户永久能力标签？
```

## 2. Test Design

使用同一虚拟用户的连续职业决策 + 跨领域场景：

```text
G01 First Career Decision
→ G02 Similar Decision with Learned Structure
→ G03 User-led Decision / Blind-spot Check
→ G04 New High-risk Domain
→ G05 Transfer to Organization Problem
```

A 每轮使用冻结 v0.1.1 正常解决问题。

B 除 v0.1.1 外，根据之前轮次中**可观察的用户行为证据**决定本轮 Assistance Mode。

## 3. Evaluation Dimensions

1–5：

- Context Fit
- Actionability
- Autonomy
- Assistance Appropriateness
- Transfer Recognition
- Process Cost（5 = 成本低）
- Outcome Protection（降低帮助后是否仍保护关键决策质量）

## 4. G01 — First Career Decision

### Situation
用户第一次系统比较两个工作机会，只说薪资、职位和公司规模，不知道如何组织决策。

### A — v0.1.1
合理加载 Goal / Context / Decision，帮助澄清目标、约束、选项和下一步。

### B — +C2
没有历史能力证据，因此提供较强结构支持，但不替用户决定：

```text
Goal / Constraints
→ Decision Criteria
→ Key Unknowns
→ Reversibility
→ User weights/tradeoffs
→ Next evidence action
```

Suggested Assistance：**Guide / Collaborate**。

### Finding
C2 增量较小，因为第一次运行 v0.1.1 本身已经能给出好结构。

**C2-F01:** C2 的价值不应主要体现在首次回答，而应体现在连续使用中的 Assistance Adaptation。

## 5. G02 — Similar Career Decision

### Situation
数周后用户遇到另一个机会，并主动说：

> “我先按上次的方法列了目标、不能接受的条件、5 个 criteria，还列了两个我不知道的信息。现在主要卡在成长空间和稳定性的取舍。”

### A
若没有显式长期能力机制，容易重新输出完整 Decision Framework。

### B
识别行为证据：用户已经独立完成 framing、criteria、unknowns。

因此跳过已掌握部分，只处理当前 tradeoff：

```text
Evidence: framing/criteria/unknowns independently completed
→ Assistance ↓
→ Coach / Collaborate only on unresolved tradeoff
```

### Finding
明显减少重复结构和 Process Cost，同时保留决策质量。

**C2-F02:** Assistance Adjustment 必须基于“用户本轮已经做了什么”，而不是仅基于历史标签。

## 6. G03 — User-led Analysis

### Situation
第三次用户给出完整分析、反方观点、关键未知、暂定选择，并说：

> “我基本决定选 B，你只帮我看看有没有明显盲点。”

### A
优秀通用回答也可能遵守请求，但 LifeOS 没有显式机制保证不重新接管分析。

### B
选择 **Calibrate**：

```text
Do not rebuild decision
→ inspect unsupported assumptions
→ inspect missing downside
→ inspect confidence / disconfirming evidence
→ return only material blind spots
```

### Finding
Autonomy 与 Process Cost 明显改善。

**C2-F03:** `User Request` 本身是 Assistance Selection 的强信号；不能只看能力证据。

## 7. G04 — New High-risk Domain

### Situation
同一用户第一次准备处理一个高风险、不可逆、自己没有经验的法律/财务型重大承诺，并说：

> “我之前已经能自己做职业决策了，所以这次也只帮我看盲点。”

### B Expected
不能把“职业决策能力”直接迁移成“所有重大决策都只需 Calibrate”。

应识别：

```text
Different Domain
+ High Stakes
+ Low Domain Evidence
+ Low Reversibility
→ Assistance may increase
→ structure unknowns / expert boundary / downside / checkpoint
```

### Finding
原 Assistance Ladder 的“越来越低”叙事有误导风险。

**C2-F04 (P1):** Assistance 不是用户的全局等级，也不是单向下降曲线；必须是 `task × domain × risk × evidence` 的动态选择。

## 8. G05 — Transfer Evidence

### Situation
用户后来处理团队问题时主动说：

> “我发现这可能和之前讨论的责任-权限差距类似。我要求团队负责人交付，但预算、人手和跨部门协调权都不在他手里，所以我先检查结构问题，而不是判断他执行力差。”

### B
这是较强 Transfer Evidence：用户在新情境中独立识别并应用结构。

LifeOS 不应重新教学 Responsibility–Authority Gap，只需：

```text
Recognize transfer
→ verify boundary / counterevidence
→ calibrate application
→ record evidence with context
```

### Finding
**C2-F05:** Capability Evidence 最有价值的不是“用户说我学会了”，而是跨情境独立应用。

## 9. Core Findings

C2 的真实增量可以收敛为：

```text
Current User Request
+ Current-task Performance
+ Relevant Prior Evidence
+ Domain Familiarity
+ Stakes / Risk / Reversibility
        ↓
Minimum Sufficient Assistance
        ↓
Observe User Performance
        ↓
Update Contextual Evidence
```

而不是：

```text
User starts at A1
→ becomes A2
→ becomes A3
→ ...
→ graduates at A5
```

后者应明确禁止。

## 10. Problems Found

### C2-R01 — Ladder Semantics
`A0 Answer → ... → A5 Independent` 看起来像从低到高的成长等级，但 Answer 并不一定比 Coach “低级”，Independent 也不适用于所有情境。

Severity: **P1**。

Decision: **CHANGE** — 将 Ladder 重构为 Assistance Modes，不使用隐含晋级语义。

### C2-R02 — Global Capability Inference
跨领域迁移 Assistance 可能产生危险的过度自信。

Severity: **P1**。

Decision: **CHANGE** — Evidence 必须带 capability + context/domain + task type。

### C2-R03 — Historical Evidence Over Current Performance
如果历史记录说用户很强，但本轮明显困惑，系统不能因为历史标签继续低介入。

Decision: **CHANGE** — Current-task evidence 优先于旧能力推断。

### C2-R04 — User Preference vs Safety/Quality
用户要求“只告诉我答案”或“别解释”，有时应该尊重；但高影响、低可逆且关键未知明显时，仍需最低限度保护。

Decision: **CHANGE** — Assistance Selection 需同时考虑 user request 与 stakes/risk。

### C2-R05 — Dependency Metric Ambiguity
“用户越来越少使用 LifeOS”不等于 Autonomy 提升；用户也可能只是放弃工具。

Decision: **CHANGE** — Autonomy Evidence 应看独立 framing/reasoning/action/transfer，而不是使用频率下降。

### C2-R06 — Over-coaching
为了培养能力而总是反问用户，会让简单任务变烦。

Decision: **CHANGE** — Capability Growth 不能凌驾于 Outcome Value 和 Process Cost；有时直接 Answer 是最优帮助。

## 11. Proposed C2 v2 Model

将 Assistance Ladder 改为 **Assistance Modes**：

```text
Answer       用户主要需要信息/直接结果
Guide        用户需要结构、步骤或示范
Coach        用户已有基础，适合通过提示/反馈形成自己的判断
Collaborate  双方共同处理真正困难的部分
Calibrate    用户已完成主体，只检查盲点/证据/置信度
Step Back    用户可以独立完成，LifeOS 不主动接管
```

这些 Mode 没有高低顺序。

Selection：

```text
User Request
+ Current Performance
+ Relevant Evidence
+ Domain Familiarity
+ Impact / Risk / Irreversibility
+ Process Cost
        ↓
Minimum Sufficient Assistance Mode
```

## 12. Contextual Capability Evidence

建议记录：

```text
Capability
Task Type
Domain / Context
Observed Behavior
Assistance Provided
Independent Portion
Outcome / Feedback
Transfer Evidence
Counterevidence
Confidence
Last Observed
```

更新规则：

```text
Current behavior > old inference
Repeated evidence > one-off result
Cross-context transfer > self-report
Specific evidence > global label
Outcome + process > satisfaction alone
```

## 13. Indicative Comparison

| Case | A | B | Main C2 Value |
|---|---:|---:|---|
| G01 | strong | strong | little first-run delta |
| G02 | strong | stronger | avoids repeated framework |
| G03 | strong | stronger | protects user ownership |
| G04 | variable | stronger | prevents unsafe over-transfer |
| G05 | variable | stronger | recognizes actual transfer |

本轮不计算总体效果量，因为 C2 是 longitudinal adaptation mechanism，单轮平均分会掩盖其主要价值。

## 14. Candidate Decision

```text
Incremental Value          PASS in longitudinal use
Autonomy Mechanism         PROMISING
Transfer Recognition       PASS conceptually
Process Cost               IMPROVES when correctly selected
Safety / Over-transfer     P1 in current Ladder semantics
Human Capability Evidence  NOT PROVEN

Decision: CHANGE
```

原 Capability Growth 方向成立，但 Assistance Ladder 表述和证据模型必须修改后再测试。

## 15. Next Gate

```text
C2 Isolation 01
      ↓
C2 v2 — Assistance Modes + Contextual Evidence
      ↓
Regression G01–G05 + guardrails
      ↓
Longitudinal Human Validation
      ↓
KEEP / DOWNGRADE / REMOVE
```

Human Validation 必须观察真实连续行为，不能只问用户“你觉得自己更独立了吗”。

## 16. Conclusion

C2 最有价值的不是建立一个从 A0 到 A5 的成长阶梯，而是建立：

> **基于当前任务表现、相关历史证据、领域熟悉度和风险，动态选择最小充分帮助，并通过后续独立行为与迁移证据判断用户是否真的形成能力。**

这更符合 LifeOS 的最终目标：增强 Autonomy，而不是制造一个新的能力等级体系。
