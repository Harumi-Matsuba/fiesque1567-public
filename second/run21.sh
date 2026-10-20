#!/bin/zsh
# v168r の独立の2回目（このページの字形に合わせて a・三角・Þ の説明を直した PROMPT3_v168r.md、新しい文脈で1回）。
C=/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex
D=$(cd "$(dirname "$0")" && pwd)
for name in $(python3 -c "import json;print(' '.join(json.load(open('$D/ind21/map.json'))))"); do
  [ -s $D/ind21/$name.jsonl ] && grep -q agent_message $D/ind21/$name.jsonl && continue
  ids=( $(python3 -c "import json;print(' '.join(json.load(open('$D/ind21/map.json'))['$name']))") )
  args=(); for id in $ids; do args+=(-i "$D/img/$id.jpg"); done
  (cd $D/empty23 && $C exec --ephemeral --skip-git-repo-check -s read-only --json "${args[@]}" -- < $D/PROMPT3_v168r.md > $D/ind21/$name.jsonl 2> $D/ind21/$name.err)
  echo "exit $? $name ${#ids}"
done
