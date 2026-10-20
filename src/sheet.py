# 1行1枚の画像を、左右2分割して縦に並べた一覧にする
import sys
from PIL import Image
out, files = sys.argv[1], sys.argv[2:]
rows = []
for f in files:
    im = Image.open(f); w = im.width; m = w // 2
    rows += [im.crop((0, 0, m + 60, im.height)), im.crop((m - 60, 0, w, im.height))]
W = max(r.width for r in rows); o = Image.new('L', (W, sum(r.height + 6 for r in rows)), 0); y = 0
for r in rows: o.paste(r, (0, y)); y += r.height + 6
o.save(out)
