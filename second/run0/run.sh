#!/bin/zsh
# 2回目の書き起こし：Codex CLI を空のフォルダから、ページ（a・b・c）ごと・回ごとに別々に走らせる
# 使い方: zsh run.sh <回の番号> <ページ a|b|c>
C=/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex
D=$(cd "$(dirname "$0")" && pwd)
pass=$1; pg=$2
imgs=()
for f in $D/img/${pg}_L*.jpg; do imgs+=(-i "$f"); done
cd $D/empty
$C exec --ephemeral --skip-git-repo-check -s read-only --json "${imgs[@]}" -- "$(cat $D/PROMPT.md)" < /dev/null > $D/out/pass${pass}_${pg}.jsonl 2> $D/out/pass${pass}_${pg}.err
echo "exit $? pass$pass $pg"
