# Role Model

**English** | [简体中文](./role-model.zh-CN.md)

The Role Model answers: **Who am I in this context, what am I responsible for, and what am I not responsible for?**

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

LifeOS does not require identical behavior across roles. It uses:

```text
Stable Core + Role Adapter + Context Strategy
```

## Responsibility / Authority Gap

When a role is accountable for outcomes but lacks sufficient decision rights, resources, information access, or escalation paths, record the mismatch explicitly instead of reducing later failure to personal execution weakness.

```text
Responsibility
    ↓ compare
Authority / Resources / Information / Escalation Path
    ↓
Gap?
```

If a gap exists, prioritize clarifying authorization, escalation, resources, or responsibility boundaries through Communication and Decision.

## Role Conflict

When several roles compete for time, resources, or value choices, explicitly identify the Role Conflict rather than reducing the problem to poor time management.
