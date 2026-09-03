# Blind / Human A/B Validation Protocol

**English** | [简体中文](./blind-ab-protocol.zh-CN.md)

This protocol tests whether LifeOS provides stable, reusable structural value beyond a capable general AI assistant.

## 1. Freeze the Baseline

Once a test run starts, freeze the specification, architecture, Skill, Foundation Models, Core OS, and validation rubric. Do not modify the framework in response to individual cases until the round is complete.

## 2. Conditions

**A — Baseline:** same base model, responding as a capable general assistant without LifeOS materials or naming.

**B — LifeOS:** same base model and same user input, with the frozen LifeOS v0.1.1 Skill loaded.

Keep model, input, context budget, and tool access as similar as possible.

## 3. Blind Evaluation

Evaluators should not know which response is Baseline or LifeOS. Label outputs Response X and Response Y. Neutralize revealing headings in the scoring copy without changing substantive content.

## 4. Scenarios

Use at least the 20 standard scenarios. Prefer adding 10–20 unseen scenarios that were not used while designing the framework. For real-user testing, use the user's actual problem whenever possible.

## 5. Scoring

Use the existing six dimensions: Clarity, Context Fit, Insight, Decision Support, Actionability, Autonomy.

Also ask:

1. Which response is more helpful: X / Y / Tie?
2. Which is easier to act on?
3. Which adds unnecessary complexity?
4. Would you use this style of help again for a similar problem?

## 6. Evaluators

Prefer framework-independent human evaluators, real target users, and optionally an independent AI evaluator as a secondary signal. Author self-scoring is debugging evidence, not public validation evidence.

## 7. Suggested Public Validation Gate

- at least 30 scenarios or real-user cases;
- at least 3 independent human evaluators;
- LifeOS wins overall preference meaningfully above chance;
- stable improvement in at least two of Clarity, Context Fit, and Actionability;
- Autonomy is not worse than Baseline;
- Complexity Penalty does not materially increase;
- no P0 issues;
- any new P1 issue has an explicit remediation plan.

Do not rely only on average score. If LifeOS wins by becoming longer and harder to use, the validation should be considered unsuccessful.

## 8. Version Discipline

```text
v0.1.1 Frozen Baseline
        ↓
Blind A/B Run
        ↓
Findings
        ↓
v0.1.2 Changes
        ↓
Regression
        ↓
Next Blind Run
```

Do not move the goalposts during a test round. Collect evidence first, then change the framework.
