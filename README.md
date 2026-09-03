# LifeOS

> **Know Yourself · Navigate Life · Evolve Yourself**

[English](README.md) | [简体中文](README.zh-CN.md)

LifeOS is an open-source personal operating system for self-awareness, context understanding, better judgment, effective action, learning, and lifelong growth.

## Start Here

- [Framework Specification v0.1.1](docs/spec-v0.1.md)
- [Architecture v0.1.1](docs/architecture.md)
- [Operating Protocol / Kernel Runtime](docs/operating-protocol.md)
- [Foundation Models](models/)
- [Core OS](core/README.md)
- [Playbook Admission Rule](docs/playbook-admission.md)
- [Templates](templates/README.md)
- [LifeOS Skill v0.1.1](skills/lifeos/SKILL.md)
- [Validation](validation/README.md)
- [Roadmap](ROADMAP.md)

## Canonical Architecture

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

The stable center of LifeOS is **Models + Kernel + Core OS**. Domain Playbooks are optional and must prove incremental value.

## Foundation Models

- **Self** — who am I, what matters, what patterns/resources do I currently have?
- **Context** — where am I operating and what constraints, people, risks, and rules matter?
- **Role** — what am I responsible for, what authority do I actually have, and what are my boundaries?
- **Goal** — am I exploring, committing, maintaining, or exiting; what outcome or information do I need next?

## Seven Core OS Systems

- Thinking
- Decision
- Communication
- Execution
- Learning
- Emotion & Energy
- Review

## Design Principles

1. LifeOS does not prescribe a single definition of a good life.
2. It helps people think; it does not replace personal judgment.
3. Facts, interpretations, assumptions, values, and unknowns should be separated when useful.
4. Use the minimum framework depth required by the situation.
5. Process matters more than collecting methods.
6. Action should generate feedback and learning.
7. Self models remain editable and evidence-based.
8. Structural context problems should not be misread as personal defects.
9. Playbooks must prove domain-specific value before becoming stable framework artifacts.
10. The long-term objective is greater autonomy, not greater dependence on LifeOS.

## Validation Status

LifeOS has completed a 20-scenario synthetic framework validation with no P0 blockers. This supports internal framework coherence, not yet real-world superiority over a capable general AI.

Current release status:

```text
Framework Gate        PASS
Public Validation     HOLD
```

The next gate is Blind / Human A/B Validation against a general AI baseline.

## Language Policy

Chinese and English are both first-class languages. Core concepts and major specifications should maintain semantic parity.

- English default: `document.md`
- Simplified Chinese: `document.zh-CN.md`

## Project Structure

```text
LifeOS/
├── docs/          # architecture, spec, kernel, admission rules
├── models/        # Self / Context / Role / Goal
├── core/          # seven Core OS systems
├── templates/     # reusable execution artifacts
├── playbooks/     # optional domain playbooks
├── skills/lifeos/ # AI runtime skill
├── validation/    # scenarios, rubric, regressions, A/B protocol
└── examples/
```

## Status

**Current stage: v0.1.1 — validation-driven architecture baseline**

The framework is now frozen enough for blind external evaluation before adding more methods or playbooks.

## License

LifeOS is released under the MIT License unless otherwise noted.
