# fiesque1567 用の変更：値が (null) の記号は出力しない。
# key.tsv を transcription_*.txt に当てて平文を出す。
# 使い方: python3 decode.py ../key.tsv ../transcription_f218r.txt [--table-only]
#   --table-only : 出典が table の記号だけを使う（inferred は [?] にする）
import sys, re

def load_key(path, table_only=False):
    key, src = {}, {}
    for ln in open(path, encoding='utf-8'):
        if ln.startswith('# ') or not ln.strip():
            continue
        p = ln.rstrip('\n').split('\t')
        key[p[0]], src[p[0]] = p[1], p[2]
    if table_only:
        key = {k: v for k, v in key.items() if src[k] == 'table'}
    return key, src

def load_lines(path):
    out = []
    for ln in open(path, encoding='utf-8'):
        m = re.match(r'(c[\w]+):\s*(.*)', ln)
        if m:
            out.append((m.group(1), m.group(2).split()))
    return out

def norm(tok):
    return tok[:-1] if tok.endswith('?') and len(tok) > 1 else tok

def decode(lines, key):
    res = []
    for lab, toks in lines:
        s = []
        for t in toks:
            if t == '|':
                s.append(' ')
                continue
            v = key.get(norm(t))
            if v == '(null)':
                continue
            if v is None:
                s.append('[?]')
            elif len(v) > 1 or t.startswith('=') or t.startswith('.'):
                s.append(' ' + v.upper() + ' ')
            else:
                s.append(v)
        res.append((lab, re.sub(r'\s+', ' ', ''.join(s)).strip()))
    return res

if __name__ == '__main__':
    key, src = load_key(sys.argv[1], '--table-only' in sys.argv)
    lines = load_lines(sys.argv[2])
    n_all = sum(1 for _, ts in lines for t in ts if t != '|')
    n_ok = sum(1 for _, ts in lines for t in ts if t != '|' and norm(t) in key and key[norm(t)] != '?')
    for lab, s in decode(lines, key):
        print(lab, s)
    label = '表（Tomokiyo）の記号だけで' if '--table-only' in sys.argv else '表と推定を合わせて'
    print(f'# 記号 {n_all} 個のうち、{label}値が付いたもの {n_ok} 個（{n_ok/n_all:.1%}）')
