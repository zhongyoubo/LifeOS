# LifeOS

> **Know Yourself · Navigate Life · Evolve Yourself**

[English](README.md) | [简体中文](README.zh-CN.md)

LifeOS is an open-source personal operating system for self-awareness, personal growth, better decisions, effective action, and lifelong evolution.

LifeOS does not define what a "successful life" should look like. Instead, it provides a reusable framework to help people understand themselves, understand their context, think clearly, make decisions, communicate, act, learn, reflect, and continuously improve.

## Start Here

- [Framework Specification v0.1](docs/spec-v0.1.md)
- [Architecture](docs/architecture.md)
- [Operating Protocol / Kernel Runtime](docs/operating-protocol.md)
- [Foundation Models](models/)
- [Core OS](core/README.md)
- [Templates](templates/README.md)
- [7 Golden Playbooks](playbooks/golden-playbooks.md)
- [LifeOS Skill v0.1](skills/lifeos/SKILL.md)
- [End-to-End Examples](examples/README.md)
- [Roadmap](ROADMAP.md)

## Vision

Build an open methodology and practical operating system that helps people:

- know themselves more clearly;
- understand roles, goals, constraints, and environments;
- think and decide with structure;
- communicate and collaborate effectively;
- turn intentions into action;
- learn faster from experience;
- reflect, adapt, and grow over time.

## Core Loop

```text
Situation
   ↓
Self + Context + Role + Goal
   ↓
Think
   ↓
Decide
   ↓
Communicate
   ↓
Act
   ↓
Observe
   ↓
Review
   ↓
Learn
   ↓
Evolve
```

## LifeOS Architecture

LifeOS is organized around four foundation models and a reusable operational core:

1. **Self** — Who am I? What matters to me? What are my strengths, limits, needs, responsibilities, and current state?
2. **Context** — What situation am I operating in: people, rules, resources, constraints, risks, and time?
3. **Role** — Who am I in this context, what am I responsible for, and what are my boundaries?
4. **Goal** — What change do I want, why does it matter, and what does done mean?
5. **Core OS** — Thinking, Decision, Communication, Execution, Learning, Emotion & Energy, and Review.
6. **Playbooks** — Context-sensitive execution paths for recurring real-world situations.

## Core Systems

- Thinking
- Decision
- Communication
- Execution
- Learning
- Emotion & Energy
- Review

## Design Principles

1. LifeOS does not prescribe a single definition of a good life.
2. LifeOS helps people think; it should not replace personal judgment.
3. Facts, assumptions, values, and decisions should be distinguished clearly.
4. Processes matter more than collecting methods.
5. Every framework should eventually support action.
6. Every action should generate feedback and learning.
7. Self-models are dynamic and must remain editable.
8. The system should become increasingly personalized over time.
9. Roles may change; the underlying operating system should remain reusable.
10. The long-term goal is greater autonomy, not greater dependence on LifeOS.

## Language Policy

Chinese and English are both first-class languages in LifeOS. Core concepts, models, specifications, templates, and major playbooks should maintain semantic parity across both languages rather than treating one language as a secondary translation.

Naming convention:

- English default: `document.md`
- Simplified Chinese: `document.zh-CN.md`

The AI Skill automatically follows the user's language by default.

## Project Structure

```text
LifeOS/
├── README.md / README.zh-CN.md
├── ROADMAP.md / ROADMAP.zh-CN.md
├── docs/
│   ├── spec-v0.1.*
│   ├── architecture.*
│   └── operating-protocol.*
├── models/
│   ├── self-model.*
│   ├── context-model.*
│   ├── role-model.*
│   └── goal-model.*
├── core/
│   ├── thinking.*
│   ├── decision.*
│   ├── communication.*
│   ├── execution.*
│   ├── learning.*
│   ├── emotion-energy.*
│   └── review.*
├── templates/
├── playbooks/
├── skills/lifeos/
└── examples/
```

## Status

**Current stage: v0.1 — Foundation / executable framework**

The v0.1 foundation now includes the four models, seven Core OS systems, Kernel Runtime, core templates, seven Golden Playbooks, a bilingual AI Skill, and initial end-to-end validation examples.

The next focus is validation: apply LifeOS to diverse real situations, identify overlap or missing boundaries, refine schemas, and only then expand the method and playbook libraries.

## License

LifeOS is released under the MIT License unless otherwise noted.
