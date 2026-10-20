# mkcheck.py で作った問いの答え（Codex と Sonnet）を集め、2つがそろって Codex の読みを選んだ箇所だけを直す（apply_check39.py と同じ決め方）。
# 使い方: python3 apply_checkp.py ページ [問いの名前] [--apply]。Sonnet の答えは sonnet2_*（1体30枚以下・読み込みが空なら読み直す手順の回）を使う。
import sys, re, json, glob, collections
from decode import load_key
key, _ = load_key('../data/key.tsv')
L = sys.argv[1]; TAG = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else L
def answers(files):
    d = {}
    for f in files:
        for ln in open(f, encoding='utf-8'):
            texts = []
            if f.endswith('.jsonl'):
                o = json.loads(ln)
                if o.get('type') == 'item.completed' and o['item'].get('type') == 'agent_message': texts = o['item']['text'].splitlines()
            else: texts = [ln]
            for row in texts:
                m = re.match(rf'\s*({TAG}-\d+)\s+([ABN])\b', row)
                if m: d[m.group(1)] = m.group(2)
    return d
import os
READERS = os.environ.get('CHECK_READERS', 'codex,sonnet2').split(',')   # 直すのは、ここに挙げた読み手がそろって Codex の読みを選んだ箇所だけ
ANS = {r: answers(sorted(glob.glob(f'../second/check/{r}_{TAG}_c*.' + ('jsonl' if r == 'codex' else 'txt')))) for r in READERS}
Q = json.load(open(f'../second/check/{TAG}_questions.json', encoding='utf-8'))
out = open(f'../second/check/decisions_{TAG}.tsv', 'w', encoding='utf-8')
out.write('id\trow\tpos\tmine\tcodex_reading\t' + '\t'.join(READERS) + '\tdecision\n')
st = collections.Counter(); fixes = collections.defaultdict(dict)
for q in Q:
    side = {'A': q['A'], 'B': q['B'], 'N': 'neither'}
    sides = [side.get(ANS[r].get(q['id']), 'missing') for r in READERS]
    if all(x == 'codex' for x in sides):
        new = q['codex']
        if new == '-': dec = 'fix:delete'
        elif new == 'y': dec = 'keep:y-class'   # y 形は s/p を文脈で書き分けるので、名前を変えない
        elif new in key: dec = 'fix:' + new
        else: dec = 'keep:not-a-key-name'
    elif all(x == 'mine' for x in sides): dec = 'keep:both-mine'
    else: dec = 'keep:split'
    st[dec.split(':')[0] if dec.startswith('fix') else dec] += 1
    out.write(f"{q['id']}\t{q['row']+1}\t{q['pos']}\t{q['mine']}\t{q['codex']}\t" + '\t'.join(sides) + f"\t{dec}\n")
    if dec.startswith('fix'): fixes[q['row']][q['pos']] = dec.split(':', 1)[1]
print(L, TAG, dict(st), {r: len(ANS[r]) for r in READERS}, 'questions', len(Q))
if '--apply' in sys.argv:
    p = f'../data/transcription_{L}.txt'; lines = open(p, encoding='utf-8').read().splitlines(True); r = -1; res = []
    for ln in lines:
        m = re.match(r'(c\d+):\s*(.*)', ln)
        if not m: res.append(ln); continue
        r += 1; n = 0; new = []
        for t in m.group(2).split():
            if not t.startswith('.') and t != 'au':
                n += 1; f = fixes.get(r, {}).get(n)
                if f == 'delete': continue
                if f: t = f
            new.append(t)
        res.append(f'{m.group(1)}: ' + ' '.join(new) + '\n')
    res.append(f'# 2026-10-20：独立の2回目の2回がそろって食い違った箇所を、画像で確かめ（読み手：' + '・'.join(READERS) + '）、読み手がそろって独立の2回目の読みを選んだ箇所だけを直した（second/check/decisions_{TAG}.tsv）。\n')
    open(p, 'w', encoding='utf-8').write(''.join(res)); print('applied', sum(len(v) for v in fixes.values()))
