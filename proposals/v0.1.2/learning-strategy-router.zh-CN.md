# v0.1.2 Candidate — Learning Strategy Router v2

[English](./learning-strategy-router.md) | **简体中文**

> 状态：**REVISED PROPOSAL / NOT PART OF FROZEN v0.1.1**  
> 依据：`validation/candidates/runs/c1-isolation-01.zh-CN.md`  
> Candidate Decision：**CHANGE → v2**

## 1. Purpose

v0.1.1 Learning System 已负责通用学习循环：

```text
Question → Map → Learn → Explain → Practice → Feedback → Correct → Apply → Transfer
```

C1 v2 不重复建设学习方法体系，只解决前置问题：

> **针对当前学习任务，什么是最小且合适的学习策略？**

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

## 2. Minimum Diagnosis

只获取会改变策略的信息。已有信息足够时直接路由，不进行问卷式盘问。

最小变量：

- **Target** — 学什么？
- **Intent** — 为什么/以什么方式学？
- **Target Mastery Depth** — 这次需要学到多深？
- **Current Gap** — 当前主要缺什么？
- **Deadline / Use Context** — 何时、在哪里使用？
- **Success Evidence** — 什么行为或结果能证明已经达到本次目标？

不是每次都需要显式询问全部变量。

## 3. Learning Intent

Intent 用于避免所有学习都被套进同一种功利目标。

```text
explore      开放探索、形成问题和连接
understand   建立理解和解释能力
perform      完成具体技能或任务
judge        比较、分析并形成专业判断
create       构建、设计或解决新问题
teach        清楚解释并帮助他人理解
retain       长期保持并可调用
```

一个任务可以有主 Intent + 次 Intent。

### Explore 特别规则

对于哲学、历史、艺术、文化或纯兴趣探索，Success Evidence 不必等于绩效输出。

可以表现为：
- 能提出更好的问题；
- 能解释重要观点与分歧；
- 能建立跨主题连接；
- 能形成并修正自己的理解；
- 愿意持续探索。

不要强迫用户把所有学习转化为项目、考试或职业能力。

## 4. Target Mastery Depth

原 L0–L5 改为 **Target Mastery Depth**。它描述“当前主题本次需要达到的深度”，不是用户的永久学习能力等级。

```text
Exposure       能识别、知道它是什么
Understand     能用自己的话解释
Apply          能在熟悉模式下使用
Analyze/Judge  能比较方案、发现问题、说明取舍
Create         能独立解决新问题或构建东西
Teach/Transfer 能教授，并迁移到不同情境
```

深度只是规划辅助。最终验证必须使用具体行为证据，不能用等级标签替代 Evidence。

## 5. Current Gap

只识别当前最主要的瓶颈：

```text
Knowledge Gap  缺少必要信息/事实
Model Gap      缺少理解结构、因果或边界
Skill Gap      知道但做不出来
Feedback Gap   做了但不知道哪里对/错
Transfer Gap   熟悉场景会做，新场景不会迁移
```

不要为了分类而分类。若 Gap 不影响下一步策略，可以省略。

## 6. Strategy Selection

```text
Intent
+ Target Mastery Depth
+ Current Gap
+ Deadline / Use Context
+ Success Evidence
        ↓
Minimum Useful Strategy
```

示例：

| Situation | Minimum Useful Strategy |
|---|---|
| 30 分钟了解 AI Agent | Overview → Concept Map → Core Concepts → Example → Explain-back → Stop |
| 一个月后架构评审 | Domain Map → Mechanisms → Tradeoffs → Cases → Architecture Review Practice |
| 理论很多但不会做项目 | Reduce Input → Real Project → Deliberate Practice → Feedback → Review |
| 明天要讲陌生概念 | Explain → Gap Detection → Teach-back → Likely Q&A → Rehearse |
| 考试记不住 | Retrieval → Spacing → Error Log → Mock Test |
| 半年达到生产级工程能力 | Real Systems → Design/Implementation → Failure Cases → Expert Review → Novel Problems |
| 长期学哲学 | Map → Primary Ideas → Reading/Dialogue → Reflection/Writing → Connections → Continue Exploring |

这些不是固定处方。Router 应删减到当前任务真正需要的最小组合。

## 7. Method Boundary

C1 不拥有独立 Method Library。

Feynman、Active Recall、Spaced Repetition、Deliberate Practice、Project-based Learning 等仍属于 Learning System 可用方法。

C1 只负责：

```text
Select Why / When
        ↓
Learning System executes How
```

这样避免 Candidate 与 Core Learning 重复维护相同方法。

## 8. Success Evidence

Success Evidence 是 v2 的核心变量。

原则：

> **先定义什么证据代表达到目标，再决定怎么学。**

示例：

```text
Understand → 无提示解释 + 能说出边界
Judge      → 比较两个真实方案并说明 tradeoff
Perform    → 无关键提示完成任务
Create     → 独立处理新问题/真实项目
Teach      → 清楚讲解 + 回答基础追问
Retain     → 延迟后仍能检索和应用
Explore    → 问题质量、理解连接、观点修正与持续探索
```

“看完课程”“读完一本书”通常只是 Activity Evidence，不是 Mastery Evidence。

## 9. Output Contract

默认最小输出：

```text
Learning Goal
Target Depth
Recommended Strategy
Why
First Practice Action
Success Evidence
Checkpoint
```

只有复杂任务才扩展 Learning Map、Stages、Resources、Practice Set 等字段。

Quick 请求可以只输出：

```text
Goal → Strategy → First Action → Check
```

## 10. Adaptive Loop

进入现有 Learning Loop 后，根据 Evidence 更新：

```text
Practice / Apply
      ↓
Evidence
      ↓
What is the current bottleneck?
      ↓
Knowledge / Model / Skill / Feedback / Transfer
      ↓
Adjust only what is needed
      ↓
Next Cycle
```

计划不是承诺；Evidence 可以改变路线。

## 11. Stop Rule

停止继续规划并开始学习，当：

- Intent 足够清楚；
- Target Depth 足够清楚；
- 当前主要 Gap 足够清楚，或可以通过实践快速发现；
- Success Evidence 已定义；
- 已有一个能产生反馈的 First Action。

对于低风险、短时学习请求，应更早 Stop。

## 12. AI Guidance

AI 应：

- 先判断学习意图，再选策略；
- 不默认把学习职业化、考试化或项目化；
- 不把 Target Depth 当用户能力标签；
- 优先选择最小有效策略；
- 信息足够时直接行动，不机械提问；
- 使用现有 Learning Methods，不重复展示方法目录；
- 用行为证据验证学习，而不是内容消费；
- 区分“AI 完成了任务”和“用户掌握了能力”；
- Evidence 显示用户已掌握时减少帮助；
- 在真实反馈出现后允许改变学习路线。

## 13. Validation Status

Isolation Test 01：**CHANGE**。

已确认候选增量主要来自：

```text
Target Depth
+ Use Context / Deadline
+ Current Gap
+ Success Evidence
→ Strategy Selection
```

已发现并在 v2 修复：
- 方法重复；
- L0–L5 等级实体化风险；
- 简单请求过度诊断；
- Explore 学习被过度工具化（P1）；
- 假精确度。

下一 Gate：使用 L01–L07 做 v2 Regression；之后再进入 Human Learning Validation。

## 14. Admission Gate

C1 v2 仍然不是 Core。

只有在 Regression + Human Validation 中证明：
- Strategy Fit 稳定提升；
- 用户更快进入有效实践；
- Success Evidence 更匹配真实目标；
- Quick 场景 Process Cost 不恶化；
- Autonomy 不下降；
- 存在真实学习/保持/迁移证据；

才考虑 KEEP。否则 DOWNGRADE / REMOVE。
