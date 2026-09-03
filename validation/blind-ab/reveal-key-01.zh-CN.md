# Blind A/B Reveal Key 01

> CONFIDENTIAL UNTIL EVALUATION COMPLETES
>
> Evaluator 不应在完成全部 10 个 Case 的评分前阅读本文件。

| Case | Response A | Response B |
|---|---|---|
| AB01 | LifeOS | Baseline |
| AB02 | LifeOS | Baseline |
| AB03 | LifeOS | Baseline |
| AB04 | LifeOS | Baseline |
| AB05 | LifeOS | Baseline |
| AB06 | LifeOS | Baseline |
| AB07 | LifeOS | Baseline |
| AB08 | LifeOS | Baseline |
| AB09 | LifeOS | Baseline |
| AB10 | LifeOS | Baseline |

## Methodological Warning

本轮 Execution Pack 的内容由同一执行环境生成，因此它适合测试 evaluator workflow 和答案结构，但**当前 A/B 顺序没有实现真正随机化**，并且生成环境知道两种条件。

因此：

- 不应把本轮结果称为严格的 randomized blind experiment；
- 可作为 `Pilot-0 / Evaluator Dry Run`；
- 正式 Pilot-1 应由独立 runner 分别生成 Baseline 与 LifeOS 输出，再通过脚本或独立协调者随机分配 A/B；
- Reveal Key 应与 evaluator material 分离存储。

保留这个限制是为了避免把“形式上的盲测”误报为真正实验结果。
