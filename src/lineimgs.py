# 2回目の書き起こし用に、1行1枚の行画像を作る（second/img/<id>.jpg）。
# 行の位置は transcription_*.txt を作ったときの strips.py の値と同じ（f.39v は右半分が上にずれるので、行を左右2枚に分けずに傾きを補う）。
import sys
from PIL import Image
def rows(src, prefix, x0, x1, y1, step, n, h=170, slope=0.0, first=1):
    im = Image.open(src).convert('L')
    for i in range(n):
        yc = y1 + i * step
        # 傾き：右端で slope*(x1-x0) だけ上にずれる。帯を細かい縦切りで集めて平らにする
        W = x1 - x0; out = Image.new('L', (W, h), 255); seg = 100
        for xs in range(0, W, seg):
            dy = int(round(slope * xs))
            out.paste(im.crop((x0 + xs, yc - dy - h // 2, x0 + min(xs + seg, W), yc - dy + h // 2)), (xs, 0))
        out.save(f'second/img/{prefix}_L{i + first:02d}.jpg', quality=92)
def rows_at(src, prefix, x0, x1, ys, h=170, slope=0.0):
    for k, y in enumerate(ys):
        rows(src, prefix, x0, x1, y, 0, 1, h=h, slope=slope, first=k + 1)
# 行の中心は、左側の帯の墨の量（横方向の和）の山から求めた（2026-10-20、28・19・27 行で書き起こしの行数と一致）
A = [1204, 1317, 1427, 1538, 1646, 1777, 1888, 2011, 2137, 2254, 2369, 2490, 2618, 2757, 2885, 3015, 3150, 3282, 3408, 3543, 3679, 3807, 3932, 4053, 4182, 4317, 4451, 4589]
B = [y + 15 for y in [1124, 1252, 1381, 1498, 1626, 1750, 1872, 1995, 2108, 2234, 2368, 2491, 2628, 2763, 2899, 3021, 3157, 3291, 3440]]  # x 900–1500 の山。右へ 1800px で約 80 上がる
C = [590, 718, 840, 968, 1099, 1227, 1360, 1482, 1610, 1743, 1884, 2017, 2152, 2286, 2411, 2549, 2680, 2810, 2948, 3078, 3207, 3360, 3494, 3647, 3783, 3924, 4059]
rows_at('gallica/full/v043.jpg', 'a', 4250, 7200, A)                    # f.39r c02–c29 → a_L01–a_L28
rows_at('gallica/full/v044.jpg', 'b', 850, 3900, B, slope=80 / 1800)  # f.39v c01–c19 → b_L01–b_L19
rows_at('gallica/full/v105.jpg', 'c', 4400, 6750, C, h=150)            # f.100r c01–c27 → c_L01–c_L27（c_L01 は平文の行の右端）
