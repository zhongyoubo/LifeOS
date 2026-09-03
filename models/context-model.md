# Context Model

**English** | [简体中文](./context-model.zh-CN.md)

The Context Model answers: **What situation am I in, and how is it shaping my choices?**

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

## Principles

- Understand context before choosing a method.
- Separate facts, assumptions, and unknowns.
- The same person may use different strategies in different contexts.
- Context is a dynamic snapshot and should be updated as conditions change.
- Do not mistake environmental constraints for personal incapability or personality flaws.
