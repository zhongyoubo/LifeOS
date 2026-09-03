# v0.1.2 Candidate — Cognitive Augmentation Protocols

**English** | [简体中文](./cognitive-augmentation.zh-CN.md)

> Status: **PROPOSAL / NOT PART OF FROZEN v0.1.1**

The goal is not to make LifeOS think more on behalf of the user, but to help the user develop more accurate, calibrated and transferable judgment.

## Positioning

```text
Situation
→ Cognitive Calibration
→ Problem Framing
→ Mental Model Router
→ Reason / Decide / Act
→ Evidence
→ Reflection + Transfer
→ Better Independent Judgment
```

This is not a proposed new Core OS layer. It should first be validated as reusable protocols across Thinking, Decision, Learning and Review.

## Cognitive Calibration Protocol

Calibration aims for **Confidence ≈ Quality of Evidence**, not maximum confidence or permanent doubt.

For consequential judgments, separate when useful:

```text
Facts          observable/verifiable information
Interpretation meaning assigned to facts
Assumptions    unverified premises required by reasoning
Values         what matters and how tradeoffs are valued
Unknowns       missing information that could affect judgment
Prediction     testable expectation about the future
Confidence     qualitative confidence in the judgment
```

Prefer qualitative confidence such as Low / Medium / High unless real quantitative evidence supports precision.

Useful questions include: What do we actually know? What is interpretation? Which assumption is most fragile? What counterevidence exists? Which unknown is most valuable to reduce? What evidence would change the conclusion? Does the next action require more certainty? How reversible is being wrong?

```text
Initial Judgment
→ Evidence / Counterevidence
→ Alternative Explanation
→ Uncertainty / Reversibility
→ Updated Judgment + Confidence
→ Checkpoint / Disconfirming Evidence
```

Changing one's mind in response to evidence is successful calibration.

## Mental Model Protocol

A mental model is valuable only when it improves real judgment. LifeOS should not default to model catalogues or force models into a problem to appear sophisticated.

A stable model should specify:

```text
Name
Definition
Purpose / Problem Type
Trigger Conditions
Core Mechanism
Assumptions
How to Apply
Questions to Ask
Example
Counterexample
Failure Modes
Boundary / When Not to Use
Related / Competing Models
Practice
Transfer Cases
Evidence Notes
```

### Mental Model Router

```text
Problem Diagnosis
→ Missing reasoning capability
→ Candidate Models
→ Relevance Check
→ Boundary / Assumption Check
→ Minimum Useful Model(s)
→ Apply to actual problem
→ Did it change understanding or action?
   ├─ No  → discard
   └─ Yes → optionally expose model to user
```

Example signals include sunk investment → Sunk Cost + Opportunity Cost; local optimization harming the whole → Systems/Bottleneck/Feedback; short-term vs long-term effects → Second-order Effects/Compounding; uncertain options → Reversibility/Option Value; single explanation → Alternative Hypotheses/Base Rates; responsibility without power → Responsibility–Authority Gap; one failure becoming a permanent self-label → Evidence Gate/Attribution.

For Quick Runtime, using a model's logic silently is often better than teaching its name.

## Model Selection Gate

Expose a model explicitly when at least one is true: it changes problem framing; changes an important decision/action; reveals a major blind spot; is likely to be reusable and worth teaching; or the user explicitly wants the method. Otherwise keep it in background reasoning to reduce Process Cost.

## Metacognitive Transfer Protocol

```text
What happened?
→ How did I interpret it?
→ What assumption/model did I use?
→ What evidence supported it?
→ What did I miss?
→ What happened after acting?
→ What should I keep/change next time?
→ Where else does this transfer?
```

Extract reusable judgment principles, triggers, boundaries/counterexamples and signals to recognize earlier next time. Do not promote one experience into a universal rule.

## Cognitive Bias Handling

Do not use a catalogue of cognitive biases as labels for users.

```text
Observe reasoning pattern
→ identify concrete evidence gap
→ test alternative explanation
→ show consequence
→ name a bias only if the label improves learning
```

Avoid replacing analysis with labels, confusing values with biases, or assuming AI reasoning is bias-free.

## AI Guidance

AI should improve judgment structure rather than pile up model names; strengthen calibration for high-impact, irreversible or uncertain problems; move faster on low-risk reversible problems and learn from feedback; identify the most decision-relevant unknown; seek disconfirming evidence; preserve uncertainty when multiple explanations remain plausible; explain model selection when useful; reduce explanation as the user becomes capable; and never present AI inference as established fact.

## Output Contract

Standard/Deep runs may include as needed:

```text
Current Judgment
Known Facts
Key Interpretation
Critical Assumption
Important Unknown
Alternative Explanation
Relevant Mental Model (optional)
Decision / Next Action
Confidence
What Would Change the Judgment
Checkpoint
Transfer Lesson (after evidence)
```

Quick Runtime should retain only fields that affect the next action.

## Validation Hypotheses

- Calibration reduces confusion between facts, interpretations and assumptions.
- The Mental Model Router improves Context Fit and Insight over catalogue-style model advice.
- Minimum Useful Model selection does not systematically increase Process Cost.
- Repeated use improves users' independent identification of assumptions and useful models.
- Assistance can move from Guide/Coach toward Calibrate without reducing outcome quality.

Candidate cases should include self-judgment after project failure, sunk-cost continuation, two uncertain job options, team scaling that reduces delivery, disagreement with a leader, high-confidence consequential choices, repeated similar cases to test assistance reduction, and a simple reversible decision to test over-analysis.

## Admission Gate

Before stable Core/Runtime adoption, demonstrate improvement in at least two of Clarity, Insight and Decision Support; no loss of Actionability; acceptable Process Cost; no encouragement of endless analysis; observable calibration/transfer improvement; and incremental value beyond existing Thinking and Decision systems. Otherwise retain the mechanism as a Thinking or Decision Pattern rather than creating a new architecture layer.
