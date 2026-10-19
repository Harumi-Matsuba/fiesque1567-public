# 値の決まっていない記号に、文字を一つずつ当てて、文字3連の尤度（control.py と同じ模型）がどう変わるかを見る
# 使い方: python3 tryval.py 記号名 [書き起こし…]
import sys, re
from control import build_model, runs, score
from decode import load_key, load_lines
sym = sys.argv[1]; files = sys.argv[2:] or ['../transcription_f039r.txt', '../transcription_f039v.txt', '../transcription_f100.txt']
key, _ = load_key('../key.tsv'); lines = [l for f in files for l in load_lines(f)]
lp = build_model(); res = []
for ch in 'abcdefghilmnopqrstuxyz':
    k2 = dict(key); k2[sym] = ch
    res.append((score(runs(lines, k2), k2, lp), ch))
res.sort(reverse=True)
print(sym, ' '.join(f'{c}:{s:.4f}' for s, c in res[:8]))
