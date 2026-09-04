# LifeOS v0.1.2 Human Validation

[English](./README.md) | **简体中文**

> 状态：**HUMAN VALIDATION BASELINE / FROZEN**

本目录把 v0.1.2 Candidate Human Validation 从“测试方案”变成可重复执行的 Evidence Pipeline。

## Pipeline

```text
Real User / Real Problem
→ cases.jsonl
→ LifeOS Session
→ sessions/*.jsonl
→ Accepted Decision / Action
→ ~7-day Follow-up
→ followups/*.jsonl
→ aggregate.py
→ summary.json
→ Human Validation Report
→ KEEP / CHANGE / DOWNGRADE / REMOVE / UNCERTAIN
```

## Frozen Semantics

```text
C1 = Learning Strategy Selection
C2 = Assistance Selection + Contextual Capability Evidence
C3 = Judgment Calibration + Reasoning Lens + Candidate Transfer Lesson
Kernel = Single Orchestrator + Stop Owner
Activation = Sparse
Evidence = Explicit Ownership
User Output = Problem-first / architecture-hidden
```

除 P0/P1 修复外，Round 1 中途不得修改 baseline。

## Directory

```text
validation/human/v0.1.2/
├── README.md
├── README.zh-CN.md
├── cases.jsonl
├── case.schema.json
├── session.schema.json
├── followup.schema.json
├── participant-guide.md
├── participant-guide.zh-CN.md
├── evaluator-guide.md
├── evaluator-guide.zh-CN.md
├── aggregate.py
└── report-template.md
```

实际 session/follow-up 数据建议按 Round 分文件，例如：

```text
sessions-round-01.jsonl
followups-round-01.jsonl
```

避免提交真实姓名、邮箱、账号、公司机密、医疗/财务等不必要敏感信息。使用 pseudonymous `user_id`。

## Run Round 1

1. 登记真实 Case，先写清 Problem/Goal 和 Case Type。
2. 记录 Before-LifeOS 状态。
3. 执行 LifeOS；内部记录 Candidate Activation，但默认不向用户暴露架构名。
4. 记录用户实际接受的 Decision / Next Action，而不是 AI 建议本身。
5. 记录 immediate metrics。
6. 行动型 Case 约 7 天后 follow-up；长期学习可 14–30 天。
7. 使用 `aggregate.py` 汇总。
8. 独立做 Evidence Review，不因既有设计投入而默认 KEEP。

## Required Mix

Round 1 至少覆盖：C1 real learning、C2 longitudinal、C3 consequential judgment、mixed candidate、Quick Control。

Quick Control 是必要反向测试：简单问题不应因为 Candidate Runtime 而变复杂。

## Gate

参考上级 `v0.1.2-test-pack.zh-CN.md`。核心门槛：≥5 users、≥15 episodes、≥80% concrete next action or justified explore/wait/no-action、action cases ≥70% yes/partial follow-through、Mean Clarity Delta >0、Autonomy not worse、Quick lightweight、P0=0、unresolved P1=0。

## Decision Discipline

C1、C2、C3、Full Runtime 分别裁决。允许某 Candidate DOWNGRADE/REMOVE，即使其他 Candidate 通过。
