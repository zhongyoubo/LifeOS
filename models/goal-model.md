# Goal Model

**English** | [简体中文](./goal-model.zh-CN.md)

The Goal Model answers: **What do I want to change, why is it worth changing, and what does done mean?**

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

- **explore** — evidence is insufficient for long-term commitment; use low-cost reversible experiments to gain real information.
- **commit** — direction has enough confidence for explicit goals, milestones, and commitment.
- **maintain** — the current state is worth preserving; focus on stable operation and health checks.
- **exit** — the objective is to stop, leave, or end a commitment that is no longer worth continued investment.

Exploration itself may be a legitimate goal:

```text
Uncertainty → Experiment → Evidence → Self/Context Update → Direction → Goal
```

## Principles

Distinguish wishes, directions, goals, and tasks. Describe desired change, not merely activity. Clarify Why. State acceptable costs and boundaries. Goals may be revised when new information appears. When evidence is insufficient, prefer Exploration Mode instead of manufacturing false certainty. Important goals should define Evidence Needed and a Revisit Condition.

```text
Values → Direction → Goal → Outcome → Milestone → Action
```
