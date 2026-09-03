# v0.1.2 Candidate — Cognitive Augmentation v2

**English** | [简体中文](./cognitive-augmentation.zh-CN.md)

> Status: **REVISED PROPOSAL / NOT PART OF FROZEN v0.1.1**  
> Evidence: `validation/candidates/runs/c3-isolation-01.zh-CN.md`  
> Candidate Decision: **CHANGE → v2**

## Purpose

C3 v2 is not a new cognitive-augmentation layer. It provides two reusable protocols and one learning interface:

```text
A. Judgment Calibration Protocol
B. Reasoning Lens Router
C. Transfer Interface
```

The goal is to improve judgment only when useful without turning LifeOS into an over-analysis system.

## Trigger Gate

Strengthen C3 when material Impact, Uncertainty, Risk, Irreversibility, strong confidence with weak evidence, repeated reasoning failure, or identity-level conclusions from limited evidence are present. For low-risk, reversible situations with fast feedback, prefer action and learning from outcome.

## Judgment Calibration

```text
Current Judgment
→ What is known?
→ What is inferred / assumed?
→ Critical Unknown
→ 1–3 Plausible Alternatives
→ Disconfirming Evidence
→ Reversibility / Downside
→ Updated Judgment
→ What would change it?
→ Action Sufficiency
```

Expose only fields that materially affect judgment or action. Do not force a full evidence worksheet. Prefer qualitative confidence unless quantitative evidence supports precision. Updating a judgment in response to evidence is successful calibration.

## Alternative Explanations

Use the current explanation plus one to three plausible alternatives and identify evidence that best distinguishes them. Stop expanding when additional alternatives would not change action.

## Disconfirming Evidence

For high-confidence or consequential judgments, ask what evidence could overturn the conclusion, where it is most likely wrong, what the downside is, and whether commitment can be staged. The purpose is calibrated commitment, not permanent doubt.

## Reasoning Lens Router

The v1 Mental Model Router becomes a **Reasoning Lens Router**:

```text
Problem Diagnosis
→ Missing reasoning
→ Candidate Lens
→ Mechanism / Boundary Check
→ Minimum Useful Lens
→ Apply
→ Materially changed understanding/action?
   ├─ No  → discard
   └─ Yes → keep; optionally explain/name
```

A lens may come from a mental model, system principle, decision method or domain mechanism. Runtime does not require a model name first.

Examples include comparing future options/opportunity cost for sunk investment; bottleneck/coordination/feedback for team scaling; reversibility/option value for uncertain choices; alternative hypotheses for single attribution; Responsibility–Authority Gap for responsibility without control; and evidence/attribution boundaries for identity conclusions from one failure.

## Model Naming Rule

Validate the mechanism before naming the model. Name it when the label improves future reuse, the user wants the method, its boundary matters, or naming does not add unnecessary Process Cost. Otherwise use the logic silently.

## Transfer Interface

C3 may generate a **Candidate Transfer Lesson**, but it cannot claim Transfer Capability:

```text
Outcome / Reflection
→ Candidate Lesson
→ Trigger
→ Boundary / Counterexample
→ Next-time Signal
→ hand off to C2 Capability Evidence
→ future independent behavior
→ Transfer Evidence or Counterevidence
```

**Transfer Lesson ≠ Transfer Evidence.** Future transfer is validated by C2 contextual capability evidence.

## Action Sufficiency Rule

Act when judgment is sufficient for the next step, remaining uncertainty is unlikely to change the current action, downside is acceptable or reversible, action will generate evidence faster than more analysis, and no major irreversible risk remains unaddressed.

```text
More Analysis Value < Feedback Value from Action
→ ACT
```

C3 obeys the Kernel Stop Rule rather than creating another reasoning loop.

## Bias Handling

Start with the observed reasoning pattern, concrete evidence gap, plausible alternative and consequence. Name a bias only when useful for transfer. Values, risk preferences and different goals are not automatically cognitive biases.

## Boundary with C2

C3 determines **which cognitive operation is useful**. C2 determines **how much assistance LifeOS should provide**. C3 does not maintain its own assistance ladder or user competence levels.

## Output Contract

Standard/Deep runs may include Current Judgment, critical Known/Assumed distinction, Critical Unknown, Plausible Alternative, Disconfirming Evidence, optional Reasoning Lens, Reversibility/Downside, Updated Judgment, Next Action, What Would Change the Judgment, Checkpoint and a Candidate Transfer Lesson after evidence. Quick runs retain only what affects the next action.

## AI Guidance

First decide whether C3 is needed. Separate only material known/inferred/assumed elements; prioritize the critical unknown; generate few high-value alternatives; seek disconfirming evidence for strong confidence; examine downside/staged commitment for consequential irreversible choices; use the minimum useful reasoning lens; apply mechanism before naming it; stop when remaining uncertainty will not change action; never treat a Transfer Lesson as capability evidence; hand future transfer validation to C2; and never present AI inference as fact.

## Validation Status

Isolation 01 decision: **CHANGE**. v2 addresses over-triggering, evidence-stack formality, model-catalogue gravity, model-naming bias, hypothesis explosion, transfer inflation, overlap with C2 and calibration paralysis.

Next gate: C01–C08 regression plus guardrails.

## Admission Gate

Consider KEEP only if Calibration Quality and Insight/Decision Support improve without Actionability loss, simple scenarios avoid Process Cost regression, analysis paralysis does not systematically appear, selected lenses materially change understanding/action, later human Calibration/Transfer Evidence appears, and C3 demonstrates incremental value beyond existing Thinking/Decision. Otherwise CHANGE, DOWNGRADE or REMOVE.
