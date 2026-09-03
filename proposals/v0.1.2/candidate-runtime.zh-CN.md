# v0.1.2 Candidate — Unified Runtime Proposal

[English](./candidate-runtime.md) | **简体中文**

> 状态：**PROPOSAL / NOT PART OF FROZEN v0.1.1**  
> 依据：`validation/candidates/runs/candidate-interaction-01.zh-CN.md`  
> 目标：整合 C1 / C2 / C3，而不改变 LifeOS 的稳定中心。

## 1. Architecture Principle

v0.1.2 不新增三个串行架构层。

稳定中心继续保持：

```text
Foundation Models
      ↓
Kernel Runtime
      ↓
Core OS
      ↓
Action / Feedback / Review
```

C1、C2、C3 是由 Kernel 稀疏触发的正交协议：

```text
Situation
   ↓
Kernel
├─ Runtime Level
├─ Problem Diagnosis
├─ Foundation Model Loader
├─ Core Router
├─ Candidate Trigger Router
└─ Stop / Continue Owner
       │
       ├─ C1 Learning Strategy Selection
       ├─ C2 Assistance Selection
       └─ C3 Cognitive Operation
              ↓
           Core OS
              ↓
        Action / Feedback
              ↓
            Review
              ↓
        Evidence Update
```

## 2. Single Orchestrator Rule

**Kernel 是唯一 orchestrator。**

Candidate 不得：
- 相互直接调用形成新的固定流水线；
- 自己决定 Runtime Level；
- 自己拥有全局 Stop Rule；
- 创建独立用户画像；
- 绕过 Core OS 直接成为顶层系统。

## 3. Candidate Trigger Router

Candidate activation 必须 sparse：

```text
0 candidate   normal/simple Core flow
1 candidate   common
2 candidates  when genuinely cross-cutting
3 candidates  rare
```

### C1 Trigger

当问题的主要目标包含学习、理解、掌握、练习、保持、教学或形成某领域判断能力时触发。

C1 owns：

```text
Intent
Target Mastery Depth
Current Gap
Deadline / Use Context
Target Success Evidence
Minimum Useful Learning Strategy
```

### C2 Trigger

当“LifeOS 应该帮多少、帮哪部分”会显著影响 Outcome、Autonomy 或 Process Cost 时触发。

C2 owns：

```text
Assistance Selection
Contextual Capability Evidence
Observed Independent Portion
Future Assistance Adaptation
```

Assistance Modes：

```text
Answer
Guide
Coach
Collaborate
Review
Step Back
```

`Review` 替代旧 `Calibrate`，避免与 C3 Judgment Calibration 命名冲突。

### C3 Trigger

当以下因素具有实质意义时触发：

```text
Impact
Uncertainty
Risk
Irreversibility
Strong confidence with weak evidence
Repeated reasoning failure
Identity-level conclusion from limited evidence
```

C3 owns：

```text
Judgment Calibration
Reasoning Lens Selection
Candidate Transfer Lesson
```

## 4. Orthogonality

三个 Candidate 回答不同问题：

```text
C1: How should this learning task be approached?
C2: How much / what kind of help should LifeOS provide?
C3: What cognitive operation would improve this judgment?
```

组合时不复制对方职责。

例：用户学习架构评审：

```text
C1 → define learning strategy
C2 → choose Guide/Coach/Review based on current performance
C3 → only calibrate high-value architecture judgments
```

## 5. Evidence Ownership

统一 Evidence 语义：

| Evidence Type | Owner | Meaning |
|---|---|---|
| Target Evidence | C1 | 什么行为/结果代表本次学习目标达到 |
| Judgment Evidence | C3 | 什么证据支持、削弱或改变当前判断 |
| Candidate Transfer Lesson | C3 | 可能值得未来迁移的原则/触发/边界 |
| Capability Evidence | C2 | 用户实际独立完成了什么，以及后续是否迁移 |
| Outcome Evidence | Review / lifecycle | 行动之后真实发生了什么 |

规则：

```text
Target Evidence ≠ Capability Evidence
Transfer Lesson ≠ Transfer Evidence
Judgment Evidence ≠ Outcome Evidence
```

Candidate 不创建独立 Evidence Store；实现层应使用统一 Evidence Model / lifecycle。

## 6. Stop Ownership

只有 Kernel 拥有全局 Stop / Continue 决策。

Candidate 只返回 readiness signal。

### C1 Readiness

```text
Intent/depth sufficient
+ target evidence defined
+ first feedback-producing practice action available
```

### C3 Readiness

```text
material judgment sufficient
+ remaining uncertainty unlikely to change next action
+ material irreversible downside addressed
```

Kernel 综合：

```text
Problem clarity
Risk / reversibility
Candidate readiness
Next action availability
Expected value of more analysis
Expected feedback value from action
        ↓
STOP / CONTINUE
```

核心原则：

```text
Marginal Value of More Analysis
< Feedback Value from Action
→ ACT
```

## 7. Runtime Sequence

```text
1. Select Runtime Level
2. Observe / clarify real problem
3. Load Self / Context / Role / Goal as needed
4. Separate material facts / interpretations / assumptions / unknowns
5. Diagnose problem type
6. Route to Core OS
7. Evaluate Candidate Triggers
8. Activate minimum necessary candidate protocols
9. Execute through Core OS
10. Kernel evaluates Stop / Continue
11. Produce concrete next action + checkpoint
12. Observe outcome when available
13. Review
14. Update evidence through explicit ownership rules
```

Candidate activation is step 7–8, not a mandatory new layer before Core.

## 8. User-visible Output Rule

默认隐藏：
- `C1 / C2 / C3` 名称；
- Assistance Mode 名称；
- Trigger Router；
- Evidence ownership；
- internal readiness fields。

用户应该看到问题本身的解决过程，而不是 LifeOS 内部架构。

只有以下情况才显式展示方法：
- 用户要求学习方法；
- 方法名称有助于未来迁移；
- 解释机制能显著提高判断质量；
- 用户正在设计/调试 LifeOS 本身。

## 9. Quick Runtime Guardrail

Quick 请求默认：

```text
Core first
→ candidate only if clearly useful
→ minimum output
→ act / answer / check
→ stop
```

禁止为了 Capability Growth 或 Cognitive Augmentation 强制增加问卷、反思或模型教学。

## 10. Full Candidate Example

用户：
> “三个月后我要第一次负责跨国项目。我想系统学习项目领导能力，但上次项目失败后一直怀疑自己不适合当负责人。”

内部：

```text
Kernel: Standard/Deep; mixed learning + identity judgment
C2: Guide/Collaborate based on current evidence
C3: calibrate only the unsupported identity inference
C1: select project-leadership learning strategy
Core Learning/Thinking/Decision: execute
Kernel: stop when first useful action is ready
Review: later collect outcome
C2: update capability evidence only after observed behavior
```

用户侧不需要看到三个 Candidate。

## 11. Conflict Resolution Priority

发生冲突时：

```text
Safety / material risk
> explicit user goal and values
> Kernel architecture rules
> current-task evidence
> candidate protocol preference
> historical inference
```

Candidate 永远不能因为自己的“成长目标”覆盖用户真实 Outcome Value。

## 12. Version Boundary

本文件只定义 v0.1.2 Candidate Runtime。

在 Human Validation 前：
- 不修改 frozen v0.1.1 Core；
- 不把 Candidate 写入稳定架构；
- 不宣称 Human Capability 已被证明；
- 不建立大规模 Mental Model Library；
- 不提前实现 Personal Agent / long-term personalization runtime。

## 13. Validation Gate

进入 Candidate Build 前至少需要：

```text
Interaction Regression I01–I04 PASS
P0 = 0
P1 = 0
No systematic Process Cost regression
Sparse activation works
Evidence ownership remains unambiguous
Kernel remains single orchestrator
```

之后进入 Human Validation，而不是继续扩张理论。
