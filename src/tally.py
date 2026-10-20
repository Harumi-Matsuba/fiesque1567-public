# 独立の2回目（例 sind5）と1回目の食い違いを、記号の型（1回目の名前 → 2回目の名前）ごとに数える。値が同じ組は数えない。
# 使い方: python3 tally.py フォルダ名 [上位の数]
import sys, re, json, collections
SRC = open('ind_compare.py').read()
exec(SRC.split('LET = {')[0])
exec('def canon' + SRC.split('def canon')[1].split('def mine')[0])
exec(('def ai' + SRC.split('def ai')[1].split('nm_eq =')[0]).replace('[a-f]_L', '[a-z]+_L'))
exec('nm_eq =' + SRC.split('nm_eq =')[1].split("print('letter")[0])
D = sys.argv[1]; N = int(sys.argv[2]) if len(sys.argv) > 2 else 25
MAP = json.load(open(f'../second/{D}/map.json')); C = collections.Counter(); tot = 0
for L, ids in MAP.items():
    rows = [m.group(1) for m in (re.match(r'c\d+:\s*(.*)', l) for l in open(f'../data/transcription_{L}.txt', encoding='utf-8')) if m]
    A = ai(f'../second/{D}/{L}.jsonl')
    x = [canon(t) for row in rows for t in row.split() if not t.startswith('.') and t != 'au']
    y = [t for lid in ids for t in A.get(lid, [])]
    al = align(x, y, v_eq)
    for i, t in enumerate(x):
        b = al.get(i, '-'); tot += 1
        if b == '-' or not v_eq(t, b): C[(t, canon(b.split('/')[0]) if b != '-' else '(なし)')] += 1
print('記号', tot, '食い違い', sum(C.values()))
for (a, b), n in C.most_common(N): print(f'{n}\t{a} → {b}')
