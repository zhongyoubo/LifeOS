# LifeOS Framework Specification v0.1

**English** | [简体中文](./spec-v0.1.zh-CN.md)

> **Know Yourself · Navigate Life · Evolve Yourself**

## 1. What Is LifeOS?

LifeOS is an open-source personal operating system for self-awareness, growth, decision-making, and action.

It is not a prescription for the "right life," a personality test, a productivity tool, or a collection of success formulas. It provides a stable, extensible, and personalizable framework for continuously moving through:

```text
Know Yourself → Understand Context → Clarify → Think → Decide → Communicate → Act → Review → Learn → Evolve
```

The ultimate goal is not dependence on LifeOS, but the development of one's own judgment, operating methods, and growth system.

## 2. Architecture

```text
                    LifeOS
                      │
       ┌──────────────┼──────────────┐
       │              │              │
     SELF           CONTEXT        GOAL
   Who am I?       Where am I?   Where am I going?
       │              │              │
       └──────────────┼──────────────┘
                      ↓
                    CORE OS
                      │
   Thinking · Decision · Communication · Execution · Learning
                      │
               Emotion & Energy
                      │
                    Review
                      ↓
                  PLAYBOOKS
                      ↓
             Experience / Feedback
                      ↓
                 Self Evolution
```

## 3. Four Foundation Models

### 3.1 Self Model

Answers: **Who am I, and what is my current state?**

Maintain identity, values, needs, interests, strengths, limitations, patterns, resources, relationships, responsibilities, and life stage.

The Self Model is versioned and editable:

```text
Self v1.0 → Experience → Reflection → Learning → Self v1.1
```

Personality types and labels may provide observations, but must never become permanent definitions.

### 3.2 Context Model

Answers: **What environment am I operating in?**

```text
Context = Role + Goal + People + Rules + Resources + Constraints + Risks + Time
```

A person can change strategy across contexts without replacing their underlying values or operating system.

### 3.3 Role Model

Answers: **Who am I in this context, and what am I responsible for?**

```text
Role
├── Purpose
├── Responsibility
├── Authority
├── Expectations
├── Relationships
├── Boundaries
├── Outcomes
└── Risks
```

LifeOS uses:

```text
Stable Core + Role Adapter + Context Strategy
```

### 3.4 Goal Model

Answers: **Where am I going, why, and what does completion mean?**

Clarify Why, What, Outcome, Measure, Horizon, Cost, Boundary, and Next Action. Goals should serve values rather than merely becoming tasks.

## 4. Core OS

Self is the foundation model. Seven reusable systems form the operational core.

### Thinking

```text
Observe → Clarify → Decompose → Analyze → Synthesize → Hypothesize
```

Separate facts, interpretations, assumptions, opinions, values, and unknowns.

### Decision

```text
Decision = Goal + Options + Criteria + Trade-offs + Risk + Commitment
```

Aim for explainable and revisable choices under current information and constraints, not imaginary certainty.

### Communication

```text
Intent → Audience → Message → Channel → Feedback → Alignment
```

### Execution

```text
Outcome → Milestone → Action → Owner → Time → Checkpoint → Adjustment
```

### Learning

```text
Question → Model → Practice → Feedback → Correction → Transfer
```

Learning is demonstrated through understanding, explanation, application, transfer, and creation.

### Emotion & Energy

Account for emotion, attention, stress, recovery, physical state, motivation, and cognitive load. Humans are not assumed to be perfectly rational or infinitely energetic.

### Review

```text
Expected → Actual → Gap → Why → Lesson → Change → Verify
```

Experience becomes reusable learning through reflection and change.

## 5. Unified LifeOS Loop

```text
1. Observe
2. Clarify
3. Context
4. Think
5. Decide
6. Communicate
7. Act
8. Observe Results
9. Review
10. Learn
11. Evolve
```

Use the stable loop before reaching for a specific technique.

## 6. Methodology Layers

LifeOS must not become an encyclopedia of disconnected methods.

```text
Principle
   ↓
Process
   ↓
Method
   ↓
Tool
   ↓
Template
```

Principles guide direction. Processes create stability. Methods provide strategies. Tools reduce cost. Templates accelerate execution.

## 7. Playbook Specification

A Playbook is an executable LifeOS unit for a class of real-world problems.

```text
Situation
Problem
Goal
Role
Context
Diagnosis
Key Questions
Options
Trade-offs
Decision
Communication
Action Plan
Checkpoint
Review
Learning
```

Initial playbooks should cover major life decisions, adapting to a new role, career choices, taking over complex projects, conflict, learning new domains, and recovering from failed goals.

## 8. AI-Native LifeOS

AI is an augmentation layer, not an answer authority.

```text
User Situation
      ↓
Context Analyzer
      ↓
Role Analyzer
      ↓
Problem Classifier
      ↓
LifeOS Core
      ↓
Playbook Router
      ↓
Guided Thinking
      ↓
Decision Support
      ↓
Action Planning
      ↓
Review & Learning
```

AI should expose assumptions and uncertainty, distinguish facts from judgments, permit user override, and avoid defining a user's values or life goals for them.

## 9. Personalization

```text
Default LifeOS
      ↓
My Self Model
My Values
My Principles
My Roles
My Methods
My Playbooks
My Experiences
My Lessons
      ↓
My LifeOS
```

A mature LifeOS should increasingly resemble the person using it rather than the framework's authors.

## 10. Definition of v0.1

v0.1 is complete when the following are stable enough to build upon:

- philosophy and boundaries;
- Self / Context / Role / Goal models;
- seven Core OS systems;
- unified operating loop;
- Principle-to-Template methodology hierarchy;
- Playbook specification;
- bilingual convention;
- AI-native foundation.

Only then should LifeOS expand aggressively into a library of specific methods and playbooks.
