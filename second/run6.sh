#!/bin/zsh
# f.39r を画像で確かめて直した後の、新しい文脈での独立の2回目（PROMPT3、2回）。出力は ind2/f039r_run3・run4。
C=/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex
D=$(cd "$(dirname "$0")" && pwd)
for k in 3 4; do
  args=(); for i in $(seq -w 01 28); do args+=(-i "$D/img/a_L$i.jpg"); done
  (cd $D/empty6 && $C exec --ephemeral --skip-git-repo-check -s read-only --json "${args[@]}" -- < $D/PROMPT3.md > $D/ind2/f039r_run$k.jsonl 2> $D/ind2/f039r_run$k.err)
  echo "exit $? f039r run$k ${#args}"
done
