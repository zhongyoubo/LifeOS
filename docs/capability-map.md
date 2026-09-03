# LifeOS Capability Map

**English** | [简体中文](./capability-map.zh-CN.md)

> This document defines LifeOS's long-term capability direction and bridges vision to architecture. It does not change the frozen v0.1.1 Runtime semantics.

## Dual Capability Thesis

LifeOS develops two coupled capability sets:

```text
LifeOS
├── System Capability
│   Understand, diagnose, reason, support action, learn and adapt
└── Human Capability
    Help the user become better at awareness, framing, judgment,
    action, learning, reflection, metacognition and adaptation
```

System capability is not the final objective. Its value must appear in real-world outcomes and human capability growth.

## System Capability

| Capability | Core Question |
|---|---|
| Observe | What happened? |
| Understand | What does this situation mean? |
| Diagnose | What is the real problem, gap or constraint? |
| Reason | What explanations, causal structures, options and tradeoffs matter? |
| Decide | What should be chosen or committed to now? |
| Plan | How does direction become an executable path? |
| Support Action | How do we move reality rather than remain in analysis? |
| Learn | What does the outcome teach us? |
| Adapt | What should change in the next cycle? |

```text
Observe → Understand → Diagnose → Reason → Decide
→ Plan → Act → Observe Result → Learn → Adapt
```

## Human Capability Model

LifeOS aims to strengthen transferable capabilities: Self Awareness, Situational Awareness, Problem Framing, Critical Thinking, Systems Thinking, Judgment, Decision Making, Communication, Execution, Learning, Reflection, Metacognition and Adaptability.

These are not personality labels and should not become fixed scores that define a person.

## Outcome Value + Capability Value

```text
Real Problem
    ↓
  LifeOS
   ├───────────────┐
   ↓               ↓
Outcome Value      Capability Value
advance this case  improve future capability
   └───────────────┬
                   ↓
                Autonomy
```

Evaluation should therefore ask not only whether advice was useful, but whether the user understands why, gained a reusable model, can transfer the learning, and can handle similar future problems with less assistance.

## Capability Growth Protocol

For important runs:

1. **Solve / Advance** — move the real problem first.
2. **Expose Reasoning Structure** — reveal key facts, assumptions, models and tradeoffs when useful.
3. **User Participation** — preserve essential judgment and action for the user.
4. **Capture Learning** — extract reusable principles, patterns, boundaries or counterexamples.
5. **Transfer Check** — identify where else the learning applies.
6. **Assistance Adjustment** — reduce assistance when evidence shows growing capability.

Quick Runtime should not mechanically execute the full protocol; cognitive cost must match the value of the problem.

## Capability Evidence Gate

Do not infer stable capability from a single success or failure. Prefer observed behavior, repeated evidence, multiple contexts, independent performance and outcome/feedback.

Suggested record:

```text
Capability
Observed Evidence
Counterevidence
Context
Assistance Level
Confidence
Transfer Evidence
Review Date
```

## Assistance Ladder

LifeOS should provide the minimum sufficient assistance rather than maximum assistance.

| Level | Mode | LifeOS Role | User Role |
|---|---|---|---|
| A0 | Answer | direct answer/information | understand and use |
| A1 | Guide | structure and steps | follow and complete |
| A2 | Coach | questions, feedback, hints | form judgment actively |
| A3 | Collaborate | joint modeling/reasoning | own core reasoning |
| A4 | Calibrate | check blind spots, evidence and confidence | independently run the process |
| A5 | Independent | no default intervention | operate autonomously |

The ladder is contextual, not a universal competence score. New domains, higher risk or uncertainty can justify temporarily increasing assistance. Repeated success, explanation and transfer justify reducing it.

**Reduced dependence is itself a success signal.**

## Metacognition Loop

```text
Event → Observation → Interpretation → Assumption / Mental Model
→ Judgment → Decision → Action → Outcome
```

LifeOS should help users distinguish what they know from what they infer, calibrate confidence to evidence, identify evidence that would change their mind, and avoid turning a single event into a permanent self-judgment.

## Mental Model Direction

A future Mental Model Library should not become a catalogue of clever concepts. Each model should specify Definition, Problem Type, Trigger, Assumptions, Application, Example, Counterexample, Failure Modes, Boundary, Related Models, and Practice/Transfer.

```text
Problem → Diagnosis → Candidate Models → Relevance Check
→ Minimum Useful Models → Apply → Explain when useful → Transfer
```

Users should not need to know a model's name to benefit from it. Make the model explicit when doing so improves future capability.

## Capability Admission Rule

For any future Core capability, method, playbook, agent or feature, ask:

1. Which System Capability does it strengthen?
2. What Outcome Value does it create?
3. Which Human Capability might it strengthen?
4. What observable evidence would demonstrate that?
5. Does it add unnecessary Process Cost?
6. Could it create dependency?
7. Can a simpler Kernel/Core mechanism already do the job?

If these cannot be answered, the capability should not enter Core easily.

## North-star Progression

```text
LifeOS solves a problem
→ User understands the structure
→ User participates in reasoning/action
→ User extracts transferable learning
→ User handles similar problems with less help
→ LifeOS becomes calibration rather than dependency
→ Become Your Own LifeOS
```

> **The ultimate goal is not to make people better users of LifeOS, but to help them become increasingly capable of operating their own LifeOS.**
