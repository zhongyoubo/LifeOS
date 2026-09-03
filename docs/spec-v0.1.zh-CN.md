# LifeOS Framework Specification v0.1

[English](./spec-v0.1.md) | **简体中文**

> **认识自己 · 驾驭人生 · 持续进化**

## 1. LifeOS 是什么

LifeOS 是一套开源的个人认知、成长、决策与行动操作系统。

它不是一套规定“正确人生”的答案，也不是人格测试、效率工具或成功学方法的集合。它提供一个稳定、可扩展、可个性化的运行框架，帮助人持续完成：

```text
认识自己 → 理解情境 → 明确问题 → 思考 → 决策 → 沟通 → 行动 → 复盘 → 学习 → 进化
```

LifeOS 的最终目标不是让人依赖 LifeOS，而是逐渐形成属于自己的判断体系、行动体系和成长体系。

## 2. 总体架构

```text
                    LifeOS
                      │
       ┌──────────────┼──────────────┐
       │              │              │
     SELF           CONTEXT        GOAL
    我是谁？         我在哪里？       我要去哪？
       │              │              │
       └──────────────┼──────────────┘
                      ↓
                 CORE OS 内核
                      │
   ┌────────┬────────┬────────┬────────┐
   ↓        ↓        ↓        ↓        ↓
 Thinking Decision Communication Execution Learning
   思考      决策       沟通       执行      学习
                      │
              Emotion & Energy
                  情绪与能量
                      │
                    Review
                     复盘
                      ↓
                  PLAYBOOKS
                  场景解决方案
                      ↓
             Experience / Feedback
                  经验与反馈
                      ↓
                 Self Evolution
                    自我进化
```

## 3. 四个基础模型

### 3.1 Self Model — 自我模型

回答：**我是谁？现在的我是什么状态？**

建议至少维护以下维度：

| 维度 | 核心问题 |
|---|---|
| Identity 身份 | 我如何理解自己？ |
| Values 价值观 | 什么对我真正重要？ |
| Needs 需求 | 我当前真正需要什么？ |
| Interests 兴趣 | 什么事情持续吸引我？ |
| Strengths 优势 | 我在哪些方面更容易产生价值？ |
| Limitations 局限 | 我的能力、资源和认知边界是什么？ |
| Patterns 模式 | 我有哪些重复出现的行为与反应模式？ |
| Resources 资源 | 我拥有怎样的时间、知识、关系与资产？ |
| Relationships 关系 | 哪些关系正在影响我的人生？ |
| Responsibilities 责任 | 我正在承担哪些责任？ |
| Life Stage 人生阶段 | 我目前处于怎样的发展阶段？ |

Self Model 必须允许版本演进：

```text
Self v1.0 → Experience → Reflection → Learning → Self v1.1
```

任何 MBTI、DISC、能力标签或身份标签都只能作为观察材料，不能成为永久定义。

### 3.2 Context Model — 情境模型

回答：**我现在处于什么环境？**

统一采用：

```text
Context = Role + Goal + People + Rules + Resources + Constraints + Risks + Time
```

同一个人在不同 Context 下可以采用不同策略，而不需要改变核心价值和基础操作系统。

### 3.3 Role Model — 角色模型

回答：**在这个情境下，我是谁？我应该承担什么？**

一个人同时拥有多个角色，例如：个人、伴侣、父母、朋友、学习者、工程师、管理者、项目负责人、创业者。

每个 Role 建议定义：

```text
Role
├── Purpose       为什么存在
├── Responsibility 责任
├── Authority     权限
├── Expectations  关键期望
├── Relationships 协作关系
├── Boundaries    边界
├── Outcomes      结果
└── Risks         主要风险
```

LifeOS 的目标不是让人拥有固定行为，而是形成：

```text
Stable Core + Role Adapter + Context Strategy
```

### 3.4 Goal Model — 目标模型

回答：**我要去哪？为什么？什么叫完成？**

目标至少需要澄清：

```text
Why      为什么值得做
What     希望发生什么变化
Outcome  最终结果
Measure  如何判断进展
Horizon  时间范围
Cost     愿意付出什么
Boundary 不愿牺牲什么
Next     下一步是什么
```

目标必须服务于价值，而不能仅仅成为待办事项。

## 4. Core OS — 七大运行系统

Self 是基础模型，Core OS 由七个跨场景能力系统组成。

### Thinking — 思考系统

从信息走向理解。

```text
Observe → Clarify → Decompose → Analyze → Synthesize → Hypothesize
```

核心要求：区分事实、解释、假设、观点、价值判断和未知信息。

### Decision — 决策系统

从理解走向选择。

```text
Decision = Goal + Options + Criteria + Trade-offs + Risk + Commitment
```

不是追求绝对正确，而是在当前信息和约束下做出可解释、可承担、可修正的选择。

### Communication — 沟通系统

让不同人的认知、目标和行动产生有效连接。

```text
Intent → Audience → Message → Channel → Feedback → Alignment
```

### Execution — 执行系统

把选择转化为现实变化。

```text
Outcome → Milestone → Action → Owner → Time → Checkpoint → Adjustment
```

### Learning — 学习系统

把未知逐渐转化为能力。

```text
Question → Model → Practice → Feedback → Correction → Transfer
```

真正的学习结果不是“知道”，而是能够理解、解释、应用、迁移和创造。

### Emotion & Energy — 情绪与能量系统

管理人的实际运行状态，而不是假设人始终理性且精力无限。

关注：情绪、注意力、压力、恢复、身体状态、动机和认知负荷。

### Review — 复盘系统

把经历转化为成长。

```text
Expected → Actual → Gap → Why → Lesson → Change → Verify
```

没有 Review，经历只是经历；经过 Review，经历才可能成为经验。

## 5. LifeOS 统一运行循环

任何问题优先经过统一循环，而不是立即寻找某个方法论：

```text
1. Observe     发生了什么？
2. Clarify     真正的问题是什么？
3. Context     当前角色、目标、约束是什么？
4. Think       我如何理解这个问题？
5. Decide      我选择什么？为什么？
6. Communicate 谁需要知道、理解或协同？
7. Act         下一步具体行动是什么？
8. Observe     结果发生了什么？
9. Review      哪些有效，哪些无效？
10. Learn      我应该更新什么？
11. Evolve     我的模型、原则或行为如何改变？
```

## 6. 方法论分层

LifeOS 不应该成为“1000 个方法论大全”。所有内容按以下层级组织：

```text
Principle 原则
   ↓
Process 流程
   ↓
Method 方法
   ↓
Tool 工具
   ↓
Template 模板
```

原则决定方向，流程保证稳定性，方法提供策略，工具降低成本，模板帮助快速执行。

## 7. Playbook 标准

Playbook 是 LifeOS 面向真实问题的执行单元。

每个 Playbook 应遵循统一结构：

```text
Situation
Problem
Goal
Role
Context
Diagnosis
Key Questions
Options
Trade-offs
Decision
Communication
Action Plan
Checkpoint
Review
Learning
```

首批 Playbook 建议覆盖：重大人生决策、新角色适应、职业选择、复杂项目接手、冲突处理、学习新领域、目标失败后的恢复。

## 8. AI Native LifeOS

AI 不是 LifeOS 的答案机器，而是认知与行动辅助层。

```text
User Situation
      ↓
Context Analyzer
      ↓
Role Analyzer
      ↓
Problem Classifier
      ↓
LifeOS Core
      ↓
Playbook Router
      ↓
Guided Thinking
      ↓
Decision Support
      ↓
Action Planning
      ↓
Review & Learning
```

AI 必须：说明假设、暴露不确定性、区分事实与判断、允许用户覆盖建议、避免替用户定义价值和人生目标。

## 9. 个性化机制

LifeOS 默认框架只是起点。

```text
Default LifeOS
      ↓
My Self Model
My Values
My Principles
My Roles
My Methods
My Playbooks
My Experiences
My Lessons
      ↓
My LifeOS
```

成熟的 LifeOS 应越来越像用户自己，而不是越来越像框架作者。

## 10. v0.1 完成定义

LifeOS v0.1 完成的标志不是内容数量，而是以下规范稳定：

- 项目哲学与边界
- Self / Context / Role / Goal 四大模型
- 七大 Core OS 系统
- 统一运行循环
- Principle → Template 方法论分层
- Playbook 标准
- 双语规范
- AI Native 基础架构

在这些基础稳定后，再进入 v0.2 的具体方法库建设。
