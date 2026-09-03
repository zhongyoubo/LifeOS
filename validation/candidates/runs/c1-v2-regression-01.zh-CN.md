# C1 v2 Regression 01

> 日期：2026-09-04  
> 类型：Synthetic / Author-environment Regression  
> 对象：Learning Strategy Router v2  
> 基于：C1 Isolation Test 01 findings

## Goal

验证 v2 是否修复：方法重复、Level 实体化、过度诊断、Explore Utility Bias、假精确度，同时保留 Strategy Selection 的增量。

## Regression Matrix

| Case | Target Risk | Result | Notes |
|---|---|---|---|
| L01 30-min AI Agent | Over-diagnosis / Process Cost | PASS | 可直接 `Goal → Strategy → First Action → Check`，无需完整问卷 |
| L02 Architecture Review | Strategy Fit / Evidence | PASS | Target Depth=Analyze/Judge；Success Evidence 明确为架构比较与 tradeoff 判断 |
| L03 Theory Without Practice | Method Duplication | PASS | Router 识别 Skill/Feedback Gap，具体方法交给 Learning System |
| L04 Teach Tomorrow | Deadline Routing | PASS | teach intent + deadline 足以改变策略，保持最小路径 |
| L05 Exam Retention | Existing-method Boundary | PASS | Recall/Spacing 不再被描述为 C1 新能力，只是被 Router 选择 |
| L06 Production Backend | Level Reification | PASS | `Create` 仅是该主题 Target Mastery Depth，不描述用户总体能力 |
| L07 Philosophy Exploration | Utility Bias P1 | PASS | explore intent 有非绩效 Success Evidence，不强制项目化 |

## Guardrail Tests

### R01 — Simple request
输入：“我有 20 分钟，帮我快速理解 CAP 定理。”

预期：不追问完整 Diagnosis；直接选择 Understand + short deadline，给最小学习路径。

Result: **PASS**。

### R02 — User already specifies evidence
输入：“我要学 SQL，目标是两周后能独立写出日常分析查询。我会 SELECT，但 JOIN 和窗口函数不熟。”

预期：不重复询问 target/current/deadline；直接识别 Apply、Skill Gap 和明确 Success Evidence。

Result: **PASS**。

### R03 — Pure curiosity
输入：“我最近对古希腊哲学感兴趣，只是想慢慢理解，没有考试或工作用途。”

预期：Explore；不要求职业 deliverable；允许阅读、比较、问题、写作/对话作为证据。

Result: **PASS**。

### R04 — Mastery-label trap
输入：“我对 Python 是 L2 吗？”

预期：拒绝把 Target Mastery Depth 变成人的固定等级；若要评估能力，应基于具体行为 Evidence。

Result: **PASS**。

### R05 — Method catalogue trap
输入：“这个 Router 有哪些学习方法？”

预期：说明 Router 不拥有 Method Library；方法属于 Learning System，Router 只负责选择何时/为什么使用。

Result: **PASS**。

## Findings

### Fixed

```text
C1-R01 Method Duplication       FIXED
C1-R02 Level Reification       FIXED
C1-R03 Over-diagnosis          FIXED by Minimum Diagnosis
C1-R04 Utility Bias (P1)       FIXED in protocol
C1-R05 False Precision         FIXED by behavioral evidence rule
```

### Remaining Uncertainty

Regression 只能证明协议内部一致性，不能证明真实学习效果。

仍未知：
- 用户是否真的更快进入实践；
- 一周后保持是否更好；
- 是否产生真实 Transfer；
- Assistance 是否会随掌握合理下降；
- 用户是否觉得 Router 的额外结构值得成本。

## Decision

```text
C1 v2 Protocol Regression   PASS
P1 Regression               0 open
Synthetic Design Gate       PASS
Human Evidence Gate         HOLD
Candidate Status            CHANGE → READY FOR HUMAN TEST
```

C1 仍不进入 frozen Core。

## Human Test Minimum

建议至少 5 位用户、10 个真实学习任务，覆盖：
- Quick understanding
- Work judgment
- Skill acquisition
- Exam/retention
- Teaching
- Open exploration

T0：目标、当前状态、时间、预期结果。  
T1：记录 Router 策略与用户实际采用的 First Action。  
T2：24–72h 检查是否开始实践、Strategy Fit、Process Cost。  
T3：7–14d 检查 Success Evidence、保持、迁移、Autonomy。

### Human KEEP Gate

至少观察到：
- 多数任务 Strategy Fit 被用户认为匹配；
- First Practice Action 实际启动率较高；
- Success Evidence 能被真实观察；
- Quick 请求没有明显方法论负担；
- 至少若干案例出现 Transfer 或独立使用；
- 没有系统性 Autonomy 下降。

## Conclusion

C1 v2 已从“学习方法框架”收敛成一个轻量的 **Learning Strategy Selection Protocol**。Synthetic Regression 未发现上一轮 P1/P2 结构问题复发。

下一状态：**READY FOR HUMAN TEST, NOT READY FOR CORE**。
