# ページの領域から行の中心を自動で求め（3つの縦の帯の山を合わせる）、行画像（second/img/<接頭辞>_Lnn.jpg）と4行ずつの一覧（scratchpad）を作る
# 使い方: python3 autopage.py 画像 接頭辞 x0 x1 y0 y1 出力の接頭辞
import sys, subprocess, numpy as np
from PIL import Image
src, pre, x0, x1, y0, y1, out = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7]), sys.argv[7]
im = Image.open(src).convert('L')
def peaks(a, b):
    arr = np.asarray(im.crop((a, y0, b, y1)), dtype=float)
    s = np.convolve((arr < 110).sum(1).astype(float), np.ones(31) / 31, 'same')
    P = []
    for i in range(45, len(s) - 46):
        if s[i] == s[i-45:i+46].max() and s[i] > s.mean() * 0.4:
            if not P or i - P[-1] > 70: P.append(i)
    return [y0 + p for p in P]
w = (x1 - x0) // 6
P = peaks(x0 + w // 2, x0 + w * 2)
print(len(P), P)
subprocess.run(['python3', 'trackline.py', src, '../second/img', pre, str(x0), str(x1)] + [str(p) for p in P], check=True)
files = [f'../second/img/{pre}_L{k:02d}.jpg' for k in range(1, len(P) + 1)]
for g in range(0, len(files), 4):
    subprocess.run(['python3', 'sheet.py', f'{out}{g//4:02d}.png'] + files[g:g+4], check=True)
