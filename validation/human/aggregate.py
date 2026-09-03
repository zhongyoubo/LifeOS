#!/usr/bin/env python3
"""Aggregate LifeOS Human Validation JSONL cases.

Usage:
  python validation/human/aggregate.py cases/*.json > summary.json
  python validation/human/aggregate.py cases/*.jsonl > summary.json
"""
import json, sys
from pathlib import Path
from collections import Counter


def load(paths):
    rows=[]
    for p in paths:
        text=Path(p).read_text(encoding='utf-8')
        if p.endswith('.jsonl'):
            rows.extend(json.loads(x) for x in text.splitlines() if x.strip())
        else:
            rows.append(json.loads(text))
    return rows


def mean(xs):
    return round(sum(xs)/len(xs), 3) if xs else None


def rate(n, d):
    return round(n/d, 3) if d else None


def main():
    if len(sys.argv) < 2:
        raise SystemExit('Provide one or more .json/.jsonl case files')
    rows=load(sys.argv[1:])
    followed=[r for r in rows if r.get('follow_up_7d')]

    clarity_delta=[r['immediate']['clarity']-r['before']['clarity'] for r in rows]
    decision_delta=[r['immediate']['decision_confidence']-r['before']['decision_confidence'] for r in rows]
    next_action_ready=sum(bool(r.get('session',{}).get('next_action','').strip()) for r in rows)
    follow_positive=sum(r['follow_up_7d']['follow_through'] in ('yes','partial') for r in followed)
    transfer_positive=sum(r['follow_up_7d'].get('learning_transfer') in ('yes','partial') for r in followed)
    continue_positive=sum(r['follow_up_7d'].get('can_continue_without_lifeos') in ('yes','partial') for r in followed)

    result={
      'participants': len(set(r['participant_id'] for r in rows)),
      'cases': len(rows),
      'followed_up_cases': len(followed),
      'metrics': {
        'clarity_delta_mean': mean(clarity_delta),
        'decision_confidence_delta_mean': mean(decision_delta),
        'context_fit_mean': mean([r['immediate']['context_fit'] for r in rows]),
        'actionability_mean': mean([r['immediate']['actionability'] for r in rows]),
        'autonomy_mean': mean([r['immediate']['autonomy'] for r in rows]),
        'process_cost_mean': mean([r['immediate']['process_cost'] for r in rows]),
        'would_use_again_mean': mean([r['immediate']['would_use_again'] for r in rows]),
        'next_action_rate': rate(next_action_ready, len(rows)),
        'follow_through_yes_or_partial_rate': rate(follow_positive, len(followed)),
        'learning_transfer_yes_or_partial_rate': rate(transfer_positive, len(followed)),
        'can_continue_without_lifeos_yes_or_partial_rate': rate(continue_positive, len(followed))
      },
      'outcomes': dict(Counter(r['follow_up_7d']['outcome_direction'] for r in followed)),
      'classifications': dict(Counter((r.get('research') or {}).get('classification','UNCLASSIFIED') for r in rows)),
      'severity': dict(Counter((r.get('research') or {}).get('severity','UNCLASSIFIED') for r in rows))
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
