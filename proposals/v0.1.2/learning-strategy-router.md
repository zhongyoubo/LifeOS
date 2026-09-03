# v0.1.2 Candidate — Learning Strategy Router v2

**English** | [简体中文](./learning-strategy-router.zh-CN.md)

> Status: **REVISED PROPOSAL / NOT PART OF FROZEN v0.1.1**  
> Evidence: `validation/candidates/runs/c1-isolation-01.zh-CN.md`  
> Candidate Decision: **CHANGE → v2**

## Purpose

The v0.1.1 Learning System already owns the general loop:

```text
Question → Map → Learn → Explain → Practice → Feedback → Correct → Apply → Transfer
```

C1 v2 does not create another learning-method system. It answers one upstream question:

> **What is the minimum appropriate strategy for this learning task?**

```text
Learning Request
→ Intent
→ Target Mastery Depth
→ Current Gap
→ Deadline / Use Context
→ Success Evidence
→ Minimum Useful Strategy
→ Existing Learning Loop
→ Evidence → Adapt → Transfer
```

## Minimum Diagnosis

Collect only information that can change the strategy: Target, Intent, Target Mastery Depth, Current Gap, Deadline/Use Context and Success Evidence. Do not mechanically ask for every variable when context is sufficient.

## Learning Intent

Use intent to avoid forcing all learning into one utilitarian form:

```text
explore      open inquiry, questions and connections
understand   build explanatory understanding
perform      execute a skill or task
judge        compare, analyze and form judgment
create       build, design or solve novel problems
teach        explain clearly and support others' understanding
retain       preserve durable access over time
```

A task may have a primary and secondary intent.

For philosophy, history, art, culture or curiosity-driven exploration, Success Evidence need not be job performance. Better questions, clearer understanding of disagreements, cross-topic connections, revised views and sustained inquiry may be valid evidence.

## Target Mastery Depth

The former L0–L5 scale is reframed as **Target Mastery Depth** for the current topic, not a permanent learner level:

```text
Exposure       recognize what it is
Understand     explain in your own words
Apply          use in familiar patterns
Analyze/Judge  compare options, find issues and explain tradeoffs
Create         independently solve novel problems or build things
Teach/Transfer teach and transfer across contexts
```

Depth is a planning aid. Concrete behavioral evidence remains the actual validation mechanism.

## Current Gap

Identify only the dominant bottleneck when useful: Knowledge Gap, Model Gap, Skill Gap, Feedback Gap or Transfer Gap. Do not classify for its own sake.

## Strategy Selection

```text
Intent
+ Target Mastery Depth
+ Current Gap
+ Deadline / Use Context
+ Success Evidence
→ Minimum Useful Strategy
```

Examples: a 30-minute AI Agent orientation routes to Overview → Concept Map → Core Concepts → Example → Explain-back → Stop; a one-month architecture review routes to Domain Map → Mechanisms → Tradeoffs → Cases → Review Practice; theory without project ability routes to reduced input plus real project/practice/feedback; next-day teaching routes to Explain → Gap Detection → Teach-back → Q&A → Rehearse; exam retention routes to Retrieval → Spacing → Error Log → Mock Test; production capability routes to real systems, failure cases, expert review and novel problems; open-ended philosophy routes to map, primary ideas, reading/dialogue, reflection/writing and connections.

These are examples, not prescriptions. Remove anything that does not add value to the current task.

## Method Boundary

C1 owns no independent Method Library. Feynman, Active Recall, Spaced Repetition, Deliberate Practice, Project-based Learning and related methods remain methods available to the Learning System.

```text
C1 selects Why / When
→ Learning System executes How
```

## Success Evidence

**Define what evidence would demonstrate the target before selecting how to learn.**

Examples: Understand → unprompted explanation plus boundaries; Judge → compare real options and explain tradeoffs; Perform → complete the task without critical prompts; Create → handle a novel problem/project; Teach → explain and answer follow-up questions; Retain → delayed retrieval/application; Explore → improved questions, connections, revised understanding and continued inquiry.

Finishing a course or book is usually Activity Evidence, not Mastery Evidence.

## Output Contract

Default minimum:

```text
Learning Goal
Target Depth
Recommended Strategy
Why
First Practice Action
Success Evidence
Checkpoint
```

Expand only for complex tasks. Quick requests may reduce to `Goal → Strategy → First Action → Check`.

## Adaptive Loop

After entering the existing Learning Loop, use evidence to identify the current bottleneck and adjust only what is needed. Plans are not commitments; evidence may change the route.

## Stop Rule

Begin learning once Intent and Target Depth are sufficiently clear, the dominant gap is known or can quickly be discovered through practice, Success Evidence is defined, and a feedback-producing First Action exists. Stop earlier for low-risk short-duration requests.

## AI Guidance

AI should identify intent before strategy; avoid automatically professionalizing or projectizing learning; never treat Target Depth as a user capability label; choose the minimum useful strategy; avoid questionnaire behavior; reuse existing Learning methods; validate with behavior rather than content consumption; distinguish AI completion from user mastery; reduce assistance when evidence shows mastery; and adapt after real feedback.

## Validation Status

Isolation Test 01 decision: **CHANGE**. The strongest incremental value came from Target Depth, Use Context/Deadline, Current Gap and Success Evidence driving Strategy Selection.

v2 addresses method duplication, level reification, over-diagnosis, utilitarian bias against Explore learning (P1), and false precision.

Next gate: regression on L01–L07, followed by Human Learning Validation.

## Admission Gate

C1 v2 is still not Core. Consider KEEP only after Regression + Human Validation demonstrate stable Strategy Fit improvement, faster effective practice, better goal-matched Success Evidence, no Quick Process Cost regression, no Autonomy loss, and real learning/retention/transfer evidence. Otherwise DOWNGRADE or REMOVE.
