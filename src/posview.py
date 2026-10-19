# 書き起こしの記号の位置（行と番号）から、行画像のおおよその位置を切り出して並べる（目視の確かめ用）
# 行画像は img/<id>.jpg（このリポジトリには含めない）。
# 使い方: python3 posview.py 出力接頭辞 lid:番号 …（番号は無効字を除いた記号の通し番号、1始まり）
import sys, os, numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
exec(open(os.path.join(ROOT, 'src', 'xcompare.py'), encoding='utf-8').read().split('M = {}')[0])
M = {}
for pg, p in PAGES.items(): M.update(mine(p, pg))
pre = sys.argv[1]; ps = []
for spec in sys.argv[2:]:
    lid, i = spec.split(':'); i = int(i); n = len(M[lid])
    im = Image.open(os.path.join(ROOT, 'img', f'{lid}.jpg')); w, h = im.size
    a = np.asarray(im.convert('L')); cols = np.where((a[40:h-30] < 110).sum(0) > 2)[0]; x0, x1 = cols.min(), cols.max()
    c = x0 + (x1 - x0) * (i - 0.5) / n
    p = im.crop((int(c - 230), 20, int(c + 230), h - 10)).resize((920, int((h - 30) * 2)))
    ImageDraw.Draw(p).text((5, 5), f'{spec}  {" ".join(M[lid][max(0,i-4):i+3])}', fill=0); ps.append(p)
for k in range(0, len(ps), 6):
    g = ps[k:k+6]; o = Image.new('L', (920, sum(p.height + 6 for p in g)), 0); y = 0
    for p in g: o.paste(p, (0, y)); y += p.height + 6
    o.save(f'{pre}{k//6}.png')
