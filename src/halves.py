# Sonnet 用に、行画像を左右半分（重なり 60px）に分け、1.25倍にして保存する（Sonnet では長い行画像が縮小されて細部が消えるため）。
# 使い方: python3 halves.py 行id...   出力: ../second/img_half/<id>a.jpg・<id>b.jpg
import sys, os
from PIL import Image
os.makedirs('../second/img_half', exist_ok=True)
for i in sys.argv[1:]:
    im = Image.open(f'../second/img/{i}.jpg'); w, h = im.size; m = w // 2
    for s, (a, b) in zip('ab', [(0, m + 30), (m - 30, w)]):
        p = im.crop((a, 0, b, h)); p = p.resize((int(p.width * 1.25), int(h * 1.25)))
        p.save(f'../second/img_half/{i}{s}.jpg', quality=92)
