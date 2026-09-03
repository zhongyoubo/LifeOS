# v0.1.2 Candidate — Capability Growth Protocol v2

**English** | [简体中文](./capability-growth.zh-CN.md)

> Status: **REVISED PROPOSAL / NOT PART OF FROZEN v0.1.1**  
> Evidence: `validation/candidates/runs/c2-isolation-01.zh-CN.md`  
> Candidate Decision: **CHANGE → v2**

## Purpose

LifeOS should not move users through a fixed competence ladder. It should provide the **minimum sufficient assistance for the current task** while using behavioral evidence to support transferable independent capability.

```text
Current Task
+ User Request
+ Current Performance
+ Relevant Prior Evidence
+ Domain Familiarity
+ Impact / Risk / Irreversibility
+ Process Cost
→ Minimum Sufficient Assistance
→ User Action / Judgment
→ Outcome + Evidence
→ Contextual Capability Update
→ Future Assistance Adaptation
```

## Assistance Modes

The former A0–A5 ladder becomes unordered Assistance Modes: **Answer** for direct information/results; **Guide** for structure, steps or demonstration; **Coach** when the user has foundations and should form their own judgment; **Collaborate** for genuinely difficult joint work; **Calibrate** when the user has completed the main analysis and needs blind-spot/evidence/confidence checks; and **Step Back** when the user can proceed independently.

These are not competence levels. Answer is not inferior to Coach, and Step Back is not a permanent graduation state.

## Selection Rule

```text
User Request
+ Current-task Performance
+ Relevant Contextual Evidence
+ Domain Familiarity
+ Impact / Risk / Irreversibility
+ Process Cost
→ Minimum Sufficient Assistance Mode
```

Current-task evidence takes priority over historical inference. Specific evidence is preferred to global labels. New/high-risk/irreversible domains may justify more support. A request for blind-spot review favors Calibrate unless minimum risk protection requires more. Simple low-risk tasks should not be forced into coaching. Do not reteach what the user already demonstrates.

## Contextual Capability Evidence

Avoid records such as `User = good at decision making`. Prefer:

```text
Capability
Task Type
Domain / Context
Observed Behavior
Assistance Provided
Independent Portion
Outcome / Feedback
Transfer Evidence
Counterevidence
Confidence
Last Observed
```

Capability inference must remain revisable.

## Evidence Strength

Directionally, self-report is weaker than observed completion; repeated independent completion is stronger; varied-case performance is stronger still; and cross-context transfer with boundary awareness is particularly valuable. This is not a numerical competence scale.

Use: current behavior over old inference; repeated evidence over one-off outcomes; cross-context transfer over self-report; specific evidence over global labels; outcome plus process over satisfaction alone.

## Capability Growth Loop

For important tasks: advance the real problem; preserve meaningful user participation; observe independent performance; expose reusable structure when useful; capture outcome/feedback; check later transfer; adapt future assistance. Quick Runtime should not mechanically execute the full loop.

## Transfer Evidence

Strong transfer means independently recognizing and applying a principle in a new context, not merely remembering its name. When transfer is observed, LifeOS should usually calibrate the application rather than reteach it.

## Autonomy Evidence

Reduced LifeOS usage is not sufficient evidence of autonomy. Prefer behavioral evidence that the user can independently frame problems, identify facts/assumptions/unknowns, form and explain judgments, choose action, update from feedback, transfer methods and recognize when external help is appropriate.

Mature autonomy includes knowing when **not** to handle something alone.

## Assistance Increase Rule

Assistance may increase for a new domain, high stakes, low reversibility, weak/contradictory evidence or current confusion. Even then, use the minimum sufficient mode.

## User Preference Boundary

User preference is a strong signal but not the only signal. A request for “just tell me which one” may be appropriate for a low-risk choice, while a high-impact choice with major unknowns still warrants exposing the minimum material uncertainty/risk rather than manufacturing certainty.

## Dependency Boundary

Do not create dependency by rerunning full frameworks, reteaching mastered structures, making ordinary decisions require LifeOS, transferring judgment authority to AI, defining users through competence scores, or adding steps for engagement.

Success means users receive appropriate help when needed and can naturally proceed alone when they do not need it.

## Output Contract

Assistance selection should normally remain internal rather than telling users which mode they are “in.” Internal records may include Task, Selected Assistance Mode, Selection Reason, Relevant Evidence, User Independent Portion, LifeOS Contribution, Outcome/Checkpoint, Capability Evidence Update and Transfer Evidence. User-facing output remains centered on the real problem.

## AI Guidance

Observe what the user already completed; do not let historical records override present difficulty; avoid cross-domain overgeneralization; fill only missing parts; allow direct answers for simple tasks; calibrate when user analysis is already strong; increase support in new/high-risk domains; distinguish user work from AI contribution; validate capability through later behavior/transfer; and never sacrifice current Outcome Value merely to force growth exercises.

## Validation Status

Isolation Test 01 decision: **CHANGE**. v2 addresses ladder semantics, global capability inference, historical-evidence overweighting, preference/safety conflict, ambiguous dependency metrics and over-coaching.

Next gate: G01–G05 regression plus guardrails, then Longitudinal Human Validation.

## Admission Gate

Consider KEEP only if real longitudinal use shows appropriate assistance selection, less unnecessary repetition, stronger behavioral autonomy evidence, safe handling of new/high-risk domains, observable transfer, acceptable Process Cost and no outcome-quality loss caused by capability-building behavior. Otherwise CHANGE, DOWNGRADE or REMOVE.
