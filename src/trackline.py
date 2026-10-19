# 行を左から右へたどって（窓ごとに墨の量の山を探して）傾きや揺れを補い、1行1枚の画像にする。
# 使い方: python3 trackline.py 画像 出力フォルダ 接頭辞 x0 x1 y_start1 y_start2 …（各行の左端での中心 y）
import sys, os, numpy as np
from PIL import Image
src, outd, pre, x0, x1 = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
ys = [int(v) for v in sys.argv[6:]]
im = Image.open(src).convert('L'); a = np.asarray(im, dtype=float); ink = (a < 120).astype(float)
os.makedirs(outd, exist_ok=True); H = 170; win = 150
for k, y in enumerate(ys, 1):
    out = Image.new('L', (x1 - x0, H), 255); yc = y
    for xs in range(x0, x1, win):
        band = ink[yc - 45: yc + 46, xs: xs + win].sum(1)
        if band.sum() > 30:
            sm = np.convolve(band, np.ones(15) / 15, 'same'); yc = int(0.6 * yc + 0.4 * (yc - 45 + int(sm.argmax())))
        out.paste(im.crop((xs, yc - H // 2, min(xs + win, x1), yc + H // 2)), (xs - x0, 0))
    out.save(f'{outd}/{pre}_L{k:02d}.jpg', quality=92)
