# 直した箇所のうち、指定した問いの id を元の読みに戻す（同じ行で前に消した箇所の分だけ位置をずらす）。
# 使い方: python3 revert_ids.py ページ 問いの名前 id...
import sys, csv, re
L, T, ids = sys.argv[1], sys.argv[2], sys.argv[3:]
rows = list(csv.DictReader(open(f'../second/check/decisions_{T}.tsv', encoding='utf-8'), delimiter='\t'))
by = {r['id']: r for r in rows}
p = f'../data/transcription_{L}.txt'; lines = open(p, encoding='utf-8').read().splitlines(True); k = -1; out = []
for ln in lines:
    m = re.match(r'(c\d+):\s*(.*)', ln)
    if not m: out.append(ln); continue
    k += 1; toks = m.group(2).split()
    todo = sorted([by[i] for i in ids if int(by[i]['row']) - 1 == k], key=lambda r: -int(r['pos']))
    for r in todo:
        pos = int(r['pos']); dels = sum(1 for x in rows if x['decision'] == 'fix:delete' and int(x['row']) - 1 == k and int(x['pos']) < pos)
        idx = [j for j, t in enumerate(toks) if not t.startswith('.') and t != 'au']; cur = pos - dels
        if r['decision'] == 'fix:delete':
            at = idx[cur - 1] if cur - 1 < len(idx) else len(toks); toks.insert(at, r['mine']); print(r['id'], 'reinsert', r['mine'])
        else:
            j = idx[cur - 1]; new = r['decision'].split(':', 1)[1]
            assert toks[j] == new, (r['id'], toks[j], new); toks[j] = r['mine']; print(r['id'], new, '->', r['mine'])
    out.append(f'{m.group(1)}: ' + ' '.join(toks) + '\n')
out.append(f"# 2026-10-20：上の確かめで直した箇所のうち、追加の読み手の Codex が1回目の読みを選んだ {len(ids)} か所（{T}）は、読み手がそろわないので元に戻した。\n")
open(p, 'w', encoding='utf-8').write(''.join(out))
