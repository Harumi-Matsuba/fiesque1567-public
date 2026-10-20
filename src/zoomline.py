# 行画像1枚を3つに分け（重なり60px）、1.6倍にして縦に並べる（目視の書き起こし用）
# 使い方: python3 zoomline.py 行画像 出力
import sys
from PIL import Image
im = Image.open(sys.argv[1]); w, h = im.size; k = 3; s = w // k
parts = [im.crop((max(0, i * s - 60), 0, min(w, (i + 1) * s + 60), h)) for i in range(k)]
parts = [p.resize((int(p.width * 1.6), int(h * 1.6))) for p in parts]
o = Image.new('L', (max(p.width for p in parts), sum(p.height + 8 for p in parts)), 0); y = 0
for p in parts: o.paste(p, (0, y)); y += p.height + 8
o.save(sys.argv[2])
