# v0.1.2 Candidate Interaction Regression 01

> 日期：2026-09-04  
> 类型：Synthetic / Author-environment Regression  
> 对象：Unified Candidate Runtime Proposal  
> 基于：`candidate-interaction-01.zh-CN.md`

## Goal

验证 Interaction Test 01 的 2 个 P1、3 个 P2 是否被统一 Runtime 修复，并重新运行 I01–I04 与 sparse activation guardrails。

## I01 — C1 + C3

学习 AI Agent 架构评审，同时需要改善多 Agent 权限/隔离等判断。

Expected：C1 owns learning route；C3 只在具体 judgment practice 中提供 calibration/lens；Kernel orchestrates。

Result: **PASS**。

未出现第二套 learning route。

## I02 — C1 + C2

用户从第一次不会评审，到后续能独立列方案/tradeoff，只需练习和复核。

Expected：C1 定义 Target Evidence；C2 记录实际 Capability Evidence 并选择 assistance。

Result: **PASS**。

```text
Target Evidence → C1
Observed Capability Evidence → C2
```

语义不再重复。

## I03 — C2 + C3

用户完成职业决策主体分析，只要求检查盲点。

Expected：

```text
C2 Assistance Mode = Review
C3 Cognitive Operation = Judgment Calibration
```

Result: **PASS**。

原 `Calibrate / Calibration` 命名冲突消失。

## I04 — Full Candidate Runtime

用户三个月后第一次负责跨国项目，同时存在学习目标和“上次失败证明自己不适合负责”的身份判断。

Expected：Kernel 识别 mixed problem；C2 silent assistance selection；C3 只校准身份推断；C1 组织学习；Core 执行；Kernel stop；Review 后才更新 evidence。

Result: **PASS**。

未要求用户理解 Candidate 架构。

## Sparse Activation Regression

| Case | Expected | Result |
|---|---|---|
| 简单事实问答 | 0 candidate / Core Answer | PASS |
| 15 分钟理解概念 | C1 lightweight；C2 可隐式；C3 off | PASS |
| 已完成重要决策求盲点 | C2 Review + C3 | PASS |
| 新领域高风险选择 | C2 + C3；C1 off | PASS |
| 长期技能学习 | C1 + C2；C3 only when judgment task requires | PASS |
| 复杂学习 + 身份错误归因 | C1 + C2 + C3 justified | PASS |

Full activation 只在最后一类 genuinely mixed case 中出现。

## Stop Ownership Regression

### Before

```text
Kernel Stop Rule
C1 Stop Rule
C3 Action Sufficiency Rule
```

### After

```text
C1 readiness ─┐
C3 readiness ─┼→ Kernel Stop / Continue
Core state ───┤
Risk ─────────┘
```

Result: **PASS**。

Candidate 不再拥有全局 Stop Rule。

## Evidence Ownership Regression

```text
Target Evidence             C1
Judgment Evidence           C3
Candidate Transfer Lesson   C3
Capability Evidence         C2
Outcome Evidence            Review / lifecycle
```

Checks：
- learning success criterion does not automatically become capability evidence → PASS
- AI-created transfer lesson does not become transfer evidence → PASS
- predicted judgment outcome does not become real outcome evidence → PASS
- C2 does not infer global capability from one result → PASS

## User Visibility Regression

测试用户普通请求时是否暴露：C1/C2/C3、Assistance Mode、Trigger Router、Evidence Store。

Expected：默认不暴露。

Result: **PASS**。

用户要求“解释 LifeOS 为什么这样处理”时可以显式解释内部机制。

## Process Cost Guardrail

高风险：统一 Runtime 可能成为新的巨大 checklist。

Guardrail：Kernel 只执行改变当前 route/action 的判断；Candidate activation 不是逐项问卷。

Synthetic cases：
- simple factual → no added visible steps
- quick learning → only minimal C1 output
- ordinary decision → no Candidate unless material trigger
- complex mixed → internal orchestration, consolidated user output

Result: **PASS at protocol level**。

真实用户 Process Cost 仍需 Human Validation。

## Issue Closure

```text
P1-1 C2 Calibrate naming collision   CLOSED → Review
P1-2 Stop ownership duplication      CLOSED → Kernel only
P2-1 Evidence ownership ambiguity    CLOSED
P2-2 Candidate visibility            CLOSED
P2-3 Additive activation risk        CLOSED → sparse triggers

P0 open = 0
P1 open = 0
P2 open = 0 at protocol regression
```

## Architecture Decision

Interaction Regression 支持：

```text
Foundation Models
      ↓
Kernel Runtime
      ↓
Core OS
      ↓
Action / Feedback / Review
```

并在 Kernel 内加入候选级的：

```text
Candidate Trigger Router
├─ C1 Learning Strategy
├─ C2 Assistance Selection
└─ C3 Cognitive Operation
```

注意：这仍是 **v0.1.2 Candidate Proposal**，不是 frozen architecture 的正式修改。

## Candidate Status

```text
C1 Design Regression          PASS
C2 Design Regression          PASS
C3 Design Regression          PASS
Interaction Regression       PASS
P0                            0
P1                            0
Synthetic Candidate Gate     PASS
Human Evidence Gate          HOLD
```

## What Is Now Frozen for Human Test

为避免继续移动目标，建议 Human Validation 期间冻结以下 candidate semantics：

```text
C1 = Learning Strategy Selection
C2 = Assistance Selection + Contextual Capability Evidence
C3 = Judgment Calibration + Reasoning Lens + Transfer Lesson
Kernel = Single Orchestrator + Stop Owner
Activation = Sparse
Evidence = Explicit Ownership
User Output = Problem-first, architecture-hidden
```

除 P0/P1 外，不在 Human Test 中途继续扩展 Candidate。

## Next Gate

现在不应该继续增加认知协议。

下一步：

```text
Candidate Runtime Freeze
        ↓
Human Validation Pack v0.1.2
        ↓
Real users / real problems
        ↓
Outcome + Process + Autonomy + Transfer evidence
        ↓
KEEP / CHANGE / DOWNGRADE / REMOVE
        ↓
v0.1.2 Candidate Build
```

Human Validation 应同时覆盖：
- C1 real learning tasks；
- C2 longitudinal repeated interactions；
- C3 consequential judgments；
- mixed interaction cases；
- Quick controls，确认没有 Process Cost regression。

## Conclusion

统一 Candidate Runtime 已通过 synthetic Interaction Regression。三个 Candidate 不再表现为三个新层，而成为 Kernel 稀疏调度的正交协议。

当前结论：**SYNTHETIC CANDIDATE GATE PASS — READY TO FREEZE FOR HUMAN VALIDATION, NOT READY FOR CORE ADMISSION.**
