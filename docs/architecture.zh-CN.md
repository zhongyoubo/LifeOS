# LifeOS 总体架构 v0.1.1

[English](./architecture.md) | **简体中文**

LifeOS 是一套可复用的个人操作系统，而不是固定的人生说明书。

## 1. 规范架构

```text
                     LifeOS
                       │
        ┌──────────────┼──────────────┐
        │              │              │
     MODELS          KERNEL        CORE OS
      模型层          运行内核        能力系统
        │              │              │
 Self / Context   Runtime Level   Thinking
 Role / Goal      Observe         Decision
                  Clarify         Communication
                  Diagnose        Execution
                  Route           Learning
                  Act             Emotion & Energy
                  Review          Review
        │              │              │
        └──────────────┴──────────────┘
                       ↓
               OPTIONAL DOMAIN LAYER
                    可选领域层
                       │
          Playbooks / Methods / Templates
                       ↓
                    现实行动
                       ↓
                 Experience / Feedback
                       ↓
                   模型与系统进化
```

LifeOS 的稳定核心是：**Models + Kernel Runtime + Core OS**。Playbook 不再属于强制内核，而是按需加载的领域加速层。

## 2. 四大基础模型

- **Self**：我是谁、什么重要、我有哪些模式与资源。
- **Context**：当前有哪些人、规则、资源、约束、风险和时间条件。
- **Role**：我承担什么责任、实际拥有多少权限、边界在哪里。
- **Goal**：当前是 explore / commit / maintain / exit 哪一种模式，下一步需要什么结果或信息。

模型必须允许修改，并尽量以证据为基础，而不是永久标签。

## 3. Kernel Runtime

Kernel 是必须存在的统一运行协议：

```text
选择运行深度
→ Observe 观察
→ Clarify 澄清
→ Load Models 加载模型
→ 区分 Fact / Interpretation / Assumption / Value / Unknown
→ Diagnose 诊断
→ Route Core OS 路由能力系统
→ 形成 Next Action
→ Checkpoint
→ Review
→ Update
```

Runtime 使用 Quick / Standard / Deep 三种深度，根据影响、未知、风险和不可逆程度选择。

## 4. 七大 Core OS

1. Thinking / 思考
2. Decision / 决策
3. Communication / 沟通
4. Execution / 执行
5. Learning / 学习
6. Emotion & Energy / 情绪与能量
7. Review / 复盘

Core OS 是跨工作、关系、学习、角色变化和人生决策复用的底层能力。

## 5. Optional Domain Layer / 可选领域层

Playbook、Method、Tool、Template 都是可选层。它们必须降低认知或执行成本，而不是重复 Kernel。

```text
Kernel Runtime
   ↓
是否存在领域特有的顺序 / 检查项 / 输出？
   ├─ 否 → 直接使用 Core OS
   └─ 是 → 加载 Optional Playbook
```

Playbook 只有在提供通用 Runtime 无法直接表达的领域特有价值时，才值得独立存在。

当前验证中独立价值较明确的包括：

- 接手陌生项目；
- 在限定时间内学习陌生领域；
- 重要失败后的恢复与复盘。

“面对复杂问题不知道怎么办”这类高度通用流程，通常更适合作为 Kernel / Thinking Pattern，而不是独立 Playbook。

详见 [Playbook Admission Rule](./playbook-admission.zh-CN.md)。

## 6. Evolution / 进化机制

```text
Experience
→ Review
→ Evidence
→ Lesson
→ Change
→ Verify
→ 更新 Self / Role / Goal / Principles / Methods / Playbooks
```

重要 Self Model 更新必须通过 Evidence Gate。一次成功或失败不应直接变成人格或能力标签。

## 7. 个性化

```text
Default LifeOS
      ↓
My Models
My Principles
My Methods
My Domain Playbooks
My Experiences
My Lessons
      ↓
My LifeOS
```

目标是提高人的判断力、自主性和能力，而不是让人依赖框架。

## 8. AI Native Runtime

```text
User Situation
      ↓
Runtime Level Router
      ↓
Foundation Model Loader
      ↓
Problem Diagnosis
      ↓
Core OS Router
      ↓
Optional Domain Router
      ↓
Next Action / Decision / Communication
      ↓
Checkpoint
      ↓
Review & Evidence-based Update
```

AI 的定位是增强判断。它必须暴露重要不确定性，不能替用户定义价值，并且只使用解决当前问题所需的最小框架深度。
