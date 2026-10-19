# EN: Tests: the agreement figures of the independent second transcription (second/ind/summary_run1.txt) are reproduced by src/ind_compare.py.
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestSecond(unittest.TestCase):
    def test_summary_reproduced(self):
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'src', 'ind_compare.py')],
                           capture_output=True, text=True, check=True)
        with open(os.path.join(ROOT, 'second', 'ind', 'summary_run1.txt'), encoding='utf-8') as f:
            self.assertEqual(r.stderr, f.read())
        with open(os.path.join(ROOT, 'second', 'ind', 'compare_run1.tsv'), encoding='utf-8') as f:
            self.assertEqual(r.stdout, f.read())

    def test_runs_have_no_commands(self):
        # 実行記録には返答（agent_message）だけがあり、コマンドの実行やファイルの読み込みがない
        import json, glob
        for p in glob.glob(os.path.join(ROOT, 'second', 'ind', '*.jsonl')):
            types = [json.loads(l)['item']['type'] for l in open(p, encoding='utf-8')
                     if json.loads(l).get('type') == 'item.completed']
            self.assertEqual(types, ['agent_message'], p)


if __name__ == '__main__':
    unittest.main()
