# LifeOS

> **认识自己 · 驾驭人生 · 持续进化**
>
> **Know Yourself · Navigate Life · Evolve Yourself**

[English](README.md) | [简体中文](README.zh-CN.md)

LifeOS 是一套开源的个人认知、情境理解、判断、行动、学习与持续成长操作系统。

## 从这里开始

- [Framework Specification v0.1.1](docs/spec-v0.1.zh-CN.md)
- [总体架构 v0.1.1](docs/architecture.zh-CN.md)
- [Operating Protocol / Kernel Runtime](docs/operating-protocol.zh-CN.md)
- [四大基础模型](models/)
- [七大 Core OS](core/README.zh-CN.md)
- [Playbook Admission Rule](docs/playbook-admission.zh-CN.md)
- [核心模板](templates/README.zh-CN.md)
- [LifeOS Skill v0.1.1](skills/lifeos/SKILL.md)
- [Validation](validation/README.zh-CN.md)
- [Roadmap](ROADMAP.zh-CN.md)

## 规范架构

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

LifeOS 的稳定核心是 **Models + Kernel + Core OS**。Domain Playbook 只是可选层，必须证明自己有增量价值。

## 四大基础模型

- **Self / 自我**：我是谁，什么重要，我当前有哪些模式和资源？
- **Context / 情境**：我正在什么环境中运行，哪些人、规则、资源、约束和风险重要？
- **Role / 角色**：我承担什么责任，实际拥有多少权限，边界是什么？
- **Goal / 目标**：当前是在探索、承诺、维持还是退出，我下一步需要什么结果或信息？

## 七大 Core OS

- Thinking / 思考
- Decision / 决策
- Communication / 沟通
- Execution / 执行
- Learning / 学习
- Emotion & Energy / 情绪与能量
- Review / 复盘

## 设计原则

1. LifeOS 不定义唯一正确的人生。
2. LifeOS 帮助人思考，而不是替人做人生决定。
3. 必要时明确区分事实、解释、假设、价值与未知。
4. 只使用当前问题真正需要的最小框架深度。
5. 稳定流程比收集大量方法更重要。
6. 行动必须产生反馈与学习。
7. Self Model 始终可修改，并尽量以证据为基础。
8. 结构性情境问题不能被误判为个人缺陷。
9. Playbook 必须证明领域特有价值，才能成为稳定框架资产。
10. 最终目标是增强人的自主性，而不是增强对 LifeOS 的依赖。

## Validation 状态

LifeOS 已完成 20 个标准场景的 Synthetic Framework Validation，未发现 P0 阻塞。这支持“框架内部可运行”，但还不能证明真实使用一定优于优秀通用 AI。

当前状态：

```text
Framework Gate        PASS
Public Validation     HOLD
```

下一道门槛是 Blind / Human A/B Validation。

## 双语原则

中文和英文都是 LifeOS 的一等语言。核心概念与主要规范保持语义一致。

- 英文默认：`document.md`
- 简体中文：`document.zh-CN.md`

## 项目结构

```text
LifeOS/
├── docs/          # 架构、规范、Kernel、准入规则
├── models/        # Self / Context / Role / Goal
├── core/          # 七大 Core OS
├── templates/     # 可复用执行模板
├── playbooks/     # 可选领域 Playbooks
├── skills/lifeos/ # AI Runtime Skill
├── validation/    # 场景、评分、回归、A/B 协议
└── examples/
```

## 当前阶段

**v0.1.1 — Validation-driven Architecture Baseline / 验证驱动架构基线**

当前框架已冻结到足以进行 Blind External Evaluation 的状态，在此之前不建议继续扩充方法或 Playbook 数量。

## License

除特别说明外，LifeOS 使用 MIT License。
