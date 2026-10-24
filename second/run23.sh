#!/bin/zsh
# v023l（コマ23左、2026-10-25 に書き起こし）の独立の2回目。PROMPT3、新しい文脈で2回（empty25・empty26、出力 ind23/v023l_run1・run2）。
C=/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex
D=$(cd "$(dirname "$0")" && pwd)
ids=( $(python3 -c "import json;print(' '.join(json.load(open('$D/ind23/map.json'))['v023l']))") )
args=(); for id in $ids; do args+=(-i "$D/img/$id.jpg"); done
for r in 1 2; do
  (cd $D/empty2$((4+r)) && $C exec --ephemeral --skip-git-repo-check -s read-only --json "${args[@]}" -- < $D/PROMPT3.md > $D/ind23/v023l_run$r.jsonl 2> $D/ind23/v023l_run$r.err)
  echo "exit $? run$r ${#ids}"
done
