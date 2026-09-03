# v0.1.2 Candidate — Cognitive Augmentation Protocols / 认知增强协议

[English](./cognitive-augmentation.md) | **简体中文**

> 状态：**PROPOSAL / NOT PART OF FROZEN v0.1.1**
>
> 目标不是让 LifeOS 替用户“想得更多”，而是让用户逐渐形成更准确、更可校准、更可迁移的思考与判断能力。

## 1. 定位

Capability Map 已定义 LifeOS 的双重价值：推进现实问题，同时增强人的能力。本提案补充其中的认知增强机制：

```text
Situation
   ↓
Cognitive Calibration
   ↓
Problem Framing
   ↓
Mental Model Router
   ↓
Reason / Decide / Act
   ↓
Evidence
   ↓
Reflection + Transfer
   ↓
Better Independent Judgment
```

认知增强层不是新的 Core OS。它优先作为 Thinking / Decision / Learning / Review 可复用的协议候选进行验证。

## 2. Cognitive Calibration Protocol

### 2.1 目标

认知校准不是让用户更自信，也不是让用户怀疑一切，而是让：

> **Confidence ≈ Quality of Evidence**

### 2.2 Evidence Stack

对重要判断，在必要时拆分：

```text
Facts          可观察或可验证的信息
Interpretation 对事实的解释
Assumptions    当前推理依赖但尚未验证的前提
Values         用户在意什么、如何取舍
Unknowns       当前不知道但可能影响判断的信息
Prediction     对未来的可检验预期
Confidence     对判断的定性置信度
```

默认使用 Low / Medium / High 等定性等级，不制造虚假的数字精确度。

### 2.3 Calibration Questions

只选择真正会改变判断的问题：

- 我们真正知道什么？
- 哪部分是解释而不是事实？
- 哪个假设最脆弱？
- 有什么反证？
- 哪个未知最值得先降低？
- 什么新证据会改变当前结论？
- 当前行动是否需要等待更高确定性？
- 如果判断错了，是否容易撤销？

### 2.4 Confidence Update

```text
Initial Judgment
      ↓
Evidence / Counterevidence
      ↓
Alternative Explanation
      ↓
Uncertainty / Reversibility
      ↓
Updated Judgment + Confidence
      ↓
Checkpoint / Disconfirming Evidence
```

置信度应可修改。改变观点是校准成功，不是失败。

## 3. Mental Model Protocol

### 3.1 原则

Mental Model 的价值不在于“知道模型名称”，而在于它能否改善现实判断。

LifeOS 不应默认输出模型清单，也不应为了显得深刻而套模型。

### 3.2 Model Schema

每个稳定 Mental Model 建议至少包含：

```text
Name
Definition
Purpose / Problem Type
Trigger Conditions
Core Mechanism
Assumptions
How to Apply
Questions to Ask
Example
Counterexample
Failure Modes
Boundary / When Not to Use
Related / Competing Models
Practice
Transfer Cases
Evidence Notes
```

### 3.3 Mental Model Router

```text
Problem Diagnosis
      ↓
What kind of reasoning is missing?
      ↓
Candidate Models
      ↓
Relevance Check
      ↓
Boundary / Assumption Check
      ↓
Select Minimum Useful Model(s)
      ↓
Apply to the actual problem
      ↓
Did it change understanding or action?
      ├─ No  → discard
      └─ Yes → optionally expose model to user
```

### 3.4 Router Signals

示例，不是穷举：

| Signal | Candidate reasoning lens |
|---|---|
| 已投入很多所以不愿退出 | Sunk Cost + Opportunity Cost |
| 局部优化反而使整体更差 | Systems / Bottleneck / Feedback |
| 短期收益与长期后果冲突 | Second-order Effects / Compounding |
| 两个方案都不确定 | Expected Value / Reversibility / Option Value |
| 只看到单一解释 | Alternative Hypotheses / Base Rates |
| 责任很大但无法推动 | Responsibility–Authority Gap |
| 一次失败变成永久自我结论 | Evidence Gate / Attribution |

模型名称不是最终输出要求。对 Quick Runtime，直接用其逻辑往往比讲模型更好。

## 4. Model Selection Gate

只有满足至少一项时才显式引入模型：

1. 它会改变问题定义；
2. 它会改变重要决策或行动；
3. 它能暴露关键盲点；
4. 它有高概率在未来重复使用，值得教给用户；
5. 用户明确希望理解方法。

否则模型应留在后台推理，减少 Process Cost。

## 5. Metacognitive Transfer Protocol

LifeOS 不只要应用模型，还应在重要场景帮助用户学习“自己是怎么判断的”。

```text
What happened?
      ↓
How did I interpret it?
      ↓
What assumption/model did I use?
      ↓
What evidence supported it?
      ↓
What did I miss?
      ↓
What happened after acting?
      ↓
What should I keep/change next time?
      ↓
Where else does this lesson transfer?
```

优先提炼：
- 可重复的判断原则；
- 触发条件；
- 边界与反例；
- 下一次更早识别的信号。

不要把单次经验升级成普遍规律。

## 6. Cognitive Bias Handling

LifeOS 不应该把“认知偏差列表”当诊断工具随意给用户贴标签。

推荐顺序：

```text
Observe reasoning pattern
→ identify concrete evidence gap
→ test alternative explanation
→ show consequence
→ only name a bias if the label improves learning
```

避免：
- “你这是确认偏误”式标签化；
- 用偏差术语替代实际分析；
- 把合理的价值偏好误判为偏差；
- AI 假设自己天然没有偏差。

## 7. AI Guidance

AI 应：

- 优先改善判断结构，而非堆砌模型名称；
- 对高影响、不可逆、高不确定问题加强校准；
- 对低风险可逆问题更快行动并用反馈学习；
- 明确最关键的未知，而不是列出所有未知；
- 主动寻找可能推翻当前结论的证据；
- 在多个解释都合理时保留不确定性；
- 必要时说明为什么选择某个 Mental Model；
- 用户已掌握时减少解释，转为 Calibrate；
- 不把 LifeOS/AI 的推理包装成确定事实。

## 8. Output Contract

Standard/Deep 场景可按需输出：

```text
Current Judgment
Known Facts
Key Interpretation
Critical Assumption
Important Unknown
Alternative Explanation
Relevant Mental Model (optional)
Decision / Next Action
Confidence
What Would Change the Judgment
Checkpoint
Transfer Lesson (after evidence)
```

Quick Runtime 只保留影响下一步的字段。

## 9. Validation Hypotheses

H1：Calibration Protocol 能减少事实/解释/假设混淆。

H2：Mental Model Router 相比“模型清单式建议”提高 Context Fit 和 Insight。

H3：Minimum Useful Model Gate 不会系统性增加 Process Cost。

H4：经过重复场景后，用户能更独立地识别关键假设和适用模型。

H5：LifeOS 的帮助强度可以从 Guide/Coach 逐渐下降到 Calibrate，而不降低结果质量。

## 10. Candidate Validation Cases

1. “这个项目失败说明我不适合做负责人。”
2. “这个项目已经投入一年了，现在放弃太可惜。”
3. “两个工作机会都不错，我担心选错。”
4. “团队一直加人但交付反而越来越慢。”
5. “领导不同意我的方案，我觉得他根本不懂技术。”
6. “这个投资/职业选择看起来成功概率很高，我要不要重仓？”
7. 同类问题重复两次，测试第二次是否能降低 Assistance Level。
8. 一个简单可逆选择，测试 LifeOS 是否避免过度分析。

## 11. Admission Gate

进入稳定 Core/Runtime 前必须证明：

- 能改善 Clarity / Insight / Decision Support 中至少两项；
- 不降低 Actionability；
- Process Cost 可接受；
- 不鼓励无限分析；
- 用户能出现可观察的 Calibration / Transfer 改善；
- 不与现有 Thinking / Decision 重复到没有增量价值。

若只有局部价值，应保留为 Thinking Pattern / Decision Pattern，而不是新增架构层。
