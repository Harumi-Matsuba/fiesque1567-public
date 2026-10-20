# 食い違いの箇所の切り出し（第2版）：行画像の墨の縦の切れ目で字の塊に分け、記号の番号を塊の番号に比例させて位置を推定する。
# 推定位置に三角の印を付け、前後およそ6記号分を2.5倍に拡大する。
import json, numpy as np
from PIL import Image, ImageDraw
exec(open('ind_compare.py').read().split("nm_eq =")[0])
M = {}
for L, (p, pg, off) in LET.items(): M.update(mine(p, pg, off))
def segments(a):
    h = a.shape[0]; core = a[int(h*0.25):int(h*0.75)]
    ink = (core < 120).sum(0); on = ink > 1
    segs = []; s = None
    for x, v in enumerate(on):
        if v and s is None: s = x
        if not v and s is not None:
            if x - s >= 4: segs.append((s, x))
            s = None
    if s is not None: segs.append((s, len(on)))
    # 近すぎる塊はつなぐ
    out = []
    for s, e in segs:
        if out and s - out[-1][1] < 6: out[-1] = (out[-1][0], e)
        else: out.append((s, e))
    return out
for L in ['f039r', 'f039v', 'f079']:
    q = json.load(open(f'../second/check/{L}_questions.json', encoding='utf-8'))
    for x in q:
        lid = x['line']; i = x['pos']; n = len(M[lid])
        im = Image.open(f'../second/img/{lid}.jpg').convert('L'); w, h = im.size
        sg = segments(np.asarray(im))
        k = min(len(sg) - 1, int((i - 0.5) / n * len(sg)))
        c = (sg[k][0] + sg[k][1]) / 2
        span = (sg[-1][1] - sg[0][0]) / n * 6
        l = int(max(0, c - span)); r = int(min(w, c + span))
        cr = im.crop((l, 0, r, h)).resize((int((r - l) * 2.5), int(h * 2.5)))
        d = ImageDraw.Draw(cr); cx = int((c - l) * 2.5)
        d.polygon([(cx - 14, 0), (cx + 14, 0), (cx, 24)], fill=0)
        cr.save(f"../second/check/crops/{x['id']}.jpg", quality=92)
