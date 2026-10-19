# 陽性対照：活字本の平文（Lettres de Catherine de Médicis t.3、fr.15919 f.118 のミニュート、Fiesque 宛 1568-10-21）を
# key.tsv で暗号化し、書き起こしの誤り（記号の取り違え）を混ぜた「疑似書き起こし」を作る。
# control.py がこれを本物の鍵で見分けられるか（陽性）、乱数の記号列では見分けないか（陰性）を見る。
# 使い方: python3 posctl.py ../key.tsv ../raw/lettres_cdm_t03.txt 出力.txt [誤り率] [--random]
import sys, random, re, unicodedata
from decode import load_key
key, _ = load_key(sys.argv[1])
raw = open(sys.argv[2], encoding='utf-8').read().split('\n')[23808:23900]
err = float(sys.argv[4]) if len(sys.argv) > 4 and not sys.argv[4].startswith('--') else 0.05
txt = ' '.join(raw).lower()
txt = unicodedata.normalize('NFD', txt); txt = ''.join(c for c in txt if not unicodedata.combining(c))
txt = txt.replace('j', 'i').replace('v', 'u').replace('w', 'u').replace('k', 'c')
words = re.findall(r'[a-z]+', txt)
inv = {}
for k, v in key.items():
    inv.setdefault(v, []).append(k)
words_code = {'et': '=10', 'faire': '=13', 'est': '=14', 'uous': '=18', 'pour': '=20', 'tant': '=21', 'que': '=22'}
nulls = inv['(null)']
syms = [k for k in key if key[k] != '(null)']
random.seed(7)
toks = []
for w in words:
    if w in words_code:
        toks.append(words_code[w]); continue
    i = 0
    while i < len(w):
        dbl = w[i:i+2]
        if len(dbl) == 2 and dbl[0] == dbl[1] and dbl in inv:
            toks.append(random.choice(inv[dbl])); i += 2; continue
        if w[i] in inv:
            toks.append(random.choice(inv[w[i]]))
        i += 1
        if random.random() < 0.03:
            toks.append(random.choice(nulls))
if '--random' in sys.argv:
    toks = [random.choice(syms) for _ in toks]
toks = [random.choice(syms) if random.random() < err else t for t in toks]
with open(sys.argv[3], 'w', encoding='utf-8') as f:
    f.write(f'# 疑似書き起こし（posctl.py、誤り率 {err}、random={"--random" in sys.argv}）\n')
    for j in range(0, len(toks), 30):
        f.write(f'c{j//30+1:02d}: ' + ' '.join(toks[j:j+30]) + '\n')
print(len(toks), 'symbols')
