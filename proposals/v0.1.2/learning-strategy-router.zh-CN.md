# v0.1.2 Candidate — Learning Strategy Router

[English](./learning-strategy-router.md) | **简体中文**

> 状态：**PROPOSAL / NOT PART OF FROZEN v0.1.1**
>
> 本提案不修改当前冻结基线。只有验证证明存在稳定增量价值后，才进入 v0.1.2。

## 1. 问题

当前 Learning System 已定义 `Question → Map → Learn → Explain → Practice → Feedback → Correct → Apply → Transfer`，但用户说“我想学 X”时，不同目标实际上需要不同学习策略。

“了解 AI Agent”“一个月后参与 AI Agent 架构评审”“成为 Agent 开发工程师”“明天给别人讲 Agent”不能使用同一学习计划。

因此需要在 Learning Process 前增加一个轻量策略路由器：

```text
Learning Request
      ↓
Learning Diagnosis
      ↓
Learning Strategy Router
      ↓
Method Stack
      ↓
Learning Path
      ↓
Learn → Practice → Apply → Verify → Transfer
```

## 2. Learning Diagnosis

只收集会改变学习策略的信息。信息已经足够时不要机械提问。

核心变量：

- **Target** — 要学什么？
- **Purpose** — 为什么学？
- **Current Level** — 当前已经会什么？
- **Required Depth** — 了解 / 理解 / 应用 / 判断 / 专业 / 教授？
- **Deadline** — 什么时候需要达到目标？
- **Use Context** — 考试、工作、项目、决策、教学还是兴趣？
- **Constraints** — 时间、资源、语言、工具、实践机会？
- **Success Evidence** — 什么证据能证明“已经学会”？

推荐最小诊断：

```text
Learn What?
For What?
Current Level?
By When?
What must you be able to do?
```

## 3. Learning Goal Levels

不要把“学习”当作单一状态。

```text
L0 Exposure       我见过/知道它是什么
L1 Understand     我能用自己的话解释
L2 Apply          我能按规则使用
L3 Analyze/Judge  我能比较方案、发现问题、做判断
L4 Create         我能独立解决新问题/构建东西
L5 Teach/Transfer 我能教授，并迁移到新的情境
```

用户不需要总是达到 L5。策略必须服务于目标深度，避免过度学习。

## 4. Strategy Router

| Learning Intent | Default Strategy | Evidence of Learning |
|---|---|---|
| 快速了解 | Overview → Concept Map → Key Concepts → Examples | 能解释整体地图和核心术语 |
| 理解复杂概念 | First Principles → Mental Model → Analogy → Boundary/Contrast → Retrieval | 能解释为什么、边界和反例 |
| 系统掌握领域 | Domain Map → Fundamentals → Modules → Connections → Cases → Review | 能建立领域模型并连接模块 |
| 学会技能 | Demonstration → Decomposition → Deliberate Practice → Feedback → Repetition | 能在无提示下完成任务 |
| 解决实际问题 | Problem-driven Learning → Just-in-time Research → Apply → Feedback → Review | 真实问题被推进且形成经验 |
| 快速进入陌生领域 | Domain Map → Core 20% → Vocabulary → Canonical Cases → Expert Sources → Decision Practice | 能与专业人员讨论并做基础判断 |
| 应对考试 | Syllabus Map → Retrieval Practice → Spaced Repetition → Error Log → Mock Test | 模拟测试与错题表现改善 |
| 准备讲给别人 | Feynman → Explain → Gap Detection → Relearn → Teach-back → Q&A | 能脱稿解释并回答问题 |
| 达到专业水平 | Fundamentals → Deliberate Practice → Projects → Expert Feedback → Case Library → Reflection | 能处理新颖、复杂、非标准问题 |
| 长期保持 | Retrieval → Spacing → Interleaving → Real Application → Periodic Review | 延迟测试和实际应用仍可调用 |

这些是默认策略，不是硬编码处方。Router 应根据实际约束组合和删减。

## 5. Method Selection Rule

LifeOS 不应该展示方法论目录然后让用户自己拼装。

方法选择顺序：

```text
Goal
→ Learning Gap
→ Required Evidence
→ Strategy
→ Minimum Useful Methods
→ Practice
→ Verification
```

原则：**先决定要形成什么能力，再选择方法。**

### Method Families

- Knowledge Mapping — Concept Map / Domain Map
- Understanding — First Principles / Analogy / Contrast / Feynman
- Memory — Active Recall / Spaced Repetition / Interleaving
- Skill — Demonstration / Deliberate Practice / Feedback
- Application — Project-based / Problem-driven / Case-based Learning
- Transfer — Teach-back / Novel Cases / Cross-context Application
- Reflection — Error Log / Review / Learning Journal

## 6. Learning Path Output Contract

当用户明确要求学习某个主题时，LifeOS 应优先给出可执行的学习方案，而不是只解释方法论。

标准输出：

```text
Learning Goal
Current → Target Gap
Recommended Strategy
Why This Strategy
Learning Map
Stages / Sequence
Practice Tasks
Verification / Success Criteria
Resources Needed (if applicable)
First Learning Action
Review Checkpoint
```

简单请求使用 Quick 版本，不强制输出全部字段。

## 7. Verification Gate

学习不能用“看完资料”作为完成标准。

建议证据层级：

```text
Recognition
   ↓
Recall
   ↓
Explain
   ↓
Apply
   ↓
Solve Novel Problem
   ↓
Teach / Transfer
```

完成条件必须与目标 Level 匹配。例如：

- 目标 L1：可以解释即可；
- 目标 L3：必须能够比较方案并说明取舍；
- 目标 L4：必须有真实项目/新问题证据。

## 8. Adaptive Loop

```text
Plan
 ↓
Learn
 ↓
Retrieve / Explain
 ↓
Practice / Apply
 ↓
Evidence
 ↓
Gap Diagnosis
 ├─ Knowledge Gap → targeted input
 ├─ Model Gap     → explanation / contrast
 ├─ Skill Gap     → practice
 ├─ Feedback Gap  → expert / test / review
 └─ Transfer Gap  → novel case
 ↓
Next Learning Cycle
```

不要因为计划已经制定就坚持原路线；证据应驱动下一轮学习。

## 9. AI Guidance

AI 应：

- 根据学习目标选择策略，而不是默认推荐课程列表；
- 信息足够时直接制定路径，不做问卷式盘问；
- 优先让用户主动检索、解释、实践；
- 生成练习、案例、反例和反馈；
- 在用户错误时诊断 gap 类型，而不仅给答案；
- 根据 evidence 调整难度；
- 明确区分“AI 帮用户完成”和“用户已经掌握”；
- 必要时推荐权威资料，但资料数量服从学习目标；
- 避免让用户因方法论过载而无法开始。

## 10. Stop Rule

学习计划的分析阶段应在以下条件满足时停止：

- 目标深度足够清楚；
- 当前差距足够清楚；
- 已有一个合理的最小学习路径；
- 可以通过实践获得更多信息。

然后立即进入第一个学习动作。

## 11. Validation Cases

至少增加以下对照测试：

1. “我想了解 AI Agent，先建立整体认知。”
2. “一个月后我要参加 AI Agent 架构评审，怎么学？”
3. “我看了很多机器学习资料，但还是不会做项目。”
4. “明天我要给团队讲一个完全陌生的概念，怎么准备？”
5. “我准备考试，知识点很多但记不住。”
6. “我已经会基本编程，想达到能独立做生产级项目的程度。”
7. “我只有 30 分钟想弄懂一个概念。”（测试 Quick / Process Cost）
8. “我想长期学习哲学，没有考试和截止日期。”（测试非功利/探索型学习）

验证重点：

- Context Fit 是否提高；
- Actionability 是否提高；
- 是否比通用学习建议更能匹配目标；
- Process Cost 是否可接受；
- 用户是否真的实践；
- 是否形成 Learning Transfer；
- 是否避免不必要的长期计划。

## 12. Admission Decision

只有满足以下条件才建议进入 Core Learning：

- 在多种学习意图下稳定选择不同策略；
- 相比现有 Learning System 有明确增量，而非换名字；
- 用户更快进入实践；
- Process Cost 不系统性增加；
- 不降低 Autonomy；
- Human Validation 中存在实际学习/迁移证据。

否则应降级为 Learning Pattern / Template，而不是扩张 Core OS。
