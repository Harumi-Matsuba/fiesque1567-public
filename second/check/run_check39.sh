#!/bin/zsh
# 食い違いの箇所の画像の確かめ（Codex、35問ずつ新しい文脈で1回）。画像は配列で1枚ずつ -i、プロンプトは標準入力。
C=/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex
D=$(cd "$(dirname "$0")" && pwd)
for name in $(python3 -c "import json;print(' '.join(json.load(open('$D/chunks39.json'))))"); do
  ids=( $(python3 -c "import json;print(' '.join(json.load(open('$D/${name}_ids.json'))))") )
  args=(); for id in $ids; do args+=(-i "$D/crops39/$id.jpg"); done
  (cd $D/empty && $C exec --ephemeral --skip-git-repo-check -s read-only --json "${args[@]}" -- < $D/${name}_prompt.md > $D/codex_${name}.jsonl 2> $D/codex_${name}.err)
  echo "exit $? $name ${#ids}"
done
