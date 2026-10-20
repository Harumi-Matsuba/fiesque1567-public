# 画像の確かめで、Codex（追加の読み手）の答えを、Sonnet 2人で決めた結果と突き合わせる。直した箇所と直さなかった箇所のそれぞれで、Codex が何を選んだかを数える。
# 使い方: python3 cmp_readers.py 問いの名前...
import sys, csv, json, re, glob, collections
def ans(f):
    d = {}
    for ln in open(f, encoding='utf-8'):
        o = json.loads(ln)
        if o.get('type') == 'item.completed' and o['item'].get('type') == 'agent_message':
            for row in o['item']['text'].splitlines():
                m = re.match(r'\s*(\S+-\d+)\s+([ABN])\b', row)
                if m: d[m.group(1)] = m.group(2)
    return d
for T in sys.argv[1:]:
    Q = {q['id']: q for q in json.load(open(f'../second/check/{T}_questions.json', encoding='utf-8'))}
    C = {}
    for f in glob.glob(f'../second/check/codex_{T}_c*.jsonl'): C.update(ans(f))
    dec = {r['id']: r['decision'] for r in csv.DictReader(open(f'../second/check/decisions_{T}.tsv', encoding='utf-8'), delimiter='\t')}
    cnt = collections.Counter()
    for i, q in Q.items():
        c = {'A': q['A'], 'B': q['B'], 'N': 'neither'}.get(C.get(i), 'missing')
        d = 'fixed' if dec.get(i, '').startswith('fix') else 'kept'
        cnt[(d, c)] += 1
    print(T, len(Q), dict(sorted(cnt.items())))
