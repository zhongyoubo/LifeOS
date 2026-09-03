# Self Model / 自我模型

[English](./self-model.md) | **简体中文**

Self Model 是 LifeOS 的个人状态模型，用于持续回答“我是谁、我现在怎样、我正在发生什么变化”。

## 模型结构

```yaml
self:
  identity: []
  values: []
  needs: []
  interests: []
  strengths: []
  limitations: []
  patterns: []
  resources: []
  relationships: []
  responsibilities: []
  life_stage: ""
  current_state:
    emotion: ""
    energy: ""
    attention: ""
    pressure: ""
  assumptions_about_self: []
  evidence_log: []
  open_questions: []
  version: "0.1.1"
```

## Evidence Gate

任何重要 Self Model 更新都应避免从单次事件直接形成永久标签。建议记录：

```yaml
self_hypothesis:
  statement: ""
  evidence: []
  counterevidence: []
  confidence: "low | medium | high"
  source_contexts: []
  review_date: ""
```

以下结论尤其需要 Evidence Gate：能力、人格、长期限制、价值观变化、重复行为模式，以及“我适合/不适合某角色”之类结论。

## 使用原则

- 描述而不是给自己贴永久标签。
- 区分事实、自我评价和他人评价。
- 允许矛盾，人不是静态模型。
- 记录证据和反证，不只记录结论。
- 单次成功或失败通常只能形成 Hypothesis，不能直接形成 Identity。
- 定期更新，而不是追求一次性“认识真正的自己”。
- 对过去的 Self Model 保留版本，以观察成长轨迹。

## 更新触发器

重大经历、角色变化、长期目标变化、重复出现的行为模式、重要反馈、失败与成功，以及周期性复盘，都可以触发 Self Model 更新。重要更新应在不同情境或后续行为中再次验证。
