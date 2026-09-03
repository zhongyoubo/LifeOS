# Role Model / 角色模型

[English](./role-model.md) | **简体中文**

Role Model 用于回答：**在当前情境下，我是谁，我承担什么，我不承担什么？**

```yaml
role:
  name: ""
  purpose: ""
  responsibilities: []
  authority: []
  expectations: []
  relationships: []
  boundaries: []
  outcomes: []
  risks: []
  conflicts_with_other_roles: []
  version: "0.1"
```

## Role Adapter

LifeOS 不要求人在所有角色中表现一致，而是：

```text
Stable Core + Role Adapter + Context Strategy
```

例如，一个人可以同时是父母、伴侣、朋友、工程师和管理者。价值观可能相对稳定，但责任、权限、沟通方式、成功标准和行为策略会随角色变化。

## 角色冲突

当多个角色同时要求时间、资源或价值选择时，应显式识别 Role Conflict，而不是简单把问题解释成“时间管理不好”。
