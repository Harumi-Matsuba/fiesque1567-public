#!/bin/zsh
# 独立の2回目（2026-10-20、修正後）：Codex CLI を空のフォルダから、書簡ごとに新しい文脈で走らせる。
# 使い方: zsh run2.sh <名前> <行画像の id …>（例 f079 e_L05 e_L06 …）
C=/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex
D=$(cd "$(dirname "$0")" && pwd)
name=$1; shift
imgs=()
for id in "$@"; do imgs+=(-i "$D/img/$id.jpg"); done
cd $D/empty2
$C exec --ephemeral --skip-git-repo-check -s read-only --json "${imgs[@]}" -- "$(cat $D/PROMPT2.md)" < /dev/null > $D/ind/$name.jsonl 2> $D/ind/$name.err
echo "exit $? $name"
