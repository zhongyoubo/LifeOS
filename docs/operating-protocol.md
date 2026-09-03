# LifeOS Operating Protocol

**English** | [简体中文](./operating-protocol.zh-CN.md)

The Operating Protocol defines how a real-world situation is processed by LifeOS. It is the framework's Kernel Runtime.

## Runtime

```text
Situation
   ↓
Observe
   ↓
Clarify Problem
   ↓
Load Self + Context + Role + Goal
   ↓
Diagnose
   ↓
Route Core OS
   ↓
Select Playbook / Methods
   ↓
Produce Next Action
   ↓
Execute & Observe Result
   ↓
Review
   ↓
Update Models / Principles / Methods / Playbooks
   ↓
Evolve
```

## Minimum Viable Run

Simple situations can use a short loop:

```text
What happened? → What matters? → What will I do next? → What happened after that?
```

Run depth should increase with importance, uncertainty, risk, and irreversibility.

## Routing Rules

Unclear problem → Thinking. Multiple consequential options → Decision. Shared understanding, conflict, or coordination → Communication. Known direction but insufficient progress → Execution. Missing knowledge or capability → Learning. State strongly affects judgment/action → Emotion & Energy. Important outcome already occurred → Review.

Several systems may be activated together.

## Runtime Output

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

Move from analysis to action when the problem is sufficiently clear, risk is acceptable, a reasonable next action exists, and the marginal value of more analysis is lower than the value of feedback from action.
