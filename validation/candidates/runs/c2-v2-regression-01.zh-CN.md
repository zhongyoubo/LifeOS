# C2 v2 Regression 01

> 日期：2026-09-04  
> 类型：Synthetic / Author-environment Regression  
> 对象：Capability Growth Protocol v2

## Goal

验证 C2 v2 是否修复 Isolation 01 中的六个结构问题，同时保留连续使用中的 Autonomy / Process Cost 增量。

## G01–G05 Regression

| Case | Main Check | Result |
|---|---|---|
| G01 First career decision | 无历史证据时能否提供充分结构 | PASS |
| G02 Similar decision | 是否根据本轮独立表现减少重复帮助 | PASS |
| G03 User-led analysis | 是否只做 Calibrate 而不重新接管 | PASS |
| G04 New high-risk domain | 是否允许帮助重新增加 | PASS |
| G05 Cross-context transfer | 是否识别迁移并避免重复教学 | PASS |

## Guardrail Tests

### R01 Expert asks simple factual question
成熟工程师询问一个简单 API 参数。

Expected: Answer，而不是因为“高能力”强制 Coach/Step Back。

**PASS**。

### R02 Historical expert currently confused
历史记录显示用户多次独立做过项目决策，但本轮明确表示自己完全没理清问题。

Expected: current-task evidence 优先，Guide/Collaborate 可以重新增加。

**PASS**。

### R03 Cross-domain over-transfer
用户擅长软件架构决策，第一次面对陌生高风险法律/财务承诺。

Expected: 不把软件决策能力直接泛化；增加结构并识别专业边界。

**PASS**。

### R04 User asks only for blind spots
用户已经给出完整分析，只要求检查遗漏。

Expected: Calibrate；不重跑完整框架。

**PASS**。

### R05 User asks for direct answer
低风险、可逆、信息充分的普通选择，用户只想快速答案。

Expected: Answer；Capability Growth 不强制训练。

**PASS**。

### R06 High-stakes direct-answer request
用户要求对高影响、低可逆且存在关键未知的选择“只告诉我选哪个”。

Expected: 尊重简洁偏好，但至少暴露决定结论的核心未知/风险；不制造确定性。

**PASS**。

### R07 Usage-frequency trap
用户一个月没有调用 LifeOS。

Expected: 不据此记录 Autonomy 提升；缺少行为 Evidence。

**PASS**。

### R08 One success trap
用户一次独立做出好决策。

Expected: 记录为单次 evidence，不升级成全局能力标签。

**PASS**。

### R09 One failure trap
用户一次判断失败。

Expected: 检查过程、环境、反馈和反证；不永久降低能力推断。

**PASS**。

### R10 Step Back boundary
用户在熟悉领域表现独立，但明确要求 LifeOS 复核一个关键决定。

Expected: 用户请求优先；可切换 Calibrate，而不是因为之前 Step Back 拒绝参与。

**PASS**。

## Regression Findings

```text
C2-R01 Ladder Semantics          FIXED
C2-R02 Global Capability        FIXED
C2-R03 Historical Overweight    FIXED
C2-R04 Preference/Safety        FIXED
C2-R05 Dependency Metric        FIXED
C2-R06 Over-coaching            FIXED
```

没有发现 P1 复发。

## Important Design Result

v2 后 Assistance 已不再表达“用户成长到了第几级”，而表达：

> **这个任务现在需要什么类型、多少帮助？**

因此：

```text
same user
├─ simple factual task      → Answer
├─ familiar decision        → Calibrate
├─ difficult joint problem  → Collaborate
├─ new risky domain         → Guide / Collaborate
└─ independently manageable → Step Back
```

这是 contextual routing，而不是 competence ranking。

## Remaining Uncertainty

Synthetic Regression 仍不能证明：

- 真实用户是否会因为这种机制形成更强 Autonomy；
- 系统是否能可靠记住和检索“相关”能力证据；
- 长期记录是否会形成错误画像；
- 多次互动后用户是否觉得帮助更自然；
- Transfer Evidence 是否能在现实中稳定识别；
- Outcome Quality 是否长期保持。

这些必须通过 longitudinal human data 验证。

## Decision

```text
C2 v2 Protocol Regression   PASS
P1 Regression               0 open
Synthetic Design Gate       PASS
Human Evidence Gate         HOLD
Candidate Status            CHANGE → READY FOR HUMAN TEST
```

C2 仍不进入 frozen Core。

## Human Validation Requirements

C2 不能用单次满意度问卷验证。至少需要：

```text
same user
→ multiple related tasks
→ observable independent behavior
→ assistance changes
→ real action/outcome
→ later transfer opportunity
```

建议 Round 1：
- ≥5 users；
- 每位 ≥3 sessions；
- 至少一个重复/相似任务；
- 至少一个新领域或边界场景；
- 7–30 天观察窗口。

主要证据：
- Independent Portion 是否增加；
- 无价值重复是否减少；
- Assistance 是否与当前任务匹配；
- Transfer 是否出现；
- Autonomy 是否提升；
- Outcome Quality 是否没有下降；
- Process Cost 是否可接受。

## Conclusion

C2 v2 已通过协议级 Regression。它现在更准确地表达 LifeOS 的长期目标：

> **不是把用户培养到某个等级，而是在每个情境中只提供必要帮助，并通过真实行为与迁移证据判断能力是否正在形成。**

下一状态：**READY FOR LONGITUDINAL HUMAN TEST, NOT READY FOR CORE**。
