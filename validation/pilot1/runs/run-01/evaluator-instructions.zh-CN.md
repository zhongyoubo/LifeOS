# Pilot-1 Run 01 — Evaluator Instructions

## 你应该看到的材料

仅使用：

- `evaluator_pack.jsonl`
- `../../evaluation.schema.json`
- `../../report-template.zh-CN.md`（仅用于理解指标，不用于查看结论）

## 不要查看

在提交全部评分前，请不要查看：

- `raw_outputs.jsonl`
- `skills/lifeos/`
- 任何旧的 validation run
- Git history 中可能暴露条件的信息

## 评分

每个 Case 分别对 Response A / B 打 1–5 分：

- Clarity
- Context Fit
- Insight
- Decision Support
- Actionability
- Autonomy
- Process Cost（越低越好）

然后做 Pairwise Choice：

- Overall
- Better understands the situation
- Clearer next action
- More likely to use
- Unnecessary complexity

## 纪律

- 回答更长不能自动加分。
- 专业术语或结构化格式不能自动加分。
- 如果简单回答已经足够，额外结构应体现在更高 Process Cost。
- 不猜测哪一个是 LifeOS。
- 所有 20 个 Case 完成前不讨论答案来源。

## 提交

建议每位 Evaluator 使用唯一 ID，例如 `E01`、`E02`、`E03`，输出符合 `evaluation.schema.json` 的 JSONL 文件。

至少 3 位独立 Evaluator 后再锁定评分、公开 Reveal Key 并运行 aggregate。
