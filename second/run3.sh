#!/bin/zsh
# 修正後の独立の2回目（PROMPT3、書簡ごとに新しい文脈で2回）。画像は配列で1枚ずつ -i、プロンプトは標準入力。
C=/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex
D=$(cd "$(dirname "$0")" && pwd)
run() { local name=$1 pre=$2 a=$3 b=$4 k=$5
  local args=(); for i in $(seq -w $a $b); do args+=(-i "$D/img/${pre}_L$i.jpg"); done
  (cd $D/empty3 && $C exec --ephemeral --skip-git-repo-check -s read-only --json "${args[@]}" -- < $D/PROMPT3.md > $D/ind2/${name}_run$k.jsonl 2> $D/ind2/${name}_run$k.err)
  echo "exit $? $name run$k ${#args}"; }
for k in 1 2; do
  run f039r a 01 28 $k
  run f039v b 01 19 $k
  run f079 e 05 28 $k
done
