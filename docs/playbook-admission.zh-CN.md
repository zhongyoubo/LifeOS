# Playbook Admission Rule / Playbook 准入规则

[English](./playbook-admission.md) | **简体中文**

Playbook 不是 LifeOS 的必经层。它只在能提供领域特有价值时存在。

## 准入标准

一个候选 Playbook 至少满足以下 3 项，才建议独立保留：

1. **Domain Sequence**：存在领域特有步骤顺序，通用 Runtime 无法简单替代。
2. **Domain Checks**：存在该领域必须检查的风险、信息或边界。
3. **Domain Output**：存在领域特有输出物，如 Project Takeover Map、Learning Map、Failure Timeline。
4. **Cognitive Cost Reduction**：明显减少用户从零组织问题的认知成本。
5. **Repeatability**：在多个同类场景中可重复使用，而非单个案例技巧。
6. **Validation Evidence**：至少在 3 个真实或高质量测试场景中证明增益。

## 不应独立成为 Playbook 的情况

- 只是把 Kernel Runtime 换一种说法；
- 只是组合通用 Thinking / Decision / Communication；
- 没有领域特有检查项或输出；
- 只适用于一个极窄案例；
- 依赖大量作者个人偏好；
- 增加流程但没有降低错误率或认知成本。

## 生命周期

```text
Candidate
   ↓
Trial
   ↓
Validated
   ↓
Stable
```

如果验证发现重复或价值不足：

```text
Stable / Trial
   ↓
Simplify
   ↓
Pattern / Method / Template
   ↓
Archive
```

## v0.1.1 当前处理

- Complex Problem → 降级为 Kernel / Thinking Pattern
- Important Decision → 优先由 Decision System + Template 承担
- New Role / Environment → Trial Playbook
- Unfamiliar Project → Validated Domain Playbook
- Important Disagreement → Trial Playbook
- New Domain Learning → Validated Domain Playbook
- Failure Recovery → Validated Domain Playbook

后续是否继续保留，必须由验证证据决定，而不是因为“7 个看起来完整”。
