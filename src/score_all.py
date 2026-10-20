# 全ページの状態の表：判定に使う回の値の一致（ページ単位）、低い方、値の付いた割合、対照、状態。記録がない回は「未実行」。
# 使い方: python3 score_all.py > ../stage_table.tsv
import json, os, re, subprocess, sys, csv
exec(open('judge.py', encoding='utf-8').read())
stats = {r['page']: r for r in csv.DictReader(open('../data/figures.tsv', encoding='utf-8'), delimiter='\t')}
CACHE = {}
def value(d, pat, L):
    f = f'../second/{d}/' + pat.format(L=L)
    if not os.path.exists(f) or 'agent_message' not in open(f, encoding='utf-8').read(): return None
    m = json.load(open(f'../second/{d}/map.json'))
    if L not in m: return None
    if (d, pat) not in CACHE:
        CACHE[(d, pat)] = subprocess.run([sys.executable, 'ind_compare4.py', d], capture_output=True, text=True, env={**os.environ, 'IND_FILE': pat}).stdout
    for ln in CACHE[(d, pat)].splitlines():
        c = ln.split('\t')
        if c[0] == L: return float(c[3].rstrip('%'))
    return None
print('page\truns\tlowest\tvalued\tcontrol\tstage\tsonnet_ref')
for L in sorted(J):
    vals = [(value(d, p, L), lab) for d, p, lab in J[L]]
    got = [v for v, _ in vals if v is not None]
    s = stats.get(L, {})
    valued = float(s.get('valued_all', '0%').rstrip('%')) if s else 0
    ctl = s.get('count_all', '?')
    if not got: stage = '未実行'
    elif min(got) >= 85 and valued >= 95 and ctl == '0': stage = '全文'
    elif min(got) >= 70 and ctl == '0': stage = '部分的'
    else: stage = '未達'
    ref = [value(d, p, L) for d, p, _ in REF.get(L, [])]
    print(f"{L}\t{', '.join(('%.1f%%' % v if v is not None else '未実行') + '（' + lab + '）' for v, lab in vals)}\t{('%.1f%%' % min(got)) if got else '—'}\t{valued}%\t{ctl}/1000\t{stage}\t{', '.join('%.1f%%' % v for v in ref if v is not None)}", flush=True)
