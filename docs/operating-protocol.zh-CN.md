# LifeOS Operating Protocol / 运行协议

[English](./operating-protocol.md) | **简体中文**

Operating Protocol 定义一个真实问题进入 LifeOS 后如何被处理。它是 LifeOS 的 Kernel Runtime。

## Runtime

```text
Situation
   ↓
1 Observe ── 收集发生了什么
   ↓
2 Clarify ── 定义真正需要处理的问题
   ↓
3 Load Models
   ├─ Self
   ├─ Context
   ├─ Role
   └─ Goal
   ↓
4 Diagnose ── 判断问题类型、关键约束和未知信息
   ↓
5 Route Core OS
   ├─ Thinking
   ├─ Decision
   ├─ Communication
   ├─ Execution
   ├─ Learning
   ├─ Emotion & Energy
   └─ Review
   ↓
6 Select Playbook / Methods
   ↓
7 Produce Next Action
   ↓
8 Execute & Observe Result
   ↓
9 Review
   ↓
10 Update
   ├─ Self Model
   ├─ Context
   ├─ Principles
   ├─ Methods
   └─ Playbooks
   ↓
Evolve
```

## Minimum Viable Run

LifeOS 不要求每次把所有步骤完整执行。简单问题可以快速运行：

```text
What happened? → What matters? → What will I do next? → What happened after that?
```

问题的重要性、不确定性、风险和不可逆程度越高，运行深度越高。

## Routing Rules

- 不清楚问题是什么 → Thinking
- 有多个重要选项 → Decision
- 涉及共同理解、冲突或协作 → Communication
- 知道做什么但没有推进 → Execution
- 缺少知识或能力 → Learning
- 状态明显影响判断与行动 → Emotion & Energy
- 已经发生重要结果 → Review

一个问题可以激活多个系统。

## Runtime Output

每次完整运行至少产生：

```yaml
lifeos_run:
  situation: ""
  problem: ""
  role: ""
  goal: ""
  facts: []
  assumptions: []
  unknowns: []
  activated_systems: []
  decision: ""
  next_action: ""
  checkpoint: ""
  review_at: ""
  updates: []
```

## Stop Rule

LifeOS 的目标不是无限分析。满足以下条件即可进入行动：问题足够清晰；风险已达到可接受程度；存在合理下一步；继续分析的边际价值低于行动获取反馈的价值。
