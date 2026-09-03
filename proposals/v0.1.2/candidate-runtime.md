# v0.1.2 Candidate — Unified Runtime Proposal

**English** | [简体中文](./candidate-runtime.zh-CN.md)

> Status: **PROPOSAL / NOT PART OF FROZEN v0.1.1**  
> Evidence: `validation/candidates/runs/candidate-interaction-01.zh-CN.md`

## Architecture Principle

v0.1.2 does not add three serial architecture layers. The stable center remains Foundation Models → Kernel Runtime → Core OS → Action / Feedback / Review. C1, C2 and C3 are orthogonal protocols sparsely triggered by the Kernel.

```text
Situation
→ Kernel
   ├─ Runtime Level
   ├─ Problem Diagnosis
   ├─ Foundation Model Loader
   ├─ Core Router
   ├─ Candidate Trigger Router
   └─ Stop / Continue Owner
        ├─ C1 Learning Strategy Selection
        ├─ C2 Assistance Selection
        └─ C3 Cognitive Operation
→ Core OS
→ Action / Feedback
→ Review
→ Evidence Update
```

## Single Orchestrator Rule

Kernel is the only orchestrator. Candidates must not create a fixed pipeline between themselves, choose Runtime Level, own the global Stop Rule, create separate user profiles, bypass Core OS, or become top-level systems.

## Candidate Trigger Router

Activation must be sparse: zero candidates for normal/simple Core flow, one candidate commonly, two when genuinely cross-cutting, and all three only rarely.

### C1
Trigger for learning, understanding, mastery, practice, retention, teaching or development of domain judgment. C1 owns Intent, Target Mastery Depth, Current Gap, Deadline/Use Context, Target Success Evidence and Minimum Useful Learning Strategy.

### C2
Trigger when the amount/type of LifeOS assistance materially affects Outcome, Autonomy or Process Cost. C2 owns Assistance Selection, Contextual Capability Evidence, Observed Independent Portion and Future Assistance Adaptation.

Modes: `Answer / Guide / Coach / Collaborate / Review / Step Back`. `Review` replaces the former `Calibrate` to avoid collision with C3 Judgment Calibration.

### C3
Trigger for material Impact, Uncertainty, Risk, Irreversibility, strong confidence with weak evidence, repeated reasoning failure, or identity-level conclusions from limited evidence. C3 owns Judgment Calibration, Reasoning Lens Selection and Candidate Transfer Lesson.

## Orthogonality

C1 asks how this learning task should be approached. C2 asks how much and what kind of help LifeOS should provide. C3 asks which cognitive operation would improve the judgment. They must not duplicate one another when combined.

## Evidence Ownership

- Target Evidence → C1: what would demonstrate the current learning target.
- Judgment Evidence → C3: what supports, weakens or changes the current judgment.
- Candidate Transfer Lesson → C3: a potentially reusable principle, trigger and boundary.
- Capability Evidence → C2: what the user actually performed independently and whether later transfer occurred.
- Outcome Evidence → Review/lifecycle: what happened after action.

`Target Evidence ≠ Capability Evidence`; `Transfer Lesson ≠ Transfer Evidence`; `Judgment Evidence ≠ Outcome Evidence`. Candidates do not create separate evidence stores; implementation should use a unified evidence model/lifecycle.

## Stop Ownership

Only Kernel owns global Stop/Continue. Candidates return readiness signals. C1 readiness means intent/depth are sufficient, target evidence is defined and a feedback-producing first practice action exists. C3 readiness means the material judgment is sufficient, remaining uncertainty is unlikely to change the next action and material irreversible downside has been addressed.

Kernel combines problem clarity, risk/reversibility, candidate readiness, next-action availability, expected value of more analysis and feedback value from action. When marginal analysis value is lower than feedback value from action, act.

## Runtime Sequence

1. Select Runtime Level.
2. Observe and clarify the real problem.
3. Load Self / Context / Role / Goal as needed.
4. Separate material facts, interpretations, assumptions and unknowns.
5. Diagnose problem type.
6. Route to Core OS.
7. Evaluate Candidate Triggers.
8. Activate the minimum necessary candidate protocols.
9. Execute through Core OS.
10. Kernel evaluates Stop / Continue.
11. Produce a concrete next action and checkpoint.
12. Observe outcome when available.
13. Review.
14. Update evidence according to explicit ownership.

Candidate activation is not a mandatory new layer before Core.

## User-visible Output Rule

Hide C1/C2/C3 names, Assistance Mode names, Trigger Router, evidence ownership and internal readiness fields by default. Users should experience problem solving rather than LifeOS architecture. Expose methods when the user wants to learn them, the name supports future transfer, mechanism explanation materially improves judgment, or the user is designing/debugging LifeOS itself.

## Quick Runtime Guardrail

Quick requests use Core first, activate candidates only when clearly useful, keep output minimal, answer/act/check and stop. Capability Growth or Cognitive Augmentation must not force questionnaires, reflection or model teaching.

## Conflict Resolution Priority

```text
Safety / material risk
> explicit user goal and values
> Kernel architecture rules
> current-task evidence
> candidate protocol preference
> historical inference
```

A candidate's growth objective must never override real Outcome Value.

## Version Boundary

Before Human Validation, do not modify frozen v0.1.1 Core, admit candidates into stable architecture, claim Human Capability is proven, build a large Mental Model Library, or prematurely implement Personal Agent / long-term personalization runtime.

## Validation Gate

Before Candidate Build: I01–I04 Interaction Regression must pass; P0 and P1 must be zero; no systematic Process Cost regression; sparse activation must work; evidence ownership must remain unambiguous; and Kernel must remain the single orchestrator. Then proceed to Human Validation rather than expanding theory.
