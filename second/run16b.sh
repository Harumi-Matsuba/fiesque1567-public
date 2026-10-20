#!/bin/zsh
# 新しく読んだページの独立の2回目（PROMPT3、ページごとに新しい文脈で1回）。行画像はそのページの全部（ind15/map.json）。比べ方はページ単位の並べ合わせ（work/ind_compare4.py）。
C=/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex
D=$(cd "$(dirname "$0")" && pwd)
for name in $(python3 -c "import json;print(' '.join(json.load(open('$D/ind15/map.json'))))"); do
  [ -s $D/ind15/$name.jsonl ] && grep -q agent_message $D/ind15/$name.jsonl && continue
  ids=( $(python3 -c "import json;print(' '.join(json.load(open('$D/ind15/map.json'))['$name']))") )
  args=(); for id in $ids; do args+=(-i "$D/img/$id.jpg"); done
  (cd $D/empty17 && $C exec --ephemeral --skip-git-repo-check -s read-only --json "${args[@]}" -- < $D/PROMPT3.md > $D/ind15/$name.jsonl 2> $D/ind15/$name.err)
  echo "exit $? $name ${#ids}"
done
