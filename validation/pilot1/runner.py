#!/usr/bin/env python3
import argparse, json, os, subprocess, sys
from pathlib import Path

BASELINE_SYSTEM = "You are a capable general AI assistant. Answer naturally, practically, and respectfully. Do not use or imitate LifeOS materials or terminology. Preserve user autonomy and avoid unnecessary process."


def load_cases(path):
    with open(path, encoding='utf-8') as f:
        for line in f:
            line=line.strip()
            if line:
                yield json.loads(line)


def load_skill(path):
    return Path(path).read_text(encoding='utf-8')


def call_command(cmd_template, system_prompt, user_prompt, case_id, condition):
    env=os.environ.copy()
    env['LIFEOS_SYSTEM_PROMPT']=system_prompt
    env['LIFEOS_USER_PROMPT']=user_prompt
    env['LIFEOS_CASE_ID']=case_id
    env['LIFEOS_CONDITION']=condition
    cmd=cmd_template.format(case_id=case_id, condition=condition)
    p=subprocess.run(cmd, shell=True, text=True, capture_output=True, env=env)
    if p.returncode != 0:
        raise RuntimeError(f"runner command failed for {case_id}/{condition}: {p.stderr}")
    return p.stdout.strip()


def main():
    ap=argparse.ArgumentParser(description='Generate paired Baseline/LifeOS outputs for Pilot-1.')
    ap.add_argument('--cases', default='validation/pilot1/cases.jsonl')
    ap.add_argument('--skill', default='skills/lifeos/SKILL.md')
    ap.add_argument('--out', default='validation/pilot1/raw_outputs.jsonl')
    ap.add_argument('--command', required=True, help='Command that reads LIFEOS_SYSTEM_PROMPT and LIFEOS_USER_PROMPT env vars and prints one answer to stdout.')
    ap.add_argument('--model', required=True, help='Model identifier recorded for audit.')
    ap.add_argument('--max-cases', type=int)
    args=ap.parse_args()

    skill=load_skill(args.skill)
    lifeos_system = BASELINE_SYSTEM + "\n\nApply the following frozen LifeOS v0.1.1 skill as runtime guidance:\n\n" + skill
    cases=list(load_cases(args.cases))
    if args.max_cases:
        cases=cases[:args.max_cases]

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out,'w',encoding='utf-8') as out:
        for case in cases:
            cid=case['case_id']; prompt=case['prompt']
            baseline=call_command(args.command, BASELINE_SYSTEM, prompt, cid, 'baseline')
            lifeos=call_command(args.command, lifeos_system, prompt, cid, 'lifeos')
            record={
                'case_id': cid,
                'title': case.get('title'),
                'prompt': prompt,
                'model': args.model,
                'baseline': baseline,
                'lifeos': lifeos
            }
            out.write(json.dumps(record, ensure_ascii=False)+'\n')
            print(f'generated {cid}', file=sys.stderr)

if __name__ == '__main__':
    main()
