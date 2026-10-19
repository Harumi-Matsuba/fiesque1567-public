# 対照実験：表の文字記号の値をかき混ぜた鍵と、本物の鍵とで、平文のフランス語らしさを比べる。
# フランス語らしさ＝文字3連の対数尤度の平均（wordfreq の仏語上位5万語を頻度で重み付けして作る）。
# 単語記号（=que、.3. など）は採点から外し、1文字の記号の並びだけを採点する。
# fiesque1567 用の変更：表の nulls（値 (null)）は区切りにせず読み飛ばす。
# 使い方: python3 control.py ../key.tsv ../transcription_f218r.txt [試行回数] [--table-only]
#   --table-only : 文脈から推定した記号（inferred）を外し、表にある記号だけで比べる
import sys, math, random, collections
from wordfreq import top_n_list, word_frequency
from decode import load_key, load_lines, norm

def build_model():
    tri = collections.Counter(); bi = collections.Counter()
    for w in top_n_list('fr', 50000):
        w2 = ''.join(c for c in w.lower() if c.isalpha())
        w2 = w2.replace('œ', 'oe').translate(str.maketrans('éèêëàâäîïôöùûüç', 'eeeeaaaiioouuuc'))
        w2 = w2.replace('j', 'i').replace('v', 'u')   # 当時の表には j・v がない
        if not w2: continue
        f = word_frequency(w, 'fr')
        s = '^' + w2 + '$'
        for i in range(len(s) - 2):
            tri[s[i:i+3]] += f; bi[s[i:i+2]] += f
    alpha = 'abcdefghilmnopqrstuxyz^$'
    def lp(a, b, c):
        return math.log((tri[a+b+c] + 1e-7) / (bi[a+b] + 1e-7 * len(alpha)))
    return lp

def runs(lines, key):
    # 1文字の記号が続く範囲を取り出す（| と単語記号で区切る）
    out = []
    for _, toks in lines:
        cur = []
        for t in toks:
            k = norm(t)
            v = key.get(k)
            if v == '(null)':        # 冠詞形の無効字は読み飛ばす（区切りにしない）
                continue
            if t == '|' or v is None or len(v) != 1:
                if cur: out.append(cur); cur = []
                continue
            cur.append(k)
        if cur: out.append(cur)
    return out

def score(rs, key, lp):
    tot = n = 0
    for r in rs:
        s = '^' + ''.join(key[k] for k in r) + '$'
        for i in range(len(s) - 2):
            tot += lp(s[i], s[i+1], s[i+2]); n += 1
    return tot / n

if __name__ == '__main__':
    key, src = load_key(sys.argv[1], '--table-only' in sys.argv)
    lines = load_lines(sys.argv[2])
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    N = int(args[2]) if len(args) > 2 else 1000
    lp = build_model()
    rs = runs(lines, key)
    letters = [k for k in key if len(key[k]) == 1]
    real = score(rs, key, lp)
    random.seed(1)
    sh = []
    for _ in range(N):
        vals = [key[k] for k in letters]; random.shuffle(vals)
        k2 = dict(key); k2.update(zip(letters, vals))
        sh.append(score(rs, k2, lp))
    sh.sort()
    print(f'採点した文字数（記号）: {sum(len(r) for r in rs)}、文字の記号の種類: {len(letters)}')
    print(f'本物の鍵: {real:.3f}')
    print(f'かき混ぜた鍵 {N} 回: 最小 {sh[0]:.3f} / 中央 {sh[N//2]:.3f} / 最大 {sh[-1]:.3f}')
    print(f'本物以上になった回数: {sum(1 for x in sh if x >= real)} / {N}')
