# LifeOS v0.1 Smoke Validation 01

> 日期：2026-09-04  
> 范围：V03 / V07 / V13 / V18 / V20  
> 类型：Synthetic Smoke Validation（合成场景验证）

## 0. 测试说明与限制

本轮用于验证 **Framework Runtime 的结构完整性**，不是用户研究，也不是独立模型 benchmark。

为了能够重复执行，每个标准场景补充一组最小合成上下文。Baseline 与 LifeOS 使用同一上下文。Baseline 是“优秀通用 AI 助手”的预期响应模式；LifeOS Run 按当前 `skills/lifeos/SKILL.md` 执行。

因此本报告中的分数属于**框架自测分数**，不能当作 LifeOS 已被真实用户验证的证据。下一阶段仍需要 blind / human validation。

---

# V03 — 是否换工作

## Synthetic Context

35 岁软件工程师；当前公司工作 5 年；收入稳定；近 18 个月工作内容重复，学习明显下降；家庭有 12 个月应急储备；外部机会薪资约 +20%，技术成长更好，但公司较小、稳定性较低；本人重视成长，也重视家庭稳定。

Runtime Level: **Deep**

### Baseline AI

典型高质量回答会建议比较薪资、成长、稳定性、文化、家庭影响，制作优缺点表，并建议在拿到正式 offer 后再决定。

**Score:** Clarity 3 / Context 3 / Insight 3 / Decision 3 / Action 4 / Autonomy 4 = **20/30**

### LifeOS Run

**Real Problem**

真正问题不是“要不要换工作”，而是：**在成长价值与家庭稳定边界之间，当前岗位是否仍然值得继续投入，以及外部机会是否提供足够的风险补偿。**

**Models**
- Self：成长重要；家庭稳定也是明确边界。
- Context：当前岗位低风险但成长下降；新机会成长高但组织风险增加。
- Role：个人职业发展者 + 家庭责任承担者。
- Goal：未来 2–3 年保持职业能力增长，同时不让家庭承担不可接受的下行风险。

**Facts**：当前工作稳定；18 个月学习下降；12 个月储备；新机会薪资约 +20%。

**Assumptions**：小公司一定更不稳定；当前岗位未来仍不会改善；新岗位成长空间真实存在。

**Unknowns**：新公司现金流/融资、直属领导、实际职责、试用期风险、当前公司内部转岗可能性。

**Decision Structure**

暂不直接决定“走/留”。先验证三个决定性未知：新机会真实风险、真实成长空间、内部改变可能性。

**Next Action**

48 小时内完成一页 Decision Evidence Sheet：向新公司确认 runway/团队稳定性/岗位前三个月目标，同时与当前领导确认未来 6–12 个月是否存在实质职责变化。证据齐备后再做正式取舍。

**Revisit Condition**：如果新公司的风险处于家庭边界以内且成长优势得到验证，进入最终 Decision Run。

**Score:** 5 / 5 / 5 / 5 / 5 / 5 = **30/30**

**Finding**：LifeOS 的价值来自把“价值冲突 + 边界 + 未知验证”放在决定之前，而不是增加更多优缺点。

---

# V07 — 接手陌生软件项目

## Synthetic Context

两周后必须向管理层汇报；项目已有 8 名成员；文档零散；版本计划晚 4 周；原负责人刚离职；你被指定为新负责人，但权限尚未明确。

Runtime Level: **Standard**

### Baseline AI

通常会建议阅读文档、理解架构、和团队 1:1、检查 Jira/里程碑、识别风险、制定接管计划。

**Score:** 4 / 3 / 3 / 3 / 5 / 4 = **22/30**

### LifeOS Run

**Real Problem**

不是“尽快学懂所有项目内容”，而是：**在两周内建立足够的项目控制面，使自己能够解释项目状态、关键风险、责任结构和下一步恢复计划。**

**Role Conflict / Gap**：Responsibility 已转移，但 Authority 未明确，这是首要管理风险。

**Unknowns**：项目成功标准、真实完成度、关键路径、Top Risks、关键人员、技术债、管理层对两周汇报的期待。

**Activated Systems**：Thinking + Communication + Execution + Learning。

**Next Action**

今天创建一张 `Project Takeover Map`，只包含：Goal、Milestones、Owners、Architecture Map、Top 5 Risks、Top 5 Unknowns、Next Deadline。随后安排 60 分钟团队状态会，并单独向上级确认自己的决策权限。

**Checkpoint**：72 小时后必须能够用一页图回答“项目在哪里、为什么延期、最大风险是什么、接下来两周做什么”。

**Score:** 5 / 5 / 5 / 4 / 5 / 5 = **29/30**

**Finding**：Role Model 在这里产生明显价值；“责任已给、权限未给”比技术学习本身更可能阻止接管成功。

---

# V13 — 重要关系中的长期分歧

## Synthetic Context

伴侣双方连续一年围绕是否迁居海外发生争执。一方认为海外机会有利于职业发展，另一方担心父母照护、社交支持和生活稳定。双方每次讨论最终都会变成“你不支持我 / 你只考虑自己”。

Runtime Level: **Deep**

### Baseline AI

通常建议冷静沟通、倾听彼此、列出利弊、理解底层需求、考虑折中方案或试住。

**Score:** 3 / 3 / 4 / 3 / 3 / 5 = **21/30**

### LifeOS Run

**Real Problem**

表面问题是“去不去海外”，深层问题是：**两个人尚未形成共同 Goal，也没有把各自不可牺牲的 Boundary 与可协商的 Preference 分开。**

**Facts**：争议持续一年；迁居涉及职业机会、父母照护、支持网络。

**Interpretations**：“你不支持我”“你只考虑自己”目前属于解释，不是已验证事实。

**Values / Boundaries**：职业成长、家庭责任、稳定、伴侣共同生活质量。

**Activated Systems**：Thinking + Communication + Decision + Emotion & Energy。

**Next Action**

下一次讨论暂时禁止讨论“去/不去”。双方分别写下：①最担心失去什么；②不可接受边界；③可协商条件；④希望共同生活在三年后是什么状态。先交换并复述对方内容，确认理解后才进入方案设计。

**Checkpoint**：只有双方都能准确复述对方的核心利益与边界，才开始比较“留下 / 迁居 / 延迟 / 试住 / 分阶段迁移”等方案。

**Score:** 5 / 5 / 5 / 5 / 5 / 5 = **30/30**

**Finding**：Communication 不应该直接承担“解决冲突”，Goal Model 和 Boundary clarification 必须先于方案谈判。

---

# V18 — 重要项目失败

## Synthetic Context

负责 6 个月的重要产品项目最终取消。团队投入很大；原因包括需求频繁变化、关键依赖延期以及自己没有及时升级风险。本人很沮丧，并开始怀疑自己是否适合继续做项目负责人。

Runtime Level: **Standard**

### Baseline AI

通常会安慰用户，建议复盘原因、区分可控不可控因素、总结经验、和团队沟通并调整心态。

**Score:** 4 / 3 / 3 / 3 / 4 / 5 = **22/30**

### LifeOS Run

**State First**：当前存在明显情绪冲击。避免在失败后的高情绪状态直接更新“我不适合做负责人”这种 Self Model 结论。

**Review Separation**
- Outcome：项目取消。
- Decision Quality：需要逐项检查当时信息，而不是用结果倒推所有决定错误。
- Execution Quality：风险升级明显偏晚。
- External Factors：需求变化、关键依赖延期。
- Luck / Environment：需单独记录。

**Candidate Lesson**：不是“我不适合负责项目”，而是一个可验证假设：**当跨团队依赖超过某阈值时，我需要更早建立显式风险升级机制。**

**Next Action**

在 72 小时内完成事实时间线，只记录 Expected / Actual / Decision / Signal / Response，不写人格评价。之后选择 1 条可改变的机制进入下一个项目验证，例如“关键依赖连续两个 checkpoint 未达成即升级”。

**Score:** 5 / 5 / 5 / 4 / 5 / 5 = **29/30**

**Finding**：Emotion & Energy 与 Review 的顺序非常重要；Self Model 更新必须受到证据门槛保护。

---

# V20 — 未来三到五年没有方向

## Synthetic Context

38 岁；工作和家庭总体稳定；经济没有明显危机；感觉生活进入重复模式；对继续晋升、创业、深度学习或更多陪伴家庭都感兴趣，但没有一个方向强到足以承诺三到五年。

Runtime Level: **Deep**

### Baseline AI

通常建议梳理价值观、想象理想生活、列出几个方向、做人生轮盘、设 SMART 目标或进行小实验。

**Score:** 3 / 3 / 3 / 3 / 4 / 5 = **21/30**

### LifeOS Run

**Real Problem**

这不是缺少 Goal，而可能是**当前还没有足够证据把一个方向升级为长期 Goal**。强迫生成三到五年目标会制造虚假确定性。

**Self / Context**：稳定提供了探索空间；多个方向同时有吸引力，说明当前阶段更需要探索而非过早承诺。

**Decision**：暂不选择一个三年目标。建立 90 天 Direction Discovery Cycle。

**Experiments**
1. 职业：承担一次更高层级职责或访谈 3 位目标角色从业者。
2. 创业：完成一个小规模真实用户验证，而不是写商业计划。
3. 学习：选择一个领域完成 20 小时深度项目。
4. 家庭：设计一个连续 4 周的高质量家庭时间实验。

每项记录 Energy / Meaning / Capability / Opportunity / Cost。

**Next Action**：本周选择两个方向，各设计一个 ≤10 小时、可逆、能产生真实信息的实验。

**Checkpoint**：90 天后根据真实经历更新 Self Model 和 Goal Model。

**Score:** 5 / 5 / 5 / 5 / 5 / 5 = **30/30**

**Finding**：Goal Model 需要正式支持 `Exploration Mode`；不是所有人生阶段都应该立即生成长期目标。

---

# 1. Smoke Result

| Scenario | Baseline | LifeOS | Delta | Result |
|---|---:|---:|---:|---|
| V03 换工作 | 20 | 30 | +10 | Strong Pass |
| V07 陌生项目 | 22 | 29 | +7 | Strong Pass |
| V13 长期分歧 | 21 | 30 | +9 | Strong Pass |
| V18 项目失败 | 22 | 29 | +7 | Strong Pass |
| V20 人生方向 | 21 | 30 | +9 | Strong Pass |
| **Average** | **21.2** | **29.6** | **+8.4** | **Synthetic Strong Pass** |

> 注意：这些分数由同一轮框架分析产生，存在 evaluator bias，不能作为独立效果证明。

# 2. Framework Findings

## F01 — Goal Model 缺少 Exploration Mode — P1

V20 显示：当用户没有足够证据形成长期目标时，当前 Goal Model 容易诱导“强行设目标”。

**建议**：Goal 增加 `mode: explore | commit | maintain | exit`，探索阶段允许目标是“获得决策信息”。

## F02 — Self Model 更新需要 Evidence Gate — P1

V18 显示：失败后容易把单次结果写成永久自我标签。

**建议**：任何重要 Self Model 更新记录 `evidence / confidence / counterevidence / review_date`。

## F03 — Runtime Depth 需要进入 Skill — P1

Validation 已定义 Quick / Standard / Deep，但当前 Skill 只写“minimum depth required”，没有明确选择机制。

**建议**：Skill 正式加入 Runtime Level，根据 Impact / Uncertainty / Risk / Irreversibility 路由。

## F04 — Role Responsibility / Authority Gap 应成为显式诊断 — P1

V07 表明角色接管问题中，责任与权限不匹配是高价值诊断点。

**建议**：Role Model 增加 `responsibility_authority_gaps` 或 Runtime 检查规则。

## F05 — Playbook 可能与 Runtime 重复 — P2

本轮五个场景主要价值来自 Foundation Models + Core Router + Next Action，Playbook 本身没有显示足够独立价值。

**建议**：后续验证 Playbook 是否提供“领域特有步骤”；若只是重复 Runtime，应删除或降级为 Pattern。

## F06 — Baseline 比较方法存在评估偏差 — P1 Validation

同一个模型同时生成 Baseline、LifeOS 并评分，天然偏向框架。

**建议**：下一轮采用 Blind A/B：隐藏答案来源，由独立人类或独立 evaluator 按 Rubric 评分。

# 3. Release Decision

**HOLD** — 不建议仅凭本轮宣布 v0.1 已验证。

Framework Runtime 在五类差异明显的合成场景中表现出良好的结构完整性，但本轮更接近“架构 Smoke Test”。先修复 F01–F04，再进行 20 场景全量验证和 Blind/Human Validation，才适合进入正式 v0.1 Release Gate。
