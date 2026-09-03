# LifeOS Capability Map / 能力地图

[English](./capability-map.md) | **简体中文**

> 本文定义 LifeOS 的长期能力方向。它是愿景与架构之间的桥梁，不改变冻结的 v0.1.1 Runtime 语义。

## 1. 双能力主线

LifeOS 同时优化两类能力：

```text
LifeOS
│
├── System Capability
│   LifeOS 能否更好地理解、诊断、推理、支持行动和学习？
│
└── Human Capability
    用户能否因此更好地认识、思考、判断、行动、学习和自我进化？
```

系统能力不是最终目的。它的价值要通过真实结果与人的能力增长体现。

## 2. System Capability

| Capability | Question | Typical LifeOS Components |
|---|---|---|
| Observe | 发生了什么？ | 输入、事实、反馈、Evidence |
| Understand | 当前人、事、环境意味着什么？ | Self / Context / Role / Goal |
| Diagnose | 真正的问题、差距或约束是什么？ | Kernel / Thinking |
| Reason | 有哪些解释、因果、方案和取舍？ | Thinking / Mental Models |
| Decide | 当前应承诺什么选择？ | Decision |
| Plan | 如何把方向转化为可执行路径？ | Execution / Templates |
| Support Action | 如何推动现实行动而非停留在分析？ | Execution / Communication |
| Learn | 结果告诉了我们什么？ | Learning / Review |
| Adapt | 下一轮应该改变什么？ | Model Update / Personalization |

系统智能闭环：

```text
Observe → Understand → Diagnose → Reason → Decide
   → Plan → Act → Observe Result → Learn → Adapt
```

## 3. Human Capability Model

LifeOS 重点促进以下可迁移能力：

| Human Capability | Desired Growth |
|---|---|
| Self Awareness | 更准确地认识自己的价值、状态、模式、优势与限制 |
| Situational Awareness | 看见角色、关系、规则、资源、约束和风险 |
| Problem Framing | 区分表面症状与真正问题 |
| Critical Thinking | 区分事实、解释、假设、价值与未知 |
| Systems Thinking | 看见关系、反馈、延迟和二阶影响 |
| Judgment | 在不完整信息与不确定性中形成合理判断 |
| Decision Making | 做取舍、承诺并知道何时重新评估 |
| Communication | 建立共同理解、反馈、协商和协作 |
| Execution | 将意图转化为行动、结果和反馈 |
| Learning | 根据目标选择学习策略并形成可迁移能力 |
| Reflection | 从经历提炼有效经验而非简单归因 |
| Metacognition | 观察自己的思考方式、偏差和置信度 |
| Adaptability | 情境变化后重新理解、调整并继续前进 |

这些不是人格标签，也不应该被当作固定分数定义一个人。

## 4. Outcome Value + Capability Value

一次重要 LifeOS Runtime 应尽量产生两种价值：

```text
Real Problem
    ↓
  LifeOS
   ├───────────────┐
   ↓               ↓
Outcome Value      Capability Value
推进当前问题         增强未来处理类似问题的能力
   └───────────────┬
                   ↓
                Autonomy
```

因此评估不能只问“建议是否有用”，还要问：

- 用户是否更理解问题？
- 是否知道为什么这样判断？
- 是否获得可复用的模型或原则？
- 下一次是否能减少外部帮助？
- 是否能够把经验迁移到新情境？

## 5. Capability Growth Protocol

重要运行可以使用以下轻量协议：

```text
1. Solve / Advance
   先推进真实问题。

2. Expose Reasoning Structure
   在有价值时让用户看见关键事实、假设、模型和取舍。

3. User Participation
   让用户完成关键判断、解释或行动，而不是全部由 AI 代劳。

4. Capture Learning
   提炼可复用原则、模式、边界或反例。

5. Transfer Check
   问：这个经验还能用于什么新情境？

6. Assistance Adjustment
   如果用户已经掌握，则下一次降低帮助强度。
```

不是每次 Quick Runtime 都需要完整执行。认知成本必须与问题价值匹配。

## 6. Capability Evidence Gate

不要因为用户一次表现好或差就永久更新能力判断。

能力更新应优先基于：

```text
Observed Behavior
+ Repeated Evidence
+ Different Contexts
+ Independent Performance
+ Feedback / Outcome
```

建议记录：

```text
Capability
Observed Evidence
Counterevidence
Context
Assistance Level
Confidence
Transfer Evidence
Review Date
```

## 7. Assistance Ladder

LifeOS 的目标不是永远提供最大帮助，而是提供**当前最小但足够的帮助**。

| Level | Mode | LifeOS Role | User Role |
|---|---|---|---|
| A0 | Answer | 给出直接答案/信息 | 理解与使用 |
| A1 | Guide | 给出结构和步骤 | 跟随并完成 |
| A2 | Coach | 主要通过问题、反馈和提示 | 主动形成判断 |
| A3 | Collaborate | 双方共同建模和推理 | 承担核心推理 |
| A4 | Calibrate | 只检查盲点、证据和置信度 | 独立完成主要过程 |
| A5 | Independent | LifeOS 默认不介入 | 用户自主运行 |

Assistance Level 不是能力等级，也不是线性晋级游戏。不同领域、风险和情境可以使用不同级别。

### 调整原则

```text
能力证据不足 / 高风险 / 新领域
        → 更多结构性支持

重复成功 + 可解释 + 可迁移
        → 减少帮助

出现新证据 / 环境变化 / 高不确定性
        → 临时增加帮助
```

**降低依赖本身是成功指标。**

## 8. Metacognition Loop

LifeOS 应帮助用户逐渐看见：

```text
Event
 ↓
Observation
 ↓
Interpretation
 ↓
Assumption / Mental Model
 ↓
Judgment
 ↓
Decision
 ↓
Action
 ↓
Outcome
```

关键问题包括：

- 我真正知道什么？
- 哪部分只是解释？
- 我假设了什么？
- 我的置信度是否与证据匹配？
- 什么证据会让我改变观点？
- 我是否把一次事件错误地变成永久性的自我判断？

目标不是让用户怀疑一切，而是提高认知校准能力。

## 9. Mental Model Direction

Mental Model Library 可以成为未来能力，但必须避免变成“模型大全”。

每个模型至少描述：

```text
Definition
Problem Type
Trigger
Assumptions
How to Apply
Example
Counterexample
Failure Modes
Boundary
Related Models
Practice / Transfer
```

Router 原则：

```text
Problem
→ Diagnosis
→ Candidate Models
→ Relevance Check
→ Minimum Useful Models
→ Apply
→ Explain when useful
→ Transfer
```

用户不需要知道模型名字才能得到帮助；当解释模型能提升未来能力时，再把模型显性化。

## 10. Capability Admission Rule

未来新增 Core 能力、Method、Playbook、Agent 或功能时，应回答：

1. 它增强了哪项 System Capability？
2. 它创造了什么 Outcome Value？
3. 它可能增强哪项 Human Capability？
4. 有什么可观察 Evidence？
5. 它是否增加不必要的 Process Cost？
6. 它是否可能制造依赖？
7. 是否已有更简单的 Kernel/Core 机制可以完成？

不能回答这些问题的能力，不应轻易进入 Core。

## 11. North-star Progression

```text
LifeOS solves a problem
        ↓
User understands the structure
        ↓
User participates in reasoning/action
        ↓
User extracts transferable learning
        ↓
User handles similar problems with less help
        ↓
LifeOS becomes calibration rather than dependency
        ↓
Become Your Own LifeOS
```

> **LifeOS 的最终目标，不是让用户越来越擅长使用 LifeOS，而是让用户越来越有能力独立运行自己的 LifeOS。**
