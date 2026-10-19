# 私の書き起こし（transcription_*.txt）と、Codex の書き起こし（second/out/pass*_<頁>.jsonl）を行ごとに並べて比べる。
# 記号の並びを編集距離で対応させ、一致・食い違い・3回の多数を数える。
# 無効字（私の .xxx と au、Codex の [..]）は比べない。
# 使い方: python3 src/xcompare.py > 出力.tsv（集計は標準エラー）。前の照合（second/run0）用。書き起こしはその後に直したので、いまの data/ と比べると second/run0 の数字とは合わない
import sys, re, json, glob, collections, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = {'a': os.path.join(ROOT, 'data', 'transcription_f039r.txt'), 'b': os.path.join(ROOT, 'data', 'transcription_f039v.txt'), 'c': os.path.join(ROOT, 'data', 'transcription_f100.txt')}
def mine(path, pg):
    d, k = {}, 0
    for ln in open(path, encoding='utf-8'):
        m = re.match(r'c\d+:\s*(.*)', ln)
        if not m: continue
        k += 1
        d[f'{pg}_L{k:02d}'] = [t for t in m.group(1).split() if not t.startswith('.') and t != 'au']
    return d
def ai(path):
    d = {}
    for ln in open(path, encoding='utf-8'):
        o = json.loads(ln)
        if o.get('type') == 'item.completed' and o['item'].get('type') == 'agent_message':
            for row in o['item']['text'].splitlines():
                m = re.match(r'\s*([abc]_L\d\d)\s+(.*)', row)
                if not m: continue
                s = re.sub(r'\[[^\]]*\]', ' ', m.group(2)).replace('\\|', '|')
                d[m.group(1)] = [('=' + t if re.fullmatch(r'\d\d', t) else t) for t in re.findall(r'\?\{[^}]*\}|\S+', s)]  # 2桁の数は = を付けて私の名前にそろえる
    return d
def match(a, b): return a == b or a in b.split('/')
def align(x, y):
    n, m = len(x), len(y)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + (0 if match(x[i-1], y[j-1]) else 1))
    i, j, out = n, m, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and D[i][j] == D[i-1][j-1] + (0 if match(x[i-1], y[j-1]) else 1):
            out.append((i-1, y[j-1])); i -= 1; j -= 1
        elif i > 0 and D[i][j] == D[i-1][j] + 1:
            out.append((i-1, '-')); i -= 1
        else: j -= 1
    return dict(out)
M = {}
for pg, p in PAGES.items(): M.update(mine(p, pg))
passes = sorted({re.search(r'pass(\d)', f).group(1) for f in glob.glob(os.path.join(ROOT, 'second', 'run0', 'pass*_*.jsonl'))})
A = []
for ps in passes:
    d = {}
    for f in glob.glob(os.path.join(ROOT, 'second', 'run0', f'pass{ps}_*.jsonl')): d.update(ai(f))
    A.append(d)
tot = 0; agree = [0] * len(A); allag = 0; maj = collections.Counter(); pairs = collections.Counter()
print('line\tpos\tmine\t' + '\t'.join(f'ai{k+1}' for k in range(len(A))) + '\tflag')
for lid in sorted(M):
    x = M[lid]; al = [align(x, a.get(lid, [])) for a in A]
    for i, t in enumerate(x):
        tot += 1; vs = [a.get(i, '-') for a in al]; ok = [match(t, v) for v in vs]
        for k, o in enumerate(ok): agree[k] += o
        if all(ok): allag += 1; continue
        flag = ''
        if sum(ok) <= len(A) // 2:
            c = collections.Counter(v for v, o in zip(vs, ok) if not o).most_common(1)
            if c and c[0][1] >= 2: flag = 'MAJ:' + c[0][0]; maj[(t, c[0][0])] += 1
            else: flag = 'split'
        print(f'{lid}\t{i+1}\t{t}\t' + '\t'.join(vs) + f'\t{flag}')
print(f'# 記号 {tot}、各回の一致 {agree}（{[round(a/tot*100,1) for a in agree]}%）、全回一致 {allag}（{allag/tot:.1%}）、多数が別の読み {sum(maj.values())}', file=sys.stderr)
for (a, b), n in maj.most_common(30): print(f'#   {a} → {b}: {n}', file=sys.stderr)
