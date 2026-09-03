# Blind A/B Run Protocol

## 1. Freeze

测试期间使用冻结的 LifeOS v0.1.1。发现问题先记录，不立即修改框架，否则后续 Case 与前面 Case 不可比较。

## 2. Generate Baseline

System instruction：作为优秀通用 AI 助手回答用户问题。不要读取、引用或模拟 LifeOS。目标是给出自然、实用、尊重用户自主性的高质量帮助。

## 3. Generate LifeOS

加载冻结的 `skills/lifeos/SKILL.md`，使用相同用户输入。不得为了测试而机械打印框架；遵守 Runtime Level 与 Process Cost 原则。

## 4. Normalize

不要人为把两边改成相同长度。只清除会暴露来源的显式标签，例如 `LifeOS`、`Self Model` 等框架品牌词；保留回答本身的结构和推理价值。

## 5. Randomize

每个 Case 独立随机决定 Baseline/LifeOS 映射到 A 或 B。映射保存在单独 Reveal Key 中，Evaluator 不可访问。

## 6. Evaluate

至少 3 位 Evaluator 为理想配置；早期试跑可用 1–2 位，但必须标注限制。每位 Evaluator 独立评分，不能先讨论。

## 7. Primary Outcomes

1. Pairwise Overall Win Rate
2. Clarity Delta
3. Context Fit Delta
4. Actionability Delta
5. Autonomy Delta
6. Process Cost Delta

Insight 与 Decision Support 为重要次级指标。

## 8. Pass Criteria for Pilot

第一轮 10 Case Pilot 不作为统计显著性研究，而作为产品/框架验证。建议门槛：

- LifeOS Overall preference ≥ 60%，且不能主要来自回答长度；
- Clarity / Context Fit / Actionability 三项中至少两项平均优于 Baseline；
- Autonomy 不低于 Baseline；
- Process Cost 不得出现明显系统性恶化；
- 无 P0；
- LifeOS Lose 的 Case 必须能够解释失败原因。

## 9. Human Real-problem Round

Pilot 后邀请 5–10 位真实用户，每人提供 1–2 个真实问题。用户本人回答三个核心问题：

1. 哪个更懂我的真实处境？
2. 哪个让我更知道下一步做什么？
3. 哪个我更愿意实际使用？

用户偏好与第三方 Rubric 同时记录。

## 10. Change Control

全部 10 Case 完成并揭盲后才能形成 v0.1.2 修改列表。修改后必须运行 Regression，再进入下一轮 Blind A/B。
