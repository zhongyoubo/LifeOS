# LifeOS Framework Specification v0.1.1

[English](./spec-v0.1.md) | **简体中文**

> **认识自己 · 驾驭人生 · 持续进化**

LifeOS 是一套开源的个人认知、情境理解、判断、行动、学习与成长操作系统。它不定义唯一正确的人生。

## 1. 规范结构

```text
Foundation Models
Self / Context / Role / Goal
        ↓
Kernel Runtime
Quick / Standard / Deep
        ↓
Core OS
Thinking / Decision / Communication / Execution / Learning / Emotion & Energy / Review
        ↓
Optional Domain Layer
Playbooks / Methods / Tools / Templates
        ↓
Action → Feedback → Review → Evolution
```

LifeOS 的稳定核心是 **Models + Kernel + Core OS**。领域层必须证明增量价值，不能因为形式完整而存在。

## 2. 四大基础模型

### Self Model
动态、可修改、尽量基于证据地维护价值、需求、优势、局限、模式、资源、关系、责任、人生阶段和当前状态。重要自我判断应记录 evidence、counterevidence、confidence、source contexts 和 review date。

### Context Model

```text
Context = Role + Goal + People + Rules + Resources + Constraints + Risks + Time
```

### Role Model
定义 Purpose、Responsibilities、Authority、Expectations、Relationships、Boundaries、Outcomes、Risks。Runtime 应显式检查 Responsibility / Authority Gap，避免把结构性权限或资源问题误判为个人执行问题。

### Goal Model
支持四种模式：

- `explore`：证据不足，先通过小实验获取信息；
- `commit`：信息足够，进入明确承诺与里程碑；
- `maintain`：维持当前有效状态；
- `exit`：有意识停止或退出不再值得继续投入的承诺。

没有长期方向，不等于必须立即设长期目标。探索本身可以是正确模式。

## 3. Kernel Runtime

```text
选择 Runtime Level
→ Observe
→ Clarify
→ Load Models
→ 区分 Facts / Interpretations / Assumptions / Values / Unknowns
→ Diagnose
→ Route Core OS
→ Optional Domain Support
→ Next Action
→ Checkpoint / Revisit Condition
→ Review
→ Evidence-based Update
```

### Runtime Levels

**Quick**：低影响、低风险、可逆。  
**Standard**：普通工作和人生问题，存在必要上下文和依赖。  
**Deep**：高影响、高未知、高风险或难逆。

原则：只使用当前问题真正需要的最小深度。

## 4. 七大 Core OS

- **Thinking / 思考**：把信息变成更可靠的问题模型。
- **Decision / 决策**：在取舍中形成可解释、可修正的选择。
- **Communication / 沟通**：建立足够共同理解与协同。
- **Execution / 执行**：把选择转化为可观察结果。
- **Learning / 学习**：把未知转化为可迁移能力。
- **Emotion & Energy / 情绪与能量**：管理影响判断和行动的真实运行状态。
- **Review / 复盘**：把经历转化为可验证的 Lesson 和系统更新。

## 5. 方法论层级

```text
Principle → Process → Method → Tool → Template
```

Method 是插件，不应把 LifeOS 变成方法大全。

## 6. Optional Domain Playbooks

Playbook 不再是强制架构层。只有当它比 Kernel 多提供明显的领域特有顺序、检查项、输出物或认知成本降低时，才允许独立存在。

详见 [Playbook Admission Rule](./playbook-admission.zh-CN.md)。

当前分类：

- Complex Problem → Kernel / Thinking Pattern
- Important Decision → Decision System + Template
- New Role / Environment → Trial Playbook
- Unfamiliar Project → Validated Domain Playbook
- Important Disagreement → Trial Playbook
- New Domain Learning → Validated Domain Playbook
- Failure Recovery → Validated Domain Playbook

## 7. Evolution / 进化

```text
Experience → Review → Evidence → Lesson → Change → Verify → Update
```

更新可以影响 Self / Role / Goal、Principles、Methods、Personal Patterns 或 Domain Playbooks。重要 Self 更新必须通过 Evidence Gate。

## 8. AI Native LifeOS

```text
User Situation
→ Runtime Level Router
→ Model Loader
→ Problem Diagnosis
→ Core OS Router
→ Optional Domain Router
→ Decision / Communication / Next Action
→ Checkpoint
→ Review & Update
```

AI 必须暴露重要不确定性、区分事实与推断、保留用户自主性、不替用户定义价值，并避免不必要的框架负担。

## 9. Validation Status

当前 Synthetic Framework Validation 已经完成 20/20 标准场景，未发现 P0 阻塞。这证明当前架构具备内部可运行性，但还不能证明真实使用中一定优于优秀通用 AI。

下一道 Release Gate 是 Blind / Human A/B Validation。

## 10. v0.1.1 完成定义

v0.1.1 是验证驱动后的架构基线，包括：

- 四个具备证据意识的 Foundation Models；
- Quick / Standard / Deep Kernel Runtime；
- 七大 Core OS；
- 可选、证据驱动准入的 Domain Playbooks；
- Principle → Template 方法论层级；
- 双语 AI Skill；
- Validation / Regression Protocol；
- 可用于 Blind A/B Evaluation 的冻结基线。
