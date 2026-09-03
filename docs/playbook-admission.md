# Playbook Admission Rule

**English** | [简体中文](./playbook-admission.zh-CN.md)

Playbooks are not a mandatory LifeOS layer. They exist only when they add domain-specific value beyond the Kernel Runtime.

## Admission Criteria

A candidate Playbook should satisfy at least three of the following:

1. **Domain Sequence** — domain-specific sequencing that the general Runtime does not trivially provide.
2. **Domain Checks** — risks, information, or boundaries that are specific to the domain.
3. **Domain Output** — a domain-specific artifact such as a Project Takeover Map, Learning Map, or Failure Timeline.
4. **Cognitive Cost Reduction** — materially reduces the effort required to structure the situation from scratch.
5. **Repeatability** — reusable across multiple situations in the domain.
6. **Validation Evidence** — demonstrates useful incremental value in at least three real or high-quality test scenarios.

## Reject or Downgrade When

- it merely restates the Kernel Runtime;
- it is only a generic combination of Thinking / Decision / Communication;
- it has no domain-specific checks or outputs;
- it only applies to a single narrow example;
- it depends heavily on author preference;
- it adds process without reducing error or cognitive cost.

## Lifecycle

```text
Candidate → Trial → Validated → Stable
```

If later evidence shows duplication or insufficient value:

```text
Stable / Trial → Simplify → Pattern / Method / Template → Archive
```

## v0.1.1 Current Classification

- Complex Problem → Kernel / Thinking Pattern
- Important Decision → primarily Decision System + Template
- New Role / Environment → Trial Playbook
- Unfamiliar Project → Validated Domain Playbook
- Important Disagreement → Trial Playbook
- New Domain Learning → Validated Domain Playbook
- Failure Recovery → Validated Domain Playbook

Playbook count is not a quality metric. Retention should be evidence-driven.
