# LifeOS Architecture v0.1.1

**English** | [简体中文](./architecture.zh-CN.md)

LifeOS is a reusable personal operating system, not a fixed set of life instructions.

## 1. Canonical Architecture

```text
                     LifeOS
                       │
        ┌──────────────┼──────────────┐
        │              │              │
     MODELS          KERNEL        CORE OS
        │              │              │
 Self / Context   Runtime Level   Thinking
 Role / Goal      Observe         Decision
                  Clarify         Communication
                  Diagnose        Execution
                  Route           Learning
                  Act             Emotion & Energy
                  Review          Review
        │              │              │
        └──────────────┴──────────────┘
                       ↓
              OPTIONAL DOMAIN LAYER
                       │
        Playbooks / Methods / Templates
                       ↓
                 Real-world Action
                       ↓
              Experience & Feedback
                       ↓
              Model / System Evolution
```

The stable center of LifeOS is **Models + Kernel Runtime + Core OS**. Playbooks are optional domain accelerators, not part of the mandatory kernel.

## 2. Foundation Models

Four models describe the current operating state:

- **Self** — who am I, what matters, what patterns and resources do I currently have?
- **Context** — what environment, people, rules, constraints, risks, and time conditions matter?
- **Role** — what am I responsible for, what authority do I actually have, and where are the boundaries?
- **Goal** — what mode am I in: explore, commit, maintain, or exit; what outcome or information do I need next?

Models are editable and evidence-based. They are not permanent labels.

## 3. Kernel Runtime

The Kernel is the mandatory operating protocol:

```text
Choose Depth
→ Observe
→ Clarify
→ Load Models
→ Separate Facts / Interpretations / Assumptions / Values / Unknowns
→ Diagnose
→ Route Core OS
→ Produce Next Action
→ Checkpoint
→ Review
→ Update
```

Runtime depth uses Quick / Standard / Deep according to impact, uncertainty, risk, and irreversibility.

## 4. Core OS

Seven reusable systems provide cross-domain capabilities:

1. Thinking
2. Decision
3. Communication
4. Execution
5. Learning
6. Emotion & Energy
7. Review

Core OS systems are reusable across work, relationships, learning, transitions, and life decisions.

## 5. Optional Domain Layer

Playbooks, methods, tools, and templates are optional. They must reduce cognitive or execution cost without duplicating the Kernel.

```text
Kernel Runtime
   ↓
Need domain-specific sequencing/checks/outputs?
   ├─ No → continue with Core OS directly
   └─ Yes → load Optional Playbook
```

A Playbook is admitted only when it adds domain-specific value that cannot be expressed as a trivial restatement of the general Runtime.

Examples with strong domain value include:

- taking over an unfamiliar project;
- learning a new domain under a deadline;
- recovering and learning after an important failure.

Generic flows such as “handle a complex problem” should normally remain Kernel/Core patterns rather than independent Playbooks.

See [Playbook Admission Rule](./playbook-admission.md).

## 6. Evolution Mechanism

```text
Experience
→ Review
→ Evidence
→ Lesson
→ Change
→ Verify
→ Update Self / Role / Goal / Principles / Methods / Playbooks
```

Important Self Model changes pass through an evidence gate. A single result should not become a permanent identity statement.

## 7. Personalization

```text
Default LifeOS
      ↓
My Models
My Principles
My Methods
My Domain Playbooks
My Experiences
My Lessons
      ↓
My LifeOS
```

The objective is increasing judgment, agency, and capability, not dependence on the framework.

## 8. AI-Native Runtime

```text
User Situation
      ↓
Runtime Level Router
      ↓
Foundation Model Loader
      ↓
Problem Diagnosis
      ↓
Core OS Router
      ↓
Optional Domain Router
      ↓
Next Action / Decision / Communication
      ↓
Checkpoint
      ↓
Review & Evidence-based Update
```

AI augments judgment. It must expose uncertainty, avoid inventing user values, and use no more framework than the situation requires.
