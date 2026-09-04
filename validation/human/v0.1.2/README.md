# LifeOS v0.1.2 Human Validation

**English** | [简体中文](./README.zh-CN.md)

> Status: **HUMAN VALIDATION BASELINE / FROZEN**

This directory turns the v0.1.2 Human Validation plan into a repeatable evidence pipeline.

```text
Real User / Real Problem
→ cases.jsonl
→ LifeOS Session
→ sessions-round-01.jsonl
→ Accepted Decision / Action
→ ~7-day Follow-up
→ followups-round-01.jsonl
→ aggregate.py
→ summary.json
→ Human Validation Report
→ KEEP / CHANGE / DOWNGRADE / REMOVE / UNCERTAIN
```

Frozen semantics: C1 = Learning Strategy Selection; C2 = Assistance Selection + Contextual Capability Evidence; C3 = Judgment Calibration + Reasoning Lens + Candidate Transfer Lesson; Kernel = Single Orchestrator + Stop Owner; Activation = Sparse; Evidence = Explicit Ownership; User Output = Problem-first / architecture-hidden. Do not modify the Round-1 baseline except for P0/P1 remediation.

Use pseudonymous user IDs and avoid unnecessary personal or sensitive data. Register a real case, capture the Before-LifeOS state, run LifeOS, record the user's actually accepted decision/action, capture immediate metrics, follow action cases at roughly seven days (14–30 days when appropriate for longer learning), aggregate, then conduct evidence review without assuming KEEP because of prior design investment.

Round 1 must include real C1 learning, longitudinal C2 use, consequential C3 judgments, mixed-candidate cases and Quick Controls. Quick Controls verify that simple problems remain lightweight.

See the parent `v0.1.2-test-pack.md` for the full gate. Decide C1, C2, C3 and Full Runtime independently; DOWNGRADE or REMOVE remains a valid outcome.
