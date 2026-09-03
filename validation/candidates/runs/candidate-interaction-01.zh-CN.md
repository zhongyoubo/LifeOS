# v0.1.2 Candidate Interaction Test 01

> 日期：2026-09-04  
> 类型：Synthetic / Author-environment Interaction Validation  
> 基线：Frozen LifeOS v0.1.1  
> Candidates：C1 Learning Strategy Router v2 + C2 Capability Growth v2 + C3 Cognitive Augmentation v2  
> 目的：验证候选组合后的职责边界、重复、冲突与 Process Cost；不是 Human Validation。

## 1. Interaction Questions

```text
I01 C1 + C3  学习策略 × 判断校准
I02 C1 + C2  学习策略 × 自适应帮助
I03 C2 + C3  帮助方式 × 判断校准
I04 C1 + C2 + C3 Full Candidate Runtime
```

重点检查：
- routing 是否出现多头决策；
- evidence ownership 是否重复；
- `Calibrate` 命名是否冲突；
- Stop Rule 是否重复；
- 用户是否看到过多框架；
- Full Stack 是否每次都被错误激活。

## 2. I01 — C1 + C3

### Case
用户：
> “我一个月后要参加 AI Agent 架构评审。我知道基本概念，但遇到多 Agent 权限、隔离和记忆设计时容易只凭直觉判断。怎么学？”

### Correct Composition

```text
C1 owns learning routing:
Intent = judge
Target Depth = Analyze/Judge
Gap = Model/Judgment Gap
Use Context = architecture review in one month
Success Evidence = compare architectures and explain tradeoffs
        ↓
C3 may support selected learning activities:
Judgment Calibration
+ Reasoning Lens for permission/isolation/tradeoff cases
        ↓
Existing Learning Loop executes practice
```

### Finding
C1 决定“学什么深度、怎么组织学习”；C3 不应创建第二套学习路线。

**I-F01:** C3 是学习活动中的认知协议，不是 Learning Router 的 peer owner。

Result: **PASS WITH BOUNDARY**。

## 3. I02 — C1 + C2

### Case
第一次用户不会做架构评审；两周后用户已经能自己列出方案、tradeoff、风险，只希望 LifeOS 出练习题并复核判断。

### Correct Composition

```text
C1: learning target / gap / evidence / strategy
C2: how much LifeOS should help this user on this task
```

第一次可能：Guide / Collaborate。

后续观察到独立表现后：Coach / Calibrate。

### Evidence Conflict

C1 的 `Success Evidence` 与 C2 的 `Capability Evidence` 看起来相似，但语义不同：

```text
C1 Success Evidence
= 这次学习目标达到的判定条件

C2 Capability Evidence
= 实际观察到的用户独立行为记录
```

例如：

```text
C1: “能独立比较两个 Agent 架构并说明 tradeoff”
      ↓ later observed
C2: user independently compared A/B, identified isolation risk,
    requested only one blind-spot check
```

**I-F02:** C1 定义 Evidence Contract；C2 保存 Observed Evidence。

Result: **PASS AFTER OWNERSHIP CLARIFICATION**。

## 4. I03 — C2 + C3

### Case
用户已经完成重要职业决策分析，只说：“帮我校准一下有没有盲点。”

### Naming Collision

C2 有 `Calibrate` Assistance Mode；C3 有 `Judgment Calibration Protocol`。

它们不是同一概念：

```text
C2 Calibrate Mode
= HOW MUCH / HOW to assist

C3 Judgment Calibration
= WHAT cognitive operation to run
```

可以组合：

```text
Assistance Mode = Calibrate
Cognitive Operation = Judgment Calibration
```

但命名非常容易让实现和文档混淆。

**I-F03 (P1):** C2 `Calibrate` 建议改名为 `Review` 或 `Check`，避免和 C3 Protocol 同名。

本轮推荐：**Review**。

```text
C2 Modes:
Answer / Guide / Coach / Collaborate / Review / Step Back
```

Result: **CHANGE REQUIRED**。

## 5. Stop Rule Interaction

当前存在：
- Kernel Stop Rule
- C1 Stop Rule
- C3 Action Sufficiency Rule

三者本质都是局部表达：

> 当继续分析/规划的边际价值低于进入行动并获取反馈时，停止。

若各 Candidate 独立拥有 Stop Rule，会产生规则漂移。

**I-F04 (P1):** Stop ownership 必须回到 Kernel。

Candidate 只能定义自己的 readiness signal：

```text
C1 readiness:
learning intent/depth/evidence + first practice action sufficient

C3 readiness:
material uncertainty no longer changes next action

        ↓
Kernel Stop / Continue decides
```

Result: **CHANGE REQUIRED**。

## 6. Evidence Ownership Model

Interaction 后建议统一为：

```text
C1  defines Target Evidence
    “What would demonstrate this learning goal?”

C3  produces Judgment Evidence / Candidate Lesson
    “What changed the judgment? What lesson may transfer?”

C2  owns Contextual Capability Evidence
    “What did the user actually do independently over time?”

Kernel / Review owns Outcome Evidence
    “What happened after action?”
```

**I-F05:** Evidence 需要分类型 ownership，不能每个 Candidate 自建 evidence store。

## 7. I04 — Full Candidate Runtime

### Complex Case
用户：
> “三个月后我要第一次负责跨国项目。我想系统学习项目领导能力，但我上次项目失败后一直怀疑自己不适合当负责人。帮我制定方案。”

### Naive Full Stack
若机械运行：

```text
C1 diagnosis
+ C2 assistance selection
+ C3 full calibration
+ mental models
+ learning map
+ capability evidence
+ transfer lesson
+ multiple stop checks
```

用户会被 LifeOS 架构本身淹没。

### Correct Runtime

```text
1 Kernel determines Standard/Deep
2 Diagnose: learning + identity judgment both material
3 C2 silently selects assistance mode
4 C3 calibrates only the harmful identity inference
5 C1 selects learning strategy
6 Core Learning executes first practice cycle
7 Kernel returns concrete next action + checkpoint
8 Later Review records outcome
9 C2 updates capability evidence only after behavior exists
```

用户不需要看到 C1/C2/C3 名称。

**I-F06:** Candidates 必须是后台协议，不是用户可见的三个模块。

Result: **PASS ONLY WITH ORCHESTRATION**。

## 8. Full-stack Quick Case

用户：
> “我有 15 分钟，快速告诉我什么是 Opportunity Cost。”

正确行为：

```text
Quick Runtime
→ C1 lightweight route: Understand
→ C2 Answer/Guide
→ C3 OFF unless misconception appears
→ explain + example + quick check
→ stop
```

不能运行 Full Stack。

**I-F07:** Candidate activation must be sparse, not additive.

Result: **PASS WITH SPARSE ACTIVATION**。

## 9. Unified Candidate Runtime Proposal

Interaction Test 后最合理的 v0.1.2 runtime 不是：

```text
Kernel
→ C1
→ C2
→ C3
→ Core
```

而是：

```text
Situation
   ↓
Kernel
├─ Runtime Level
├─ Problem Diagnosis
├─ Stop / Continue ownership
├─ Core Router
└─ Candidate Trigger Router
       │
       ├─ Learning task? ─────→ C1 Strategy Selection
       ├─ Assistance context? → C2 Assistance Selection
       └─ Judgment risk? ─────→ C3 Cognitive Operation
                                ↓
                         Core OS execution
                                ↓
                         Action / Feedback
                                ↓
                              Review
                                ↓
                         Evidence Update
```

C1/C2/C3 是 **orthogonal protocols**，按需触发，不构成串行架构层。

## 10. Required Changes

### P1 — C2 Calibrate naming collision

```text
Calibrate → Review
```

建议未来 C2：

```text
Answer
Guide
Coach
Collaborate
Review
Step Back
```

### P1 — Stop ownership duplication

C1/C3 不拥有独立 Stop Rule。

改为：

```text
Candidate Readiness Signals
→ Kernel Stop Rule
```

### P2 — Evidence ownership ambiguity

统一：

```text
Target Evidence       → C1
Judgment Evidence     → C3
Capability Evidence   → C2
Outcome Evidence      → Review / Kernel lifecycle
```

### P2 — Candidate visibility

默认不向用户显示 C1/C2/C3 内部名称、Mode 或字段。

### P2 — Additive activation risk

Candidate Trigger Router 必须允许：

```text
0 candidate
1 candidate
2 candidates
rarely 3 candidates
```

而不是每个 Standard/Deep 请求全开。

## 11. Interaction Results

| Test | Result |
|---|---|
| I01 C1 + C3 | PASS WITH BOUNDARY |
| I02 C1 + C2 | PASS AFTER OWNERSHIP CLARIFICATION |
| I03 C2 + C3 | CHANGE REQUIRED |
| I04 Full Stack | PASS ONLY WITH ORCHESTRATION |
| Quick Full-stack guardrail | PASS WITH SPARSE ACTIVATION |

Open issues：

```text
P1 = 2
P2 = 3
P0 = 0
```

## 12. Candidate Decision

三个 Candidate 单体仍保持 Design PASS，但组合层当前不是直接 KEEP：

```text
C1  DESIGN PASS
C2  DESIGN PASS / naming change required
C3  DESIGN PASS

Interaction Architecture = CHANGE
```

## 13. Next Build

下一步不是继续增加测试案例，而是生成一个统一的：

```text
v0.1.2 Candidate Runtime Proposal
```

它只定义：
- Kernel ownership；
- Candidate Trigger Router；
- C1/C2/C3 boundaries；
- evidence ownership；
- readiness → Kernel Stop；
- sparse activation；
- internal vs user-visible output。

然后用 I01–I04 做 Interaction Regression。

## 14. Conclusion

Interaction Test 证明 C1/C2/C3 可以共存，但**不能作为三个串行新层加入 LifeOS**。

更合理的结构是：

> **Kernel remains the single orchestrator; C1, C2 and C3 are orthogonal, sparsely triggered protocols with explicit ownership boundaries.**

这保持 LifeOS 的稳定中心：

```text
Models + Kernel + Core OS
```

而不是让 v0.1.2 演化成新的框架堆叠。
