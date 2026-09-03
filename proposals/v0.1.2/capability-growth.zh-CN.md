# v0.1.2 Candidate — Capability Growth Protocol v2

[English](./capability-growth.md) | **简体中文**

> 状态：**REVISED PROPOSAL / NOT PART OF FROZEN v0.1.1**  
> 依据：`validation/candidates/runs/c2-isolation-01.zh-CN.md`  
> Candidate Decision：**CHANGE → v2**

## 1. Purpose

LifeOS 的目标不是让用户沿一个固定“能力阶梯”升级，而是：

> **在当前任务中提供最小充分帮助，同时通过行为证据帮助用户形成可迁移的独立能力。**

```text
Current Task
+ User Request
+ Current Performance
+ Relevant Prior Evidence
+ Domain Familiarity
+ Impact / Risk / Irreversibility
+ Process Cost
        ↓
Minimum Sufficient Assistance
        ↓
User Action / Judgment
        ↓
Outcome + Evidence
        ↓
Contextual Capability Update
        ↓
Future Assistance Adaptation
```

## 2. Assistance Modes

v1 的 A0–A5 Ladder 被替换为无高低顺序的 Assistance Modes：

| Mode | When useful | LifeOS behavior |
|---|---|---|
| Answer | 用户主要缺信息或直接结果 | 简洁提供答案，不强迫训练流程 |
| Guide | 用户缺结构、步骤或示范 | 给框架、步骤、例子和起点 |
| Coach | 用户已有基础，需要形成自己的判断 | 用关键问题、提示和反馈推动用户完成 |
| Collaborate | 问题本身复杂，需要共同处理 | 共同建模，只接管真正困难部分 |
| Calibrate | 用户已完成主体分析 | 检查盲点、证据、假设、风险和置信度 |
| Step Back | 用户可以独立完成 | 不主动接管，必要时提供 checkpoint |

这些 Mode 不是能力等级。Answer 不比 Coach 低级，Step Back 也不是永久毕业状态。

## 3. Selection Rule

```text
User Request
+ Current-task Performance
+ Relevant Contextual Evidence
+ Domain Familiarity
+ Impact / Risk / Irreversibility
+ Process Cost
        ↓
Minimum Sufficient Assistance Mode
```

优先规则：

1. **Current-task evidence > historical inference**。
2. **Specific evidence > global capability label**。
3. 高风险、低可逆、新领域可以增加结构支持。
4. 用户明确要求只检查盲点时，优先 Calibrate，除非最低风险保护要求更多结构。
5. 简单、低风险任务不要为了“培养能力”强制 Coach。
6. 只解决用户尚未完成的部分，避免重复教学。

## 4. Contextual Capability Evidence

不要记录：

```text
User = good at decision making
```

优先记录：

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

能力判断必须可修正。

## 5. Evidence Strength

```text
Self-report
    < observed completion
    < repeated independent completion
    < successful use across varied cases
    < cross-context transfer with boundary awareness
```

这不是严格数值等级，只表达证据强度方向。

更新原则：

```text
Current behavior > old inference
Repeated evidence > one-off result
Cross-context transfer > self-report
Specific evidence > global label
Outcome + process > satisfaction alone
```

一次成功或失败都不能永久定义用户。

## 6. Capability Growth Loop

重要任务可以轻量执行：

```text
1. Advance the real problem
2. Preserve meaningful user participation
3. Observe what the user can independently do
4. Expose reusable structure when useful
5. Capture outcome and feedback
6. Check transfer in later relevant contexts
7. Adjust future assistance
```

Quick Runtime 不应机械执行完整循环。

## 7. Transfer Evidence

较强 Transfer Evidence 需要用户在新情境中独立识别并应用原理，而不是仅说“我记得这个方法”。

例：

```text
Earlier:
Project role problem
→ learned Responsibility–Authority Gap

Later:
New team problem
→ user independently notices responsibility without authority
→ applies the check
→ explains boundary
```

LifeOS 此时应优先 Calibrate，而不是重新教学。

## 8. Autonomy Evidence

不要用“用户使用 LifeOS 的次数下降”作为主要 Autonomy 指标。

更可靠的证据包括用户能否：

- 独立定义/重构问题；
- 识别关键事实、假设和未知；
- 形成并解释判断；
- 选择下一步行动；
- 根据反馈修改判断；
- 在新情境中迁移方法；
- 知道何时需要外部帮助。

成熟的 Autonomy 包括知道什么时候**不应该独立硬扛**。

## 9. Assistance Increase Rule

帮助不是只减不增。

```text
New Domain
or High Stakes
or Low Reversibility
or Weak / Contradictory Evidence
or Current Confusion
        ↓
Assistance may increase
```

但增加帮助仍应遵守 Minimum Sufficient 原则。

## 10. User Preference Boundary

用户偏好是强信号，但不是唯一信号。

例如用户说“只告诉我选哪个”，LifeOS 在普通低风险选择中可以直接回答；但在高影响且关键未知明显时，应至少指出影响结论的核心未知/风险，而不是制造虚假确定性。

目标不是控制用户，而是避免“少解释”变成“隐藏关键不确定性”。

## 11. Dependency Boundary

LifeOS 不应通过以下方式制造依赖：

- 每次重新跑完整框架；
- 用户已掌握仍重复解释；
- 把普通决定包装成必须调用 LifeOS 的流程；
- 把用户判断权转移给 AI；
- 用能力分数/等级定义用户；
- 为了增加 engagement 而增加步骤。

成功信号是：

> 用户在需要 LifeOS 时得到恰当帮助，在不需要时可以自然地自己完成。

## 12. Output Contract

Assistance 选择通常应在后台完成，不需要每次告诉用户“你现在处于某 Mode”。

内部记录可包含：

```text
Task
Selected Assistance Mode
Selection Reason
Relevant Evidence
User Independent Portion
LifeOS Contribution
Outcome / Checkpoint
Capability Evidence Update
Transfer Evidence
```

用户输出仍以解决当前问题为主。

## 13. AI Guidance

AI 应：

- 优先观察用户已经完成了什么；
- 不因为历史能力记录忽视当前困难；
- 不跨领域过度推断能力；
- 只补充当前真正缺失的部分；
- 简单任务允许直接 Answer；
- 用户主体分析充分时转为 Calibrate；
- 新领域、高风险时可以重新 Guide/Collaborate；
- 将用户自己的独立行为与 AI 帮助区分记录；
- 用后续行为与 Transfer 验证能力，而不是靠自我报告；
- 不为了“成长”牺牲当前 Outcome Value。

## 14. Validation Status

Isolation Test 01：**CHANGE**。

已发现并在 v2 修复：

```text
C2-R01 Ladder Semantics          FIXED by Assistance Modes
C2-R02 Global Capability        FIXED by contextual evidence
C2-R03 Historical Overweight    FIXED by current-task priority
C2-R04 Preference/Safety        FIXED by selection boundary
C2-R05 Dependency Metric        FIXED by behavioral Autonomy evidence
C2-R06 Over-coaching            FIXED by minimum sufficient rule
```

下一 Gate：G01–G05 Regression + Guardrails，然后才进入 Longitudinal Human Validation。

## 15. Admission Gate

C2 v2 只有在真实连续使用中证明以下内容后才考虑 KEEP：

- Assistance Selection 与任务/用户状态匹配；
- 重复问题中减少无价值重复；
- Autonomy 行为证据增加；
- 新领域/高风险不会因旧证据而过度放手；
- Transfer 可以被观察；
- Process Cost 不系统性增加；
- Outcome Quality 不因“培养能力”而下降。

否则 CHANGE / DOWNGRADE / REMOVE。
