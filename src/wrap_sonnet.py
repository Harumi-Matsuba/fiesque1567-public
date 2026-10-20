# Sonnet の独立の2回目（テキスト：行 id TAB 記号名）を、Codex の記録と同じ形（jsonl の agent_message 1件）に包む。比較スクリプトをそのまま使うため。
# 使い方: python3 wrap_sonnet.py 入力.txt 出力.jsonl
import sys, json
t = open(sys.argv[1], encoding='utf-8').read()
open(sys.argv[2], 'w', encoding='utf-8').write(json.dumps({'type': 'item.completed', 'item': {'type': 'agent_message', 'text': t}}, ensure_ascii=False) + '\n')
