# 原寸画像から行の帯を切り出し、左右2分割を縦に並べた画像を作る（目視の書き起こし用）。
# 使い方: python3 strips.py ../gallica/full/v043.jpg 出力接頭辞 x0 x1 y_first step n [h]
#   y_first：最初の行の中心の y、step：行の間隔、n：行数、h：帯の高さ（既定 160）
import sys
from PIL import Image
src, pre, x0, x1, y1, step, n = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:8])
h = int(sys.argv[8]) if len(sys.argv) > 8 else 160
im = Image.open(src).convert('L')
mid = (x0 + x1) // 2
for half, (a, b) in enumerate([(x0, mid + 60), (mid - 60, x1)]):
    strips = [im.crop((a, y1 + i * step - h // 2, b, y1 + i * step + h // 2)) for i in range(n)]
    out = Image.new('L', (b - a, n * (h + 6)), 0)
    for i, s in enumerate(strips):
        out.paste(s, (0, i * (h + 6)))
    out.save(f'{pre}_h{half}.png')
