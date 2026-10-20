# EN: Tests: the first-version second transcription records (second/ind/) contain one reply and no commands. (Its agreement figures were made with the first-version transcription, kept in git history.)
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestSecond(unittest.TestCase):
    # 初版の比較の結果（second/ind/summary_run1.txt・compare_run1.tsv）は、初版の書き起こし（git の履歴）で出したもの。
    # その後に書き起こしを直したので、今の書き起こしでは同じ数字にならない。今の判定は tests/test_status.py で確かめる。

    def test_runs_have_no_commands(self):
        # 実行記録には返答（agent_message）だけがあり、コマンドの実行やファイルの読み込みがない
        import json, glob
        for p in glob.glob(os.path.join(ROOT, 'second', 'ind', '*.jsonl')):
            types = [json.loads(l)['item']['type'] for l in open(p, encoding='utf-8')
                     if json.loads(l).get('type') == 'item.completed']
            self.assertEqual(types, ['agent_message'], p)


if __name__ == '__main__':
    unittest.main()
