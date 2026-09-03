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
  responsibility_authority_gaps: []
  version: "0.1.1"
```

## Role Adapter

LifeOS 不要求人在所有角色中表现一致，而是：

```text
Stable Core + Role Adapter + Context Strategy
```

## Responsibility / Authority Gap

当一个角色需要为结果负责，但缺少相应决策权、资源权、信息权或协调权时，应显式记录，而不是把后续失败简单归因于个人执行力。

检查：

```text
Responsibility
    ↓ compare
Authority / Resources / Information / Escalation Path
    ↓
Gap?
```

若存在 Gap，应优先通过 Communication / Decision 明确授权、升级路径、资源或责任边界。

## 角色冲突

当多个角色同时要求时间、资源或价值选择时，应显式识别 Role Conflict，而不是简单把问题解释成“时间管理不好”。
