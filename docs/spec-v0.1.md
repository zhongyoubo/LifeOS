# LifeOS Framework Specification v0.1.1

**English** | [简体中文](./spec-v0.1.zh-CN.md)

> **Know Yourself · Navigate Life · Evolve Yourself**

LifeOS is an open-source personal operating system for self-awareness, context understanding, better judgment, action, learning, and growth. It does not define a universally correct life.

## 1. Canonical Structure

```text
Foundation Models
Self / Context / Role / Goal
        ↓
Kernel Runtime
Quick / Standard / Deep
        ↓
Core OS
Thinking / Decision / Communication / Execution / Learning / Emotion & Energy / Review
        ↓
Optional Domain Layer
Playbooks / Methods / Tools / Templates
        ↓
Action → Feedback → Review → Evolution
```

The stable LifeOS core is **Models + Kernel + Core OS**. Optional domain artifacts must prove incremental value.

## 2. Foundation Models

### Self Model
Dynamic, editable, evidence-based representation of values, needs, strengths, limitations, patterns, resources, relationships, responsibilities, life stage, and current state. Important self claims should track evidence, counterevidence, confidence, source contexts, and review date.

### Context Model

```text
Context = Role + Goal + People + Rules + Resources + Constraints + Risks + Time
```

### Role Model
Defines purpose, responsibilities, authority, expectations, relationships, boundaries, outcomes, and risks. Runtime should explicitly detect responsibility-authority gaps.

### Goal Model
Supports four modes:

- `explore` — gain information before committing;
- `commit` — pursue an explicit outcome;
- `maintain` — preserve a working state;
- `exit` — intentionally stop or leave.

A lack of long-term direction does not automatically require a long-term goal; exploration may be the correct mode.

## 3. Kernel Runtime

```text
Choose Runtime Level
→ Observe
→ Clarify
→ Load Models
→ Separate Facts / Interpretations / Assumptions / Values / Unknowns
→ Diagnose
→ Route Core OS
→ Optional Domain Support
→ Next Action
→ Checkpoint / Revisit Condition
→ Review
→ Evidence-based Update
```

### Runtime Levels

**Quick** — low-impact, low-risk, reversible.  
**Standard** — ordinary life/work problems with meaningful context and dependencies.  
**Deep** — high impact, uncertainty, risk, or irreversibility.

Use only the minimum useful depth.

## 4. Seven Core OS Systems

- **Thinking** — turn information into a reliable problem model.
- **Decision** — make explainable and revisable choices under trade-offs.
- **Communication** — create sufficient shared understanding and coordination.
- **Execution** — turn choices into observable outcomes.
- **Learning** — turn unknowns into transferable capability.
- **Emotion & Energy** — manage human runtime state that affects judgment and action.
- **Review** — turn experience into testable lessons and system changes.

## 5. Methodology Hierarchy

```text
Principle → Process → Method → Tool → Template
```

Methods are plugins. The framework should not become an encyclopedia of techniques.

## 6. Optional Domain Playbooks

Playbooks are no longer a mandatory architectural layer. They are admitted only when they provide meaningful domain-specific sequencing, checks, outputs, or cognitive-cost reduction beyond the Kernel.

See [Playbook Admission Rule](./playbook-admission.md).

Current classification:

- Complex Problem → Kernel / Thinking Pattern
- Important Decision → Decision System + Template
- New Role / Environment → Trial Playbook
- Unfamiliar Project → Validated Domain Playbook
- Important Disagreement → Trial Playbook
- New Domain Learning → Validated Domain Playbook
- Failure Recovery → Validated Domain Playbook

## 7. Evolution

```text
Experience → Review → Evidence → Lesson → Change → Verify → Update
```

Updates may affect Self / Role / Goal models, principles, methods, personal patterns, or domain playbooks. Important Self updates must pass an evidence gate.

## 8. AI-Native LifeOS

```text
User Situation
→ Runtime Level Router
→ Model Loader
→ Problem Diagnosis
→ Core OS Router
→ Optional Domain Router
→ Decision / Communication / Next Action
→ Checkpoint
→ Review & Update
```

AI should expose uncertainty, distinguish fact from inference, preserve user autonomy, avoid inventing values, and avoid unnecessary framework overhead.

## 9. Validation Status

Synthetic framework validation has demonstrated that the architecture can complete 20/20 standard scenarios without P0 blockers. This is evidence of internal framework coherence, not yet proof of real-world superiority over a capable general AI.

The next release gate requires blind/human A/B validation.

## 10. Definition of v0.1.1

v0.1.1 is the validation-driven architecture baseline consisting of:

- four evidence-aware Foundation Models;
- Quick / Standard / Deep Kernel Runtime;
- seven Core OS systems;
- optional evidence-gated domain playbooks;
- Principle → Template hierarchy;
- bilingual AI Skill;
- validation and regression protocols;
- a frozen baseline suitable for blind A/B evaluation.
