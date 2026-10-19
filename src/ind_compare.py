# 独立の2回目（second/ind/*.jsonl、PROMPT2.md）と、私の書き起こし（修正後）を書簡ごとに比べる。
# 記号の並びを編集距離で対応させ、名前の一致と値（key.tsv で当てた字）の一致を数える。
# y 形（私の v と 3p）は形で分けられないので、名前でも値でも一つの組「y」（値 s/p）として扱う。
# 使い方: python3 src/ind_compare.py > second/ind/compare_run1.tsv 2> second/ind/summary_run1.txt
import sys, re, json, collections, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))
from decode import load_key
key, _ = load_key(os.path.join(ROOT, 'data', 'key.tsv'))
D = lambda *a: os.path.join(ROOT, *a)
LET = {'f039r': (D('data', 'transcription_f039r.txt'), 'a', 0), 'f039v': (D('data', 'transcription_f039v.txt'), 'b', 0),
       'f100': (D('data', 'transcription_f100.txt'), 'c', 0), 'f158': (D('data', 'transcription_f158.txt'), 'd', 0),
       'f079': (D('data', 'transcription_f079.txt'), 'e', 4), 'f094': (D('data', 'transcription_f094.txt'), 'f', 1)}
def canon(t):
    t = t.split('/')[0] if t != '//' else t
    if re.fullmatch(r'\d\d', t): t = '=' + t
    if t == 'tt': return 'H#'   # 同じ ŧŧ／# 形（私の初めの名前が tt）
    return 'y' if t in ('v', '3p', 'y') else t
def val(t):
    t = canon(t)
    return 's/p' if t == 'y' else key.get(t, '?' + t)
def mine(path, pg, off):
    d, k = {}, 0
    for ln in open(path, encoding='utf-8'):
        m = re.match(r'c\d+:\s*(.*)', ln)
        if not m: continue
        k += 1
        d[f'{pg}_L{k + off:02d}'] = [canon(t) for t in m.group(1).split() if not t.startswith('.') and t != 'au']
    return d
def ai(path):
    d = {}
    for ln in open(path, encoding='utf-8'):
        o = json.loads(ln)
        if o.get('type') == 'item.completed' and o['item'].get('type') == 'agent_message':
            for row in o['item']['text'].splitlines():
                m = re.match(r'\s*([a-f]_L\d\d)\s+(.*)', row)
                if not m: continue
                s = re.sub(r'\[[^\]]*\]', ' ', m.group(2)).replace('\\|', '|')
                d[m.group(1)] = [t for t in re.findall(r'\?\{[^}]*\}|\S+', s)]
    return d
def align(x, y, eq):
    n, m = len(x), len(y)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + (0 if eq(x[i-1], y[j-1]) else 1))
    i, j, out = n, m, {}
    while i > 0 or j > 0:
        if i > 0 and j > 0 and D[i][j] == D[i-1][j-1] + (0 if eq(x[i-1], y[j-1]) else 1):
            out[i-1] = y[j-1]; i -= 1; j -= 1
        elif i > 0 and D[i][j] == D[i-1][j] + 1: out[i-1] = '-'; i -= 1
        else: j -= 1
    return out
nm_eq = lambda a, b: any(a == canon(z) for z in (b.split('/') if b != '//' else [b]))
v_eq = lambda a, b: any(val(a) == val(z) for z in (b.split('/') if b != '//' else [b]))
print('letter\tline\tpos\tmine\tcodex\tname_ok\tvalue_ok')
tot = collections.Counter(); nm = collections.Counter(); vm = collections.Counter(); dis = collections.Counter()
for L, (p, pg, off) in LET.items():
    M = mine(p, pg, off)
    try: A = ai(D('second', 'ind', f'{L}.jsonl'))
    except FileNotFoundError: continue
    for lid, x in sorted(M.items()):
        y = A.get(lid, [])
        al_n = align(x, y, nm_eq); al_v = align(x, y, v_eq)
        for i, t in enumerate(x):
            a, b = al_n.get(i, '-'), al_v.get(i, '-')
            okn = a != '-' and nm_eq(t, a); okv = b != '-' and v_eq(t, b)
            tot[L] += 1; nm[L] += okn; vm[L] += okv
            if not okv: dis[(val(t), 'なし' if b == '-' else val(b))] += 1
            if not (okn and okv): print(f'{L}\t{lid}\t{i+1}\t{t}\t{b}\t{int(okn)}\t{int(okv)}')
for L in LET:
    if tot[L]: print(f'# {L}: 記号 {tot[L]}、名前の一致 {nm[L]}（{nm[L]/tot[L]:.1%}）、値の一致 {vm[L]}（{vm[L]/tot[L]:.1%}）', file=sys.stderr)
T = sum(tot.values())
if T: print(f'# 計: 記号 {T}、名前 {sum(nm.values())/T:.1%}、値 {sum(vm.values())/T:.1%}', file=sys.stderr)
print('# 値の食い違い上位:', dis.most_common(15), file=sys.stderr)
