# 新しいページの画像の確かめ（f.39r と同じ決め方）：独立の2回目の2回がそろって私の読みと同じように食い違った箇所を問いにし、
# 字の塊で位置を推定した切り出し（三角の印、2.5倍）と、30問ずつのプロンプトを作る。
# 使い方: python3 mkcheck.py ページ 接頭辞 フォルダ1 フォルダ2 [問いの名前]   例: python3 mkcheck.py v149r am ind5 ind8
import sys, re, json, random, os, numpy as np
from PIL import Image, ImageDraw
SRC = open('ind_compare.py').read()
exec(SRC.split('LET = {')[0])
exec('def canon' + SRC.split('def canon')[1].split('def mine')[0])
exec(('def ai' + SRC.split('def ai')[1].split('nm_eq =')[0]).replace('[a-f]_L', '[a-z]+_L'))
exec('nm_eq =' + SRC.split('nm_eq =')[1].split("print('letter")[0])
exec(open('crops2.py').read().split('def segments')[1].split('for L in')[0].join(['def segments', '']))
L, pre, D1, D2 = sys.argv[1:5]; TAG = sys.argv[5] if len(sys.argv) > 5 else L  # TAG：問いの名前（同じページを2回確かめるとき）
rows = [m.group(1) for m in (re.match(r'c\d+:\s*(.*)', l) for l in open(f'../data/transcription_{L}.txt', encoding='utf-8')) if m]
toks = []  # (行番号, 行内の番号, 名前)
for r, row in enumerate(rows):
    k = 0
    for t in row.split():
        if t.startswith('.') or t == 'au': continue
        k += 1; toks.append((r, k, canon(t)))
x = [t[2] for t in toks]
def page(D):
    ids = json.load(open(f'../second/{D}/map.json'))[L]; A = ai(f'../second/{D}/{L}.jsonl')
    return [t for lid in ids for t in A.get(lid, [])]
al = [align(x, page(D), nm_eq) for D in (D1, D2)]
# 行と行画像の対応（linemap と同じ：c 行 → 一番よく合う行画像）
import difflib
A1 = ai(f'../second/{D1}/{L}.jsonl')
lmap = {}
for r, row in enumerate(rows):
    xr = [canon(t) for t in row.split() if not t.startswith('.')]
    lmap[r] = max(A1, key=lambda k: difflib.SequenceMatcher(None, xr, [canon(t) for t in A1[k]]).ratio())
random.seed(1); Q = []
for i, (r, k, t) in enumerate(toks):
    a, b = al[0].get(i, '-'), al[1].get(i, '-')
    if nm_eq(t, a) or nm_eq(t, b): continue
    if canon(a.split('/')[0]) != canon(b.split('/')[0]): continue
    c = canon(a.split('/')[0])
    if c.startswith('?'): continue
    before = ' '.join(x[max(0, i-3):i]) or '(line start)'; after = ' '.join(x[i+1:i+4]) or '(line end)'
    if c == '-': tc = 'there is no sign here (only a thin separator line, a gap, or nothing)'; tm = f'there is one sign "{t}" here'
    else: tc = f'"{c}"'; tm = f'"{t}"'
    sw = random.random() < 0.5
    Q.append({'id': f'{TAG}-{len(Q)+1:03d}', 'line': lmap[r], 'row': r, 'pos': k, 'before': before, 'after': after,
              'A': 'mine' if sw else 'codex', 'B': 'codex' if sw else 'mine', 'textA': tm if sw else tc, 'textB': tc if sw else tm, 'mine': t, 'codex': c})
# 前に問いにした箇所を除く（環境変数 EXCLUDE に問いのファイルを空白区切りで。行・1回目の名前・2回目の名前が同じで、位置の差が3以内なら同じ箇所とみなす）
import glob as _g
done = []
for f in os.environ.get('EXCLUDE', '').split():
    for f2 in _g.glob(f):
        for q in json.load(open(f2, encoding='utf-8')):
            r0 = q['row'] if 'row' in q else int(q['line'].split('_L')[1]) - 1 - (4 if q['line'].startswith('e_') else 0)
            done.append((r0, q['mine'], q['codex'], q['pos']))
Q = [q for q in Q if not any(r == q['row'] and m == q['mine'] and c == q['codex'] and abs(p - q['pos']) <= 3 for r, m, c, p in done)]
for k, q in enumerate(Q): q['id'] = f'{TAG}-{k+1:03d}'
out = f'../second/check/{TAG}'; os.makedirs(out + '_crops', exist_ok=True)
json.dump(Q, open(f'{out}_questions.json', 'w'), ensure_ascii=False, indent=0)
nrow = {}
for r, k, t in toks: nrow[r] = k
for q in Q:
    im = Image.open(f"../second/img/{q['line']}.jpg").convert('L'); w, h = im.size
    sg = segments(np.asarray(im)); n = nrow[q['row']]; i = q['pos']
    kk = min(len(sg) - 1, int((i - 0.5) / n * len(sg))); c = (sg[kk][0] + sg[kk][1]) / 2
    span = (sg[-1][1] - sg[0][0]) / n * 6; l = int(max(0, c - span)); rr = int(min(w, c + span))
    cr = im.crop((l, 0, rr, h)).resize((int((rr - l) * 2.5), int(h * 2.5)))
    d = ImageDraw.Draw(cr); cx = int((c - l) * 2.5); d.polygon([(cx - 14, 0), (cx + 14, 0), (cx, 24)], fill=0)
    cr.save(f"{out}_crops/{q['id']}.jpg", quality=92)
head = open('../second/check/r39_c0_prompt.md', encoding='utf-8').read().split('Questions:')[0]
chunks = []
for g in range(0, len(Q), 30):
    name = f'{TAG}_c{g//30}'; chunks.append(name); part = Q[g:g+30]
    body = '\n'.join(f"{q['id']} | before: {q['before']} | after: {q['after']} | A: {q['textA']} | B: {q['textB']}" for q in part)
    tail = open('../second/check/r39_c0_prompt.md', encoding='utf-8').read().split('Questions:')[1].split('\n\n', 1)
    open(f'../second/check/{name}_prompt.md', 'w').write(head + 'Questions:\n' + body + '\n\n' + (tail[1] if len(tail) > 1 else ''))
    json.dump([q['id'] for q in part], open(f'../second/check/{name}_ids.json', 'w'))
json.dump(chunks, open(f'{out}_chunks.json', 'w'))
print(len(Q), chunks)
