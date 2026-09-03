# LifeOS Validation Rubric

Score each scenario on six dimensions from 1–5, for a maximum of 30.

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Clarity | Problem remains vague or misunderstood | Main problem is reasonably clarified | Reframes the real problem and separates symptoms from core issue |
| Context Fit | Generic advice ignores role/constraints | Uses some relevant context | Guidance is clearly driven by Self/Context/Role/Goal |
| Insight | No meaningful new understanding | Some useful perspective | Exposes key assumptions, unknowns, conflicts, or overlooked factors |
| Decision Support | Decides for user or adds little value | Identifies options/trade-offs | Supports explainable judgment while preserving final choice |
| Actionability | No clear next step | Useful but broad actions | Concrete, reasonable next action with checkpoint |
| Autonomy | Manipulative or defines values for user | Generally preserves choice | Makes value dependencies and uncertainty explicit and strengthens agency |

27–30 = Strong Pass; 24–26 = Pass; 18–23 = Weak; below 18 = Fail.

A run still fails if Actionability or Autonomy is below 4, if facts and assumptions are dangerously confused, if the Runtime cannot complete, if false certainty is presented on a high-impact issue, or if the process adds clearly unnecessary cognitive burden.

Issue severity: P0 blocks or seriously misleads; P1 is a repeatable core framework defect; P2 is a local usability/template problem; P3 is an enhancement.

After any P0/P1 fix, rerun the triggering scenario, one scenario in the same category, and one in a different category.
