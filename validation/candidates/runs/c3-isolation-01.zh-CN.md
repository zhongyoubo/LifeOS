# C3 Isolation Test 01 — Cognitive Augmentation

> 日期：2026-09-04  
> 状态：**Synthetic / Author-environment Candidate Isolation**  
> 对照：A = Frozen LifeOS v0.1.1；B = v0.1.1 + C3 Cognitive Augmentation  
> 范围：Cognitive Calibration + Mental Model Router + Metacognitive Transfer  
> 限制：本轮用于设计筛选，不构成真实用户认知能力提升证据。

## 1. Test Question

C3 是否提供超出现有 Thinking / Decision 的稳定增量价值，同时避免把 LifeOS 变成“过度分析系统”？

重点验证：

```text
Calibration      是否改善事实/解释/假设/未知的分离？
Model Router     是否真正改变理解或行动，而不是模型炫技？
Transfer         是否能提炼可迁移结构，而不是把一次经验普遍化？
Process Cost     简单问题是否能快速停止？
```

## 2. Evaluation Dimensions

- Clarity
- Insight
- Decision Support
- Calibration Quality
- Model Relevance
- Actionability
- Transfer Value
- Process Cost（5 = 低负担）

## 3. C01 — Project Failure → Permanent Self Attribution

输入：
> “这个项目失败了，我觉得这证明我根本不适合做负责人。”

B 将：

```text
Fact: project failed
Interpretation: failure reflects leadership suitability
Assumption: this outcome is mainly caused by stable personal inability
Unknowns: context, authority, resources, decisions, execution, external factors
Alternative explanations: structural / situational / skill-specific / mixed
```

Mental Model 名称不是必要输出；Evidence Gate / Attribution 逻辑有价值。

**Finding C3-F01:** Calibration 对“事件 → 永久身份结论”的跳跃有真实结构性增量。

## 4. C02 — Sunk Cost

输入：
> “项目已经投入一年和很多钱，现在停掉太可惜，所以我倾向继续。”

B 不仅说“这是沉没成本”，而重构决策：

```text
Past cost is unrecoverable
→ compare future options from today
→ expected future value / opportunity cost / exit cost
→ identify evidence that justifies continued investment
```

**Finding C3-F02:** Mental Model 只有在改变 forward-looking decision structure 时才有增量；仅命名模型无价值。

## 5. C03 — Two Good Job Options

输入：
> “两个工作机会都很好，我一直想找到正确答案，但信息不完整。”

B 使用：关键未知 + reversibility + option value，而不是追求消除全部不确定性。

**Finding C3-F03:** Calibration 的价值不是提高确定性，而是判断“当前需要多少确定性才能行动”。

## 6. C04 — More People, Slower Delivery

输入：
> “团队不断加人，但交付越来越慢。是不是应该继续招更多人？”

B 使用 systems/bottleneck/feedback 逻辑，先检查 coordination cost、dependency、WIP、onboarding、decision latency 等替代解释。

风险：若一次性列十几个系统模型，会降低 Actionability。

**Finding C3-F04:** Router 必须选择 `Minimum Useful Lens`，通常先测试 1 个最可能改变行动的机制。

## 7. C05 — Leader Disagrees → “Doesn't Understand Tech”

输入：
> “领导反对我的技术方案，我觉得他根本不懂技术。”

B 分离：

```text
Fact: proposal rejected / challenged
Interpretation: leader lacks technical understanding
Alternative hypotheses:
- different business/risk constraints
- missing context
- communication failure
- actual technical disagreement
- authority/incentive difference
```

**Finding C3-F05:** Alternative Hypothesis 生成有增量，但不能假装所有解释等概率；应寻找最有区分力的 Evidence。

## 8. C06 — High-confidence Consequential Commitment

输入：
> “我有 90% 把握这个选择会成功，身边人也支持，我准备一次性投入大量资源。”

B 不直接接受 90%：

```text
What supports 90%?
What is the strongest disconfirming evidence?
What happens in the 10%?
Can commitment be staged?
What evidence would change the decision?
```

**Finding C3-F06:** 对高影响、低可逆选择，`downside × reversibility × disconfirming evidence` 比要求更多正向理由更重要。

## 9. C07 — Lunch A or B

输入：
> “今天午饭吃 A 还是 B？两个都可以。”

完整 Calibration Stack / Mental Model 输出会明显恶化体验。

正确行为：根据偏好快速选，或给一个简单 tie-breaker，然后停止。

**Finding C3-F07 (P1):** C3 必须有明确 `Calibration Trigger + Stop Rule`；不能因为协议存在就默认运行。

## 10. C08 — Repeated Calibration Case

输入设定：用户此前已经学会主动区分 Fact / Interpretation / Assumption，本轮自己先完成分离，只要求检查。

B 应跳过教学，直接 Calibrate 最脆弱假设/遗漏反证。

**Finding C3-F08:** C3 与 C2 有交互，但 C3 自身不应维护 Assistance Ladder；帮助强度交给 C2 Assistance Modes。

## 11. Component-level Findings

### C3-A Cognitive Calibration

**Incremental value: STRONGEST**。

最稳定的增量是：

```text
Judgment
→ Fact / Interpretation / Assumption / Unknown separation
→ Critical uncertainty
→ Alternative explanation / counterevidence
→ Reversibility
→ Updated judgment
→ What would change it?
```

但完整 Evidence Stack 不应成为每次必填表。

### C3-B Mental Model Router

**Incremental value: CONDITIONAL**。

有价值的是选择合适 reasoning lens，不是模型库本身。

Mental Model Schema 很完整，但如果作为 Runtime 强制结构会过重。

建议把：

```text
Mental Model Router
```

收敛成：

```text
Reasoning Lens Selection
```

模型名可以显式，也可以完全隐藏。

### C3-C Metacognitive Transfer

**Incremental value: PROMISING BUT UNPROVEN**。

单次回答可以提炼 Transfer Lesson，但“用户是否真正迁移”只能由未来独立行为证明。

因此：

```text
Transfer Lesson ≠ Transfer Evidence
```

这是关键边界。

## 12. Problems Found

### C3-R01 — Protocol Over-triggering
完整 Calibration 对简单、低风险、可逆问题成本过高。

Severity: **P1**。

Decision: **CHANGE** — 增加 Trigger：Impact / Uncertainty / Risk / Irreversibility / recurring reasoning failure。

### C3-R02 — Evidence Stack as Form
Facts / Interpretation / Assumptions / Values / Unknowns / Prediction / Confidence 全部显式输出会模板化。

Decision: **CHANGE** — 只暴露会改变判断的字段。

### C3-R03 — Model Catalogue Gravity
Mental Model Protocol 容易自然演化成模型大全。

Decision: **CHANGE** — Runtime 以 Reasoning Lens 为中心；Library 只是可选知识资产。

### C3-R04 — Model Naming Bias
一旦命名“Sunk Cost”“Confirmation Bias”，系统容易为了匹配模型而解释问题。

Decision: **CHANGE** — 先验证机制，再决定是否命名。

### C3-R05 — Alternative Hypothesis Explosion
列大量可能解释并不等于更好的思考。

Decision: **CHANGE** — 优先 1–3 个 plausible alternatives + discriminating evidence。

### C3-R06 — Transfer Claim Inflation
AI 总结一个“可迁移原则”不代表用户获得了能力。

Decision: **CHANGE** — 分离 Transfer Lesson 与未来 Transfer Evidence；后者由 C2 evidence protocol 记录。

### C3-R07 — Overlap with C2
“用户已掌握时减少解释”属于 Assistance Selection，不应在 C3 再实现一套机制。

Decision: **CHANGE** — C3 提供认知操作，C2 决定帮助强度。

### C3-R08 — Calibration Paralysis
不断寻找反证/未知可能让用户无法行动。

Severity: **P1**。

Decision: **CHANGE** — 增加 Action Sufficiency Rule：当剩余不确定性不足以改变当前可逆行动时停止分析。

## 13. Proposed C3 v2 Shape

C3 不再作为一个大而完整的“认知增强层”，而收敛成两个协议 + 一个学习接口：

```text
A. Judgment Calibration Protocol
   Trigger only when useful
   ↓
   Known / Inferred / Assumed
   Critical Unknown
   Plausible Alternative
   Disconfirming Evidence
   Reversibility
   Updated Judgment
   Action Sufficiency

B. Reasoning Lens Router
   What reasoning is missing?
   ↓
   Select minimum useful lens
   ↓
   Apply mechanism
   ↓
   Did it change understanding/action?
      No → discard
      Yes → optionally explain/name

C. Transfer Interface
   Extract candidate lesson
   ↓
   define boundary / trigger
   ↓
   hand off to C2 for future Transfer Evidence
```

## 14. Trigger Rule

C3 should activate more strongly when one or more are material:

```text
Impact
Uncertainty
Risk
Irreversibility
Strong confidence with weak evidence
Repeated reasoning failure
Identity-level conclusion from limited evidence
```

Low-risk + reversible + easy-feedback situations should usually act first and learn from outcome.

## 15. Action Sufficiency Rule

Move to action when：

- the material judgment is clear enough for the next step;
- remaining uncertainty is unlikely to change the current action;
- downside is bounded or reversible;
- action can produce useful evidence faster than more analysis.

这与 Kernel Stop Rule 一致；C3 不应创建另一个无限分析循环。

## 16. Indicative Decision

```text
Cognitive Calibration        KEEP DIRECTION / CHANGE PROTOCOL
Mental Model Router          CHANGE → Reasoning Lens Router
Metacognitive Transfer       CHANGE → Transfer Interface

Overall C3 Decision          CHANGE
P1                           2 found, both protocol-level fixable
Human Cognitive Evidence     NOT PROVEN
```

## 17. Next Gate

```text
C3 Isolation 01
      ↓
C3 v2
Judgment Calibration
+ Reasoning Lens Router
+ Transfer Interface
      ↓
Regression C01–C08 + Guardrails
      ↓
C1/C2/C3 Interaction Validation
      ↓
Human Validation
```

## 18. Conclusion

C3 的核心价值不是给用户更多 Mental Models，而是：

> **在真正需要时，提高判断与证据的校准质量；在推理缺口存在时选择最小有效 reasoning lens；在事后提炼可迁移候选经验，并等待未来行为证明它真的迁移。**

这使 C3 从“认知增强功能集合”收敛为更轻、更可验证的判断协议。
