#!/bin/zsh
# 食い違いの箇所の画像の確かめ（Codex、書簡ごとに新しい文脈で1回）。画像は配列で1枚ずつ -i、プロンプトは標準入力。
C=/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex
D=$(cd "$(dirname "$0")/.." && pwd)
L=$1
ids=( $(python3 -c "import json;print(' '.join(json.load(open('$D/check/${L}_lines.json'))))") )
args=(); for id in $ids; do args+=(-i "$D/img/$id.jpg"); done
cd $D/check/empty
$C exec --ephemeral --skip-git-repo-check -s read-only --json "${args[@]}" -- < $D/check/${L}_prompt.md > $D/check/codex_${L}.jsonl 2> $D/check/codex_${L}.err
echo "exit $? $L ${#args}"
