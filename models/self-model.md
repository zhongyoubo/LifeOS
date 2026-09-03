# Self Model

**English** | [简体中文](./self-model.zh-CN.md)

The Self Model is LifeOS's evolving representation of the person. It continuously asks: Who am I, what is my current state, and how am I changing?

## Schema

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

Important Self Model updates should not turn one event into a permanent label. Record:

```yaml
self_hypothesis:
  statement: ""
  evidence: []
  counterevidence: []
  confidence: "low | medium | high"
  source_contexts: []
  review_date: ""
```

Capability, personality, long-term limitations, value changes, recurring patterns, and statements such as “I am / am not suited for this role” especially require an Evidence Gate.

## Principles

Describe rather than permanently label. Distinguish observations, self-evaluations, and external evaluations. Allow contradictions. Record evidence and counterevidence. A single success or failure usually creates a hypothesis, not an identity. Update continuously and preserve earlier versions. Important changes should be re-tested across later behavior or different contexts.
