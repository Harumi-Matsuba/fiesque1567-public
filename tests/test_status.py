# EN: Tests: every Codex/Sonnet record has one reply and no commands; the status table matches a recomputation for some pages; no page has a shuffled key at or above the true key.
import csv, glob, json, os, subprocess, sys, unittest
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestStatus(unittest.TestCase):
    def test_records_have_no_commands(self):
        # 独立の2回目と画像の確かめの記録には、返答（agent_message）だけがあり、コマンドの実行やファイルの読み込みがない
        files = glob.glob(os.path.join(ROOT, 'second', 'ind*', '*.jsonl')) + glob.glob(os.path.join(ROOT, 'second', 'check', 'codex_*.jsonl'))
        self.assertGreater(len(files), 50)
        for p in files:
            types = [json.loads(l)['item']['type'] for l in open(p, encoding='utf-8') if json.loads(l).get('type') == 'item.completed']
            self.assertEqual(types, ['agent_message'], p)

    def test_status_recomputed(self):
        # 判定表（data/status.tsv）の値を、src/ind_compare4.py で計算し直して確かめる（f039r の ind17、5ページの ind15）
        st = {r['page']: r for r in csv.DictReader(open(os.path.join(ROOT, 'data', 'status.tsv'), encoding='utf-8'), delimiter='\t')}
        for d, pages in [('ind17', ['f039r']), ('ind15', ['v007l', 'v007r', 'v022r', 'v065r', 'v071l'])]:
            out = subprocess.run([sys.executable, 'ind_compare4.py', d], cwd=os.path.join(ROOT, 'src'), capture_output=True, text=True, check=True).stdout
            got = {l.split('\t')[0]: l.split('\t')[3] for l in out.splitlines()}
            for p in pages:
                self.assertIn(got[p], st[p]['runs'], (d, p))

    def test_controls(self):
        # どのページも、かき混ぜた鍵1000回で本物以上が0回（data/figures.tsv）
        for r in csv.DictReader(open(os.path.join(ROOT, 'data', 'figures.tsv'), encoding='utf-8'), delimiter='\t'):
            self.assertEqual(r['count_all'], '0', r['page'])


if __name__ == '__main__':
    unittest.main()
