# v0.1.2 Candidate — Cognitive Augmentation v2 / 认知增强协议

[English](./cognitive-augmentation.md) | **简体中文**

> 状态：**REVISED PROPOSAL / NOT PART OF FROZEN v0.1.1**  
> 依据：`validation/candidates/runs/c3-isolation-01.zh-CN.md`  
> Candidate Decision：**CHANGE → v2**

## 1. Purpose

C3 v2 不创建新的“认知增强层”，而提供两个可复用协议和一个学习接口：

```text
A. Judgment Calibration Protocol
B. Reasoning Lens Router
C. Transfer Interface
```

目标：只在真正需要时提高判断质量，不让 LifeOS 变成过度分析系统。

## 2. Trigger Gate

C3 不默认运行完整协议。以下因素达到实质程度时才增强校准：

```text
Impact
Uncertainty
Risk
Irreversibility
Strong confidence with weak evidence
Repeated reasoning failure
Identity-level conclusion from limited evidence
```

低风险 + 可逆 + 易获得反馈时，优先行动并从结果学习。

## 3. Judgment Calibration Protocol

核心不是填 Evidence Stack，而是找出**会改变判断的证据结构**。

```text
Current Judgment
→ What is known?
→ What is inferred / assumed?
→ Critical Unknown
→ 1–3 Plausible Alternatives
→ Disconfirming Evidence
→ Reversibility / Downside
→ Updated Judgment
→ What would change it?
→ Action Sufficiency
```

### Minimum Exposure Rule

只显式输出影响结论或行动的字段。不要机械展示 Facts / Interpretation / Assumptions / Values / Unknowns / Prediction / Confidence 全套表格。

### Confidence

默认使用定性描述；没有量化依据时不要制造 73%、91% 之类假精确度。

置信度可以随证据改变。改变判断是校准成功，不是失败。

## 4. Alternative Explanations

Alternative Hypothesis 的目标是打破单一解释锁定，而不是列举所有可能性。

默认：

```text
Current explanation
+ 1–3 plausible alternatives
+ evidence that best distinguishes them
```

如果替代解释不会改变行动，可以停止扩展。

## 5. Disconfirming Evidence

高置信度或高影响判断优先问：

- 什么证据最可能推翻当前结论？
- 如果结论错了，最可能错在哪里？
- 失败场景的代价是什么？
- 能否分阶段承诺，而不是一次性押注？

寻找反证不是为了永久怀疑，而是为了校准承诺强度。

## 6. Reasoning Lens Router

v1 的 Mental Model Router 改为 **Reasoning Lens Router**。

```text
Problem Diagnosis
→ What reasoning is missing?
→ Candidate Lens
→ Mechanism / Boundary Check
→ Select Minimum Useful Lens
→ Apply to actual problem
→ Did it materially change understanding/action?
   ├─ No  → discard
   └─ Yes → keep; optionally explain/name
```

Lens 可以来自 Mental Model、系统原则、决策方法或领域机制。Runtime 不要求先给它一个模型名称。

示例：

| Signal | Useful lens |
|---|---|
| 因过去投入而继续 | Compare future options from today; opportunity cost |
| 加人后反而更慢 | Bottleneck / coordination / feedback |
| 不确定选择 | Reversibility / option value |
| 单一归因 | Alternative hypotheses / evidence |
| 责任与推动能力不匹配 | Responsibility–Authority Gap |
| 一次失败 → 永久自我判断 | Evidence / attribution boundary |

## 7. Model Naming Rule

先验证机制是否适用，再决定是否命名。

显式介绍模型仅当：
- 名称能帮助用户未来复用；
- 用户希望学习方法；
- 模型边界值得说明；
- 命名不会增加不必要 Process Cost。

否则直接使用逻辑。

## 8. Transfer Interface

C3 只能生成 **Candidate Transfer Lesson**，不能宣称用户已经形成 Transfer Capability。

```text
Outcome / Reflection
→ Candidate Lesson
→ Trigger
→ Boundary / Counterexample
→ Next-time Signal
→ hand off to C2 Capability Evidence
→ future independent behavior
→ Transfer Evidence or Counterevidence
```

严格区分：

```text
Transfer Lesson ≠ Transfer Evidence
```

未来是否真的迁移，由 C2 Contextual Capability Evidence 验证。

## 9. Action Sufficiency Rule

停止分析并进入行动，当：

- 当前判断已足够支持下一步；
- 剩余未知不太可能改变当前行动；
- downside 可接受或行动可逆；
- 行动产生证据的速度高于继续分析；
- 没有未处理的重大不可逆风险。

```text
More Analysis Value < Feedback Value from Action
→ ACT
```

C3 必须服从 Kernel Stop Rule，不创建第二个无限推理循环。

## 10. Bias Handling

不要先给用户贴 bias 标签。

```text
Observed reasoning
→ concrete evidence gap
→ plausible alternative
→ consequence
→ optionally name bias if useful for transfer
```

价值偏好、风险偏好和不同目标不自动等于认知偏差。

## 11. Boundary with C2

C3 决定**需要什么认知操作**；C2 决定**LifeOS 应帮助到什么程度**。

```text
C3: calibration / reasoning lens / transfer lesson
C2: Answer / Guide / Coach / Collaborate / Calibrate / Step Back
```

C3 不维护自己的 Assistance Ladder，也不根据“用户等级”改变解释量。

## 12. Output Contract

Standard / Deep 按需：

```text
Current Judgment
Critical Known / Assumed distinction
Critical Unknown
Plausible Alternative
Disconfirming Evidence
Relevant Reasoning Lens (optional)
Reversibility / Downside
Updated Judgment
Next Action
What Would Change the Judgment
Checkpoint
Candidate Transfer Lesson (after evidence)
```

Quick 只保留影响下一步的最小内容。

## 13. AI Guidance

AI 应：
- 先判断是否需要 C3；
- 只拆分会影响判断的事实/推断/假设；
- 优先关键未知，不罗列全部未知；
- 生成少量高价值替代解释；
- 高置信度时主动寻找反证；
- 高风险低可逆时关注 downside 与 staged commitment；
- 使用最小有效 reasoning lens；
- 先应用机制，再考虑模型名称；
- 剩余不确定性不足以改变行动时停止分析；
- 不把 Transfer Lesson 当作能力证据；
- 将未来 Transfer Evidence 交给 C2；
- 不把 AI 推断包装成事实。

## 14. Validation Status

Isolation 01：**CHANGE**。

```text
C3-R01 Over-triggering            FIXED by Trigger Gate
C3-R02 Evidence Stack as Form     FIXED by Minimum Exposure
C3-R03 Model Catalogue Gravity    FIXED by Reasoning Lens
C3-R04 Model Naming Bias          FIXED by mechanism-first rule
C3-R05 Hypothesis Explosion       FIXED by 1–3 + discriminating evidence
C3-R06 Transfer Inflation         FIXED by Transfer Interface
C3-R07 C2 Overlap                 FIXED by boundary
C3-R08 Calibration Paralysis      FIXED by Action Sufficiency
```

下一 Gate：C01–C08 Regression + Guardrails。

## 15. Admission Gate

只有证明以下内容才考虑 KEEP：
- Calibration Quality 稳定提升；
- Insight / Decision Support 有增量；
- Actionability 不下降；
- 简单场景 Process Cost 不恶化；
- 不系统性产生 analysis paralysis；
- Reasoning Lens 真正改变理解/行动；
- 真实用户出现后续 Calibration / Transfer Evidence；
- 相对现有 Thinking / Decision 有独立增量价值。

否则 CHANGE / DOWNGRADE / REMOVE。
