# 状態の判定に使う独立の2回目（その書き起こしを直す材料に使っていない回だけ）。(フォルダ, 記録の名前の型, 表示名)
J = {}
def add(pages, *runs):
    for p in pages: J[p] = list(runs)
add(['f039r'], ('ind17', '{L}.jsonl', 'Codex'), ('ind18', '{L}.jsonl', 'Codex'))
add(['f039v'], ('ind2', '{L}_run1.jsonl', 'Codex'), ('ind2', '{L}_run2.jsonl', 'Codex'))
add(['f079'], ('ind2', '{L}_run1.jsonl', 'Codex'))
add(['f094', 'f100', 'f158'], ('ind', '{L}.jsonl', 'Codex'))
add(['f079v', 'f080', 'f094v', 'f095', 'f100v', 'f101', 'f101v', 'v008l', 'v035l', 'v038l', 'v038r', 'v049r', 'v070r', 'v103r'], ('ind3', '{L}.jsonl', 'Codex'))
add(['v034r', 'v109r', 'v110l', 'v110r'], ('ind4', '{L}.jsonl', 'Codex'))
add(['v125r', 'v129r', 'v130l', 'v140r', 'v141l', 'v146r'], ('ind6', '{L}.jsonl', 'Codex'))
add(['v149r'], ('ind12', '{L}.jsonl', 'Codex'), ('ind13', '{L}.jsonl', 'Codex'))
add(['v150l', 'v150r'], ('ind7', '{L}.jsonl', 'Codex'))
add(['v155r', 'v159r', 'v161r'], ('ind9', '{L}.jsonl', 'Codex'))
add(['v008r', 'v037r'], ('ind19', '{L}.jsonl', 'Codex'))
add(['v168r'], ('ind20', '{L}.jsonl', 'Codex'))
add(['v007l', 'v007r', 'v022r', 'v065r', 'v071l'], ('ind15', '{L}.jsonl', 'Codex'))
# 参考（判定に使わない）：Sonnet の独立の2回目（sind5）
REF = {p: [('sind5', '{L}.jsonl', 'Sonnet')] for p in ['f039r', 'f079', 'v149r', 'v168r', 'v007l', 'v007r', 'v008r', 'v022r', 'v037r', 'v065r', 'v071l']}
