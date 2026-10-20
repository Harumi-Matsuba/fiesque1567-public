# f.39r の2回の独立の2回目（ind2）がそろって食い違った90か所の画像の確かめ（r39）。apply_check.py と同じ決め方。
# 使い方: python3 apply_check.py [--apply]（--apply なしは一覧だけ出す）
import sys, re, json, collections
from decode import load_key
key, _ = load_key('../data/key.tsv')
FILES = {'r39': ('../data/transcription_f039r.txt', 'a', 0)}
import glob
def answers_codex(L):
    d = {}
    for f in sorted(glob.glob(f'../second/check/codex_{L}_c*.jsonl')):
      for ln in open(f, encoding='utf-8'):
        o = json.loads(ln)
        if o.get('type') == 'item.completed' and o['item'].get('type') == 'agent_message':
            for row in o['item']['text'].splitlines():
                m = re.match(r'\s*(r\d+-\d+)\s+([ABN])\b\s*(.*)', row)
                if m: d[m.group(1)] = (m.group(2), m.group(3))
    return d
def answers_sonnet(L):
    d = {}
    rows = [r for f in sorted(glob.glob(f'../second/check/sonnet_{L}_c*.txt')) for r in open(f, encoding='utf-8')]
    for row in rows:
        m = re.match(r'\s*(r\d+-\d+)\s+([ABN])\b\s*(.*)', row)
        if m: d[m.group(1)] = (m.group(2), m.group(3))
    return d
out = open('../second/check/decisions39.tsv', 'w', encoding='utf-8')
out.write('id\tline\tpos\tmine\trun1\tcodex_check\tsonnet_check\tdecision\n')
stats = collections.Counter(); fixes = collections.defaultdict(dict)
for L in FILES:
    q = json.load(open(f'../second/check/{L}_questions.json', encoding='utf-8'))
    C = answers_codex(L); S = answers_sonnet(L)
    for x in q:
        side = {'A': x['A'], 'B': x['B'], 'N': 'neither'}
        c = side[C[x['id']][0]] if x['id'] in C else 'missing'
        s = side[S[x['id']][0]] if x['id'] in S else 'missing'
        if c == s == 'codex':
            new = x['codex']
            if new == '-': dec = 'fix:delete'
            elif new == 'y': dec = 'fix:v'
            elif re.fullmatch(r'\d\d', new) and '=' + new in key: dec = 'fix:=' + new
            elif new in key: dec = 'fix:' + new
            else: dec = 'keep:not-a-key-name'
        elif c == s == 'mine': dec = 'keep:both-mine'
        else: dec = 'keep:split'
        stats[(L, dec.split(':')[0] if not dec.startswith('keep') else dec)] += 1
        out.write(f"{x['id']}\t{x['line']}\t{x['pos']}\t{x['mine']}\t{x['codex']}\t{c}\t{s}\t{dec}\n")
        if dec.startswith('fix'): fixes[x['line']][x['pos']] = dec.split(':', 1)[1]
for k, v in sorted(stats.items()): print(k, v)
if '--apply' in sys.argv:
    for L, (p, pg, off) in FILES.items():
        lines = open(p, encoding='utf-8').read().splitlines(True); res = []; k = 0
        for ln in lines:
            m = re.match(r'(c\d+):\s*(.*)', ln)
            if not m: res.append(ln); continue
            k += 1; lid = f'{pg}_L{k + off:02d}'; n = 0; new = []
            for t in m.group(2).split():
                if not t.startswith('.') and t != 'au':
                    n += 1
                    f = fixes.get(lid, {}).get(n)
                    if f == 'delete': continue
                    if f: t = f
                new.append(t)
            res.append(f'{m.group(1)}: ' + ' '.join(new) + '\n')
        res.append('# 2026-10-20：独立の2回目（ind2 の2回）がそろって食い違った箇所を、Codex と Claude Sonnet が別々に画像で確かめ、2つがそろって run1 の読みを選んだ箇所だけを直した（second/check/decisions39.tsv）。\n')
        open(p, 'w', encoding='utf-8').write(''.join(res))
    print('applied')
