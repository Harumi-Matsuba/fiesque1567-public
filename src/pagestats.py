# ページごとの数字（行・記号・値の付いた割合（表＋推定／表だけ）・対照（表＋推定、表だけ））を TSV で出す。
# 使い方: python3 pagestats.py > ../pages_stats.tsv
import glob, re, subprocess, sys, os
print('page\tlines\tsigns\tvalued_all\tvalued_table\ttrue_all\tmax_all\tcount_all\ttrue_table\tmax_table\tcount_table')
for f in sorted(glob.glob('../data/transcription_*.txt')):
    p = os.path.basename(f)[14:-4]
    n = sum(1 for l in open(f, encoding='utf-8') if re.match(r'c\d+:', l))
    def dec(*a):
        o = subprocess.run([sys.executable, 'decode.py', '../data/key.tsv', f, *a], capture_output=True, text=True).stdout
        m = re.search(r'記号 (\d+) 個のうち.*?(\d+) 個（([\d.]+)%）', o); return m
    a, t = dec(), dec('--table-only')
    def ctl(*a):
        o = subprocess.run([sys.executable, 'control.py', '../data/key.tsv', f, '1000', *a], capture_output=True, text=True).stdout
        tv = re.search(r'本物の鍵: (-[\d.]+)', o).group(1); mx = re.search(r'最大 (-[\d.]+)', o).group(1); c = re.search(r'本物以上になった回数: (\d+)', o).group(1)
        return tv, mx, c
    ca, ct = ctl(), ctl('--table-only')
    print(f'{p}\t{n}\t{a.group(1)}\t{a.group(3)}%\t{t.group(3)}%\t' + '\t'.join(ca) + '\t' + '\t'.join(ct), flush=True)
