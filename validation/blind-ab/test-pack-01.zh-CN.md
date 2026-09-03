# LifeOS v0.1.1 Blind A/B Test Pack 01

> Baseline: LifeOS v0.1.1 Frozen Architecture  
> Purpose: test structural value beyond a capable general AI assistant.

## Test Rules

1. 每个 Case 使用完全相同的用户输入生成两个回答。
2. Response A/B 随机分配，Evaluator 不知道哪个使用 LifeOS。
3. Baseline 不允许读取 LifeOS 文档；LifeOS 条件使用冻结的 `skills/lifeos/SKILL.md`。
4. 尽量保持相同模型、temperature、语言和可用上下文。
5. 不以回答长度作为优势；额外流程必须证明有价值。
6. 每个回答独立评分后，再做 Pairwise Preference。
7. 在全部评分完成前不得揭盲。

## 10 Cases

### AB01 — Career Decision
我在现在公司工作 5 年，收入稳定，但最近一年多成长明显变慢。现在有一家规模更小的公司给我机会，工资高约 20%，技术方向更有吸引力，但稳定性肯定不如现在。我有家庭，也有大约一年的应急储备。我该不该换工作？

### AB02 — New Manager
我刚从资深工程师升为团队经理。以前我主要靠自己解决问题，现在发现每天都是会议、协调和处理人的问题。我感觉自己的产出反而下降了，不知道这个角色应该怎么做好。

### AB03 — Project Takeover
原项目负责人突然离职，公司让我接手一个已经延期 4 周的软件项目。团队 8 个人，文档比较乱，两周后我要向管理层汇报。我对项目技术和历史都不熟，而且目前也不确定自己到底有多大决策权限。我应该先做什么？

### AB04 — Important Disagreement
我认为领导准备推进的方案有明显技术风险，但他已经比较倾向这个方案。我不想显得是在反对领导，也不想因为没说清楚最后项目出问题。我应该怎么沟通？

### AB05 — Too Many Priorities
最近同时有四五件重要事情：项目交付、团队管理、学习 AI、家庭安排，还有一个自己很想做的副项目。每件事情都有理由做，我每天都很忙，但总感觉最重要的事情没有推进。应该怎么处理？

### AB06 — Learn a New Domain
我需要在一个月内快速理解一个完全陌生的技术领域，不要求成为专家，但要达到可以和专业人员讨论、判断方案和做基本决策的程度。应该怎么学？

### AB07 — Failure and Self-Doubt
我负责了半年多的一个重要项目最后被取消了。需求变化和外部依赖都有影响，但我自己确实也没有及时升级风险。现在我开始怀疑自己是不是不适合继续做项目负责人。我应该怎么面对这件事？

### AB08 — Long-term Relationship Conflict
我和伴侣已经一年多反复争论要不要去海外发展。我觉得这是很好的职业机会，对方担心父母照护、生活稳定和社交关系。现在每次讨论最后都会变成互相指责。我们应该怎么处理？

### AB09 — No Long-term Direction
我 38 岁，工作、家庭和经济总体都比较稳定，但感觉生活进入重复模式。我对继续晋升、创业、深入学习一个领域、花更多时间陪家庭都有兴趣，但没有一个方向强烈到让我愿意承诺未来三五年。我应该怎么规划？

### AB10 — Sunk Cost / Exit Decision
我已经在一个个人项目上投入了一年多，也花了不少钱，但用户增长一直不好。我仍然觉得这个想法可能有价值，可继续投入又担心是在沉没成本里越陷越深。我应该继续、调整还是停止？

## Coverage

| Case | Main Coverage |
|---|---|
| AB01 | Goal, Decision, Values, Risk |
| AB02 | Role, Responsibility/Authority, Learning |
| AB03 | Role, Context, Thinking, Execution, Project Playbook |
| AB04 | Thinking, Communication, Risk |
| AB05 | Goal, Decision, Execution |
| AB06 | Learning, Execution, Domain Playbook |
| AB07 | Review, Emotion & Energy, Self Evidence Gate |
| AB08 | Goal, Communication, Decision, Boundaries |
| AB09 | Self, Goal Exploration Mode, Decision |
| AB10 | Goal Exit Mode, Decision, Review |

## Reveal Key

不要在本文件记录 A/B 对应关系。Reveal Key 必须在所有评价完成后单独生成并保存。
