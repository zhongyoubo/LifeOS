# Context Model / 情境模型

[English](./context-model.md) | **简体中文**

Context Model 用于回答：**我现在处于什么情境，这个情境正在如何影响我的选择？**

```text
Context = Role + Goal + People + Rules + Resources + Constraints + Risks + Time
```

```yaml
context:
  situation: ""
  role: ""
  goal: ""
  people: []
  rules: []
  resources: []
  constraints: []
  risks: []
  time:
    horizon: ""
    urgency: ""
  known_facts: []
  assumptions: []
  unknowns: []
  version: "0.1"
```

## 原则

- 先理解情境，再选择方法。
- 明确哪些是事实、假设和未知信息。
- 同一个人在不同情境中可以采取不同策略。
- Context 是动态快照，应随环境变化更新。
- 不把环境约束误认为个人能力或人格缺陷。
