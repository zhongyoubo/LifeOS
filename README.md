# LifeOS

> **Know Yourself · Navigate Life · Evolve Yourself**

[English](README.md) | [简体中文](README.zh-CN.md)

LifeOS is an open-source personal operating system for self-awareness, context understanding, better judgment, effective action, learning, and lifelong growth.

It pursues two goals at the same time: **make LifeOS more capable, and make the user more capable.**

> **The ultimate goal of LifeOS is to help you become your own LifeOS.**

## Mission

Help people understand themselves, understand their world, form better judgment, take meaningful action, and continuously grow from experience.

LifeOS does not optimize for doing more on behalf of the user. Its long-term objective is to strengthen human cognition, judgment, action, learning, metacognition, and autonomy.

See: [LifeOS Vision and Capability Model](docs/vision.md)

## Start Here

- [Vision and Capability Model](docs/vision.md)
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

## Two Capability Tracks

```text
LifeOS
│
├── System Capability
│   └── Understand → Diagnose → Reason → Plan → Support Action → Learn / Adapt
│
└── Human Capability
    └── Awareness → Framing → Thinking → Judgment → Action → Learning → Reflection → Metacognition → Adaptability
```

Every meaningful run should aim to create both:

- **Outcome Value** — the current problem is better understood, judged, or advanced;
- **Capability Value** — the user becomes more able to handle similar problems independently in the future.

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
11. Important runs should consider whether transferable Capability Value was created.
12. Better cognition does not mean more confidence; judgment and confidence should become better calibrated to reality.

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
├── docs/          # vision, architecture, spec, kernel, admission rules
├── models/        # Self / Context / Role / Goal
├── core/          # seven Core OS systems
├── templates/     # reusable execution artifacts
├── playbooks/     # optional domain playbooks
├── skills/lifeos/ # AI runtime skill
├── validation/    # scenarios, rubric, regressions, A/B and human validation
└── examples/
```

## Status

**Current stage: v0.1.1 — validation-driven architecture baseline**

The frozen core remains stable. Vision, validation infrastructure, and future candidate capabilities may evolve, but the frozen core should not expand without evidence from Blind / Human Validation.

## License

LifeOS is released under the MIT License unless otherwise noted.
