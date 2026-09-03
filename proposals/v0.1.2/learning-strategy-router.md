# v0.1.2 Candidate — Learning Strategy Router

**English** | [简体中文](./learning-strategy-router.zh-CN.md)

> Status: **PROPOSAL / NOT PART OF FROZEN v0.1.1**

This proposal does not modify the frozen baseline. It should enter v0.1.2 only if validation demonstrates stable incremental value.

## Purpose

When a user says “I want to learn X,” LifeOS should not default to one generic study plan. The strategy must depend on what the user needs to do with the knowledge, current level, required depth, deadline, context, constraints, and evidence of mastery.

```text
Learning Request
→ Learning Diagnosis
→ Learning Strategy Router
→ Method Stack
→ Learning Path
→ Learn → Practice → Apply → Verify → Transfer
```

## Minimum Diagnosis

Ask only for information that would change the strategy. If enough context is already available, proceed directly.

- What are you learning?
- What do you need it for?
- What can you already do?
- By when?
- What must you be able to do to count as success?

Additional variables when relevant: required depth, use context, resources, language, tools, and practice opportunities.

## Learning Goal Levels

```text
L0 Exposure       recognize what it is
L1 Understand     explain it in your own words
L2 Apply          use it with known patterns
L3 Analyze/Judge  compare options and make judgments
L4 Create         solve novel problems independently
L5 Teach/Transfer teach and transfer across contexts
```

Do not optimize every learner for L5. Avoid over-learning beyond the actual goal.

## Strategy Router

| Intent | Default Strategy | Evidence |
|---|---|---|
| Quick orientation | Overview → Concept Map → Key Concepts → Examples | explain the map and vocabulary |
| Complex understanding | First Principles → Mental Model → Analogy → Contrast → Retrieval | explain why, boundaries and counterexamples |
| Systematic domain mastery | Domain Map → Fundamentals → Modules → Connections → Cases | build and use a coherent domain model |
| Skill acquisition | Demonstration → Decomposition → Deliberate Practice → Feedback | perform without prompts |
| Solve a real problem | Problem-driven Learning → Just-in-time Research → Apply → Review | real problem progresses and lessons emerge |
| Enter an unfamiliar domain | Domain Map → Core 20% → Vocabulary → Canonical Cases → Expert Sources → Decision Practice | discuss with experts and make basic judgments |
| Exam preparation | Syllabus Map → Retrieval → Spacing → Error Log → Mock Tests | test performance improves |
| Prepare to teach | Feynman → Explain → Gap Detection → Relearn → Teach-back → Q&A | explain without notes and answer questions |
| Professional capability | Fundamentals → Deliberate Practice → Projects → Expert Feedback → Case Library | handle novel, complex cases |
| Durable retention | Retrieval → Spacing → Interleaving → Application → Review | delayed recall and application remain strong |

These are defaults, not rigid prescriptions.

## Selection Rule

```text
Goal
→ Learning Gap
→ Required Evidence
→ Strategy
→ Minimum Useful Methods
→ Practice
→ Verification
```

Choose methods after defining the capability and evidence required.

Method families include Knowledge Mapping, Understanding, Memory, Skill Practice, Application, Transfer, and Reflection.

## Output Contract

For explicit learning requests, prefer an executable learning design over a catalogue of methods:

```text
Learning Goal
Current → Target Gap
Recommended Strategy
Why This Strategy
Learning Map
Stages / Sequence
Practice Tasks
Verification / Success Criteria
Resources Needed (when relevant)
First Learning Action
Review Checkpoint
```

Quick requests should use a reduced form rather than forcing every field.

## Verification Gate

Do not treat content consumption as mastery.

```text
Recognition → Recall → Explain → Apply → Solve Novel Problem → Teach / Transfer
```

Evidence must match the target level. L1 may require explanation; L3 requires comparison and judgment; L4 requires evidence from a project or novel problem.

## Adaptive Loop

```text
Plan → Learn → Retrieve/Explain → Practice/Apply → Evidence → Gap Diagnosis → Next Cycle
```

Route gaps differently: knowledge gaps need targeted input, model gaps need explanation/contrast, skill gaps need practice, feedback gaps need external feedback/tests, and transfer gaps need novel cases.

## AI Guidance

AI should select strategies from goals rather than defaulting to resource lists; avoid questionnaire-like interrogation; encourage retrieval, explanation and practice; generate exercises, cases and feedback; diagnose gap types; adapt difficulty from evidence; distinguish AI-completed work from user mastery; recommend authoritative resources when useful; and minimize methodology overhead.

## Stop Rule

Stop planning and begin learning once the target depth, current gap, minimum useful path, and first feedback-producing action are sufficiently clear.

## Validation

Test at least: quick AI Agent orientation; one-month architecture-review preparation; heavy theory but inability to build projects; next-day teaching preparation; exam retention; production-level skill development; a 30-minute concept-learning request; and open-ended philosophy learning.

Measure Context Fit, Actionability, Process Cost, practice initiation, learning transfer, autonomy, and whether the router avoids unnecessary long-term plans.

## Admission Gate

Admit this into Core Learning only if it reliably selects different strategies for different intents, adds value beyond the current Learning System, gets users into practice faster, does not systematically increase Process Cost or reduce Autonomy, and gains real learning/transfer evidence in Human Validation. Otherwise downgrade it to a Learning Pattern or Template.
