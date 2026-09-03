# Goal Model / 目标模型

[English](./goal-model.md) | **简体中文**

Goal Model 用于回答：**我要改变什么、为什么值得改变、什么叫完成？**

```yaml
goal:
  mode: "explore | commit | maintain | exit"
  statement: ""
  why: ""
  desired_outcome: ""
  measures: []
  horizon: ""
  costs_willing_to_pay: []
  boundaries_not_to_cross: []
  dependencies: []
  risks: []
  milestones: []
  next_action: ""
  evidence_needed: []
  revisit_condition: ""
  status: ""
  version: "0.1.1"
```

## Goal Mode

- **explore**：证据不足，不强行承诺长期目标；目标是通过低成本、可逆实验获得真实信息。
- **commit**：方向已达到足够置信度，进入明确目标、里程碑和执行承诺。
- **maintain**：当前状态值得维持，重点是稳定运行、健康检查和防止退化。
- **exit**：目标是结束、退出或停止一项不再值得持续投入的承诺。

探索本身可以是合法目标：

```text
Uncertainty → Experiment → Evidence → Self/Context Update → Direction → Goal
```

## 原则

- 区分愿望、方向、目标和任务。
- Goal 应描述希望发生的变化，而不仅是动作。
- 明确 Why，避免为了完成目标而完成目标。
- 同时明确愿意付出的成本和不可突破的边界。
- 目标可以根据新信息修正，修改目标不天然等于失败。
- 当证据不足时，优先进入 Exploration Mode，而不是制造虚假确定性。
- 重要 Goal 应定义 Evidence Needed 和 Revisit Condition。

```text
Values → Direction → Goal → Outcome → Milestone → Action
```
