# LifeOS

> **认识自己 · 驾驭人生 · 持续进化**
>
> **Know Yourself · Navigate Life · Evolve Yourself**

[English](README.md) | [简体中文](README.zh-CN.md)

LifeOS 是一套开源的人生自我管理与成长操作系统，帮助人认识自己、理解所处环境、清晰思考、做出决策、有效沟通、付诸行动，并通过持续学习与复盘不断成长。

LifeOS 不定义什么才是“成功的人生”。它更关注帮助每个人建立一套可复用的方法，用来寻找属于自己的答案。

## 从这里开始

- [LifeOS Framework Specification v0.1](docs/spec-v0.1.zh-CN.md)
- [总体架构](docs/architecture.zh-CN.md)
- [Operating Protocol / Kernel Runtime](docs/operating-protocol.zh-CN.md)
- [四大基础模型](models/)
- [七大 Core OS](core/README.zh-CN.md)
- [核心模板](templates/README.zh-CN.md)
- [7 个 Golden Playbooks](playbooks/golden-playbooks.zh-CN.md)
- [LifeOS Skill v0.1](skills/lifeos/SKILL.md)
- [端到端示例](examples/README.zh-CN.md)
- [Roadmap](ROADMAP.zh-CN.md)

## 愿景

构建一套开放、可实践、可演进的方法论与个人操作系统，帮助人：

- 更清楚地认识自己；
- 理解角色、目标、环境、约束与资源；
- 结构化地思考与决策；
- 更有效地沟通与协作；
- 将意图真正转化为行动；
- 从经验中持续学习；
- 通过复盘、调整与反馈实现长期成长。

## 核心循环

```text
现实情境
   ↓
Self + Context + Role + Goal
   ↓
思考
   ↓
决策
   ↓
沟通
   ↓
行动
   ↓
观察结果
   ↓
复盘
   ↓
学习
   ↓
进化
```

## LifeOS 总体架构

LifeOS 由四个基础模型、Core OS 和场景执行层组成：

1. **Self / 自我** —— 我是谁？我重视什么？我的优势、限制、需要、责任和当前状态是什么？
2. **Context / 情境** —— 我正在什么环境中运行？涉及哪些人、规则、资源、约束、风险和时间条件？
3. **Role / 角色** —— 在当前情境下我是谁？负责什么？权限和边界是什么？
4. **Goal / 目标** —— 我希望发生什么变化？为什么重要？怎样算完成？
5. **Core OS / 核心运行系统** —— 思考、决策、沟通、执行、学习、情绪与能量、复盘。
6. **Playbooks / 场景方案** —— 针对典型真实问题，通过 LifeOS 内核形成可执行路径。

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
3. 明确区分事实、假设、价值判断与决策。
4. 稳定流程比堆积大量方法论更重要。
5. 每一个框架最终都应该能够支持行动。
6. 每一次行动都应该产生反馈与学习。
7. Self Model 是动态的，永远允许修改。
8. LifeOS 应随着使用不断个性化。
9. 角色可以变化，但底层操作系统应保持可复用。
10. 最终目标是增强人的自主性，而不是让人依赖 LifeOS。

## 双语原则

中文和英文都是 LifeOS 的一等语言。核心概念、模型、规范、模板和主要 Playbook 应在中英文之间保持语义一致，而不是把其中一种语言仅作为附属翻译。

文件命名约定：

- 英文默认文件：`document.md`
- 简体中文文件：`document.zh-CN.md`

LifeOS Skill 默认自动跟随用户输入语言输出。

## 项目结构

```text
LifeOS/
├── README.md / README.zh-CN.md
├── ROADMAP.md / ROADMAP.zh-CN.md
├── docs/
│   ├── spec-v0.1.*
│   ├── architecture.*
│   └── operating-protocol.*
├── models/
│   ├── self-model.*
│   ├── context-model.*
│   ├── role-model.*
│   └── goal-model.*
├── core/
│   ├── thinking.*
│   ├── decision.*
│   ├── communication.*
│   ├── execution.*
│   ├── learning.*
│   ├── emotion-energy.*
│   └── review.*
├── templates/
├── playbooks/
├── skills/lifeos/
└── examples/
```

## 当前阶段

**v0.1 — Foundation / 可运行基础框架**

当前已经具备：四大基础模型、七大 Core OS、Kernel Runtime、核心模板、7 个 Golden Playbooks、双语 AI Skill，以及第一批端到端验证示例。

下一阶段重点不再是继续堆内容，而是用更多真实人生和工作场景验证整个 Runtime，识别系统重叠、边界缺失和 Schema 不足，再进入方法库与 Playbook 扩展。

## License

除特别说明外，LifeOS 使用 MIT License。
