#!/bin/zsh
# 利用上限が解けた後に、残りの独立の2回目を走らせる（f039r run2、f039v・f079 の run1・run2）
C=/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex
D=$(cd "$(dirname "$0")" && pwd)
run() { local name=$1 pre=$2 a=$3 b=$4 k=$5
  local args=(); for i in $(seq -w $a $b); do args+=(-i "$D/img/${pre}_L$i.jpg"); done
  (cd $D/empty3 && $C exec --ephemeral --skip-git-repo-check -s read-only --json "${args[@]}" -- < $D/PROMPT3.md > $D/ind2/${name}_run$k.jsonl 2> $D/ind2/${name}_run$k.err)
  echo "exit $? $name run$k ${#args}"; }
run f039v b 01 19 1
run f079 e 05 28 1
run f039r a 01 28 2
run f039v b 01 19 2
run f079 e 05 28 2
zsh $D/../calib/run_calib.sh
