# LifeOS Validation

**English** | [简体中文](./README.zh-CN.md)

LifeOS Validation tests whether the framework can reliably move a person from “I don't know what to do” toward “I understand the problem and know a reasonable next action.”

## Validation Goals

Test whether LifeOS clarifies the real problem, uses Self / Context / Role / Goal appropriately, routes to useful Core OS systems, produces meaningful insight, supports rather than replaces judgment, generates an actionable next step, converts outcomes into learning, and creates structural value beyond a generic AI response.

## Flow

```text
Scenario → Baseline AI Run → LifeOS Run → Score → Compare → Record Failures → Framework Fix → Regression Run
```

## Runtime Levels

**Quick** for simple, low-risk, reversible situations. **Standard** for ordinary life and work problems. **Deep** for high-impact, uncertain, risky, or hard-to-reverse situations.

Depth should scale with:

```text
Impact × Uncertainty × Risk × Irreversibility
```

## v0.1 Suggested Acceptance Gate

- all 20 standard scenarios complete a LifeOS Runtime;
- average six-dimension score ≥ 24/30;
- Actionability ≥ 4/5;
- Autonomy ≥ 4/5;
- no P0 framework issue prevents completion;
- P1 issues are fixed or explicitly tracked;
- compared with Baseline AI, LifeOS shows consistent improvement in at least two of Clarity, Context Fit, and Actionability.

Validation exists to discover where LifeOS fails, not to prove that it is correct.
