# 独立の2回目（second/ind4 など）と1回目を、ページ単位で比べる。行の対応を決めず、ページの記号を全部つないで編集距離で並べる。
# 使い方：python3 ind_compare4.py [フォルダ名 (既定 ind4)]。記録の名前が違うときは環境変数 IND_FILE（例 '{L}_run3.jsonl'）。比べ方（canon・値の一致）は ind_compare.py と同じ。
import sys, re, json, collections, os
SRC = open('ind_compare.py').read()
exec(SRC.split('LET = {')[0])
exec('def canon' + SRC.split('def canon')[1].split('def mine')[0])
exec(('def ai' + SRC.split('def ai')[1].split('nm_eq =')[0]).replace('[a-f]_L', '[a-z]+_L'))
exec('nm_eq =' + SRC.split('nm_eq =')[1].split("print('letter")[0])
D = sys.argv[1] if len(sys.argv) > 1 else 'ind4'
MAP = json.load(open(f'../second/{D}/map.json'))
tot = collections.Counter(); nm = collections.Counter(); vm = collections.Counter()
for L, ids in MAP.items():
    rows = [m.group(1) for m in (re.match(r'c\d+:\s*(.*)', l) for l in open(f'../data/transcription_{L}.txt', encoding='utf-8')) if m]
    try: A = ai(f'../second/{D}/' + os.environ.get('IND_FILE', '{L}.jsonl').format(L=L))
    except FileNotFoundError: continue
    if not A: continue
    x = [canon(t) for row in rows for t in row.split() if not t.startswith('.') and t != 'au']
    y = [t for lid in ids for t in A.get(lid, [])]
    al_n = align(x, y, nm_eq); al_v = align(x, y, v_eq)
    for i, t in enumerate(x):
        a, b = al_n.get(i, '-'), al_v.get(i, '-')
        tot[L] += 1; nm[L] += a != '-' and nm_eq(t, a); vm[L] += b != '-' and v_eq(t, b)
for L in MAP:
    if tot[L]: print(f'{L}\t{tot[L]}\t{nm[L]/tot[L]:.1%}\t{vm[L]/tot[L]:.1%}')
T = sum(tot.values())
if T: print(f'計\t{T}\t{sum(nm.values())/T:.1%}\t{sum(vm.values())/T:.1%}')
