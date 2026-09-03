# LifeOS Validation / 验证体系

[English](./README.md) | **简体中文**

LifeOS Validation 用真实问题验证框架是否能够稳定地把用户从“我不知道怎么办”带到“我理解问题，并知道合理的下一步”。

## 验证目标

验证的不是 LifeOS 是否能给出漂亮答案，而是：

1. 是否真正澄清问题；
2. 是否正确使用 Self / Context / Role / Goal；
3. 是否路由到合适的 Core OS；
4. 是否产生新的、有价值的洞察；
5. 是否帮助形成判断而不是替用户决定；
6. 是否产生具体且合理的 Next Action；
7. 是否能够通过 Review 形成学习与模型更新；
8. 相比普通 AI 是否存在明显结构性价值。

## 验证流程

```text
Scenario
  ↓
Baseline AI Run
  ↓
LifeOS Run
  ↓
Score 6 Dimensions
  ↓
Compare
  ↓
Record Failure Modes
  ↓
Framework Fix
  ↓
Regression Run
```

## Runtime Level

### Quick
低风险、可逆、简单问题。目标是快速形成下一步，不完整加载所有模型。

### Standard
普通人生与工作问题。加载必要模型，运行主要 Core OS 和 Playbook。

### Deep
高影响、高不确定性、高风险或难逆问题。完整记录事实、假设、未知、取舍、风险和重新评估条件。

运行深度应由 `Impact × Uncertainty × Risk × Irreversibility` 决定。

## 目录

- `scenarios.zh-CN.md`：20 个标准测试场景
- `rubric.zh-CN.md`：评分规则与发布门槛
- `comparison-template.zh-CN.md`：普通 AI 与 LifeOS 对照测试
- `validation-matrix.zh-CN.md`：Core OS / 场景覆盖矩阵
- `report-template.zh-CN.md`：验证报告模板

## v0.1 验收建议

- 20 个标准场景全部能够完成 Runtime；
- 六项指标平均总分 ≥ 24/30；
- Actionability 不低于 4/5；
- Autonomy 不低于 4/5；
- 不存在阻止 Runtime 完成的 P0 Framework Issue；
- P1 问题完成修复或明确记录；
- 与 Baseline AI 相比，LifeOS 在 Clarity、Context Fit、Actionability 中至少两项表现出稳定提升。

Validation 的目的不是证明 LifeOS 正确，而是持续寻找 LifeOS 哪里不工作。
