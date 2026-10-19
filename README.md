# Scipion de Fiesque の暗号書簡（ウィーン、1568〜69年）の読み

[English README](README.en.md)

| | |
|---|---|
| 状態 | **f.94r・f.100r・f.158r：全文の読み（独立の2回目との一致 87.5〜91.9%、値の付いた割合 99% 以上）。f.39r・f.39v・f.79r：部分的な読み（独立の2回目との一致 76.1〜82.4%）。** どの書簡も、行の大半は語の切れ目や綴りを補った推定の読み（[docs/READING.md](docs/READING.md) の【推】） |
| 先行との関係 | 2026-10-19〜20 に調べた先（[SOURCES.md](SOURCES.md)）では、この5通の先行の読みが見当たらない。友清理士氏は鍵を復元して公開し、「The reconstructed key below will allow reading undeciphered portions」と書いている。読みにかかわっていない調べ手が否定するつもりで調べ直した先でも見当たらない（[docs/PRIOR_CHECK.md](docs/PRIOR_CHECK.md)）。調べていない先が残るので、「初めて」とは言わない |
| 人の確認 | **人は書き起こしを確かめていない。** 書き起こしは2回とも AI（1回目 Claude、2回目 Codex）による。AI どうしの一致は、人の確認の代わりにならない |
| 数字 | 対照：鍵をかき混ぜた1000回で本物以上は6ページとも0回／較正：なし（当時の解読も平文もないため）／独立の2回目（Codex、1回目を見せずに）との値の一致：f.39r 76.1%、f.39v 82.4%、f.79r 81.5%、f.94r 91.9%、f.100r 87.5%、f.158r 90.5%。詳しくは [docs/METHOD.md](docs/METHOD.md) |
| AI の使用 | 書き起こし・鍵の補い・解読・スクリプト・文書は Claude（Claude Opus 5.5）、2回目の書き起こしは OpenAI Codex。人は対象の選定・画像の取得の許可・公開の判断（[docs/METHOD.md](docs/METHOD.md) §9） |

フランス国立図書館 BnF fr. 15919 には、Scipion de Fiesque（Scipione Fiesco）が皇帝マクシミリアン2世の宮廷（ウィーン）から、国王シャルル9世と王妃カトリーヌ・ド・メディシスに送った書簡が綴じられています。国王とエリザベート・ドートリッシュの結婚の交渉のための使節でした。このリポジトリは、そのうち暗号を含む5通の暗号部分を、友清理士氏の復元表で読んだ記録です。

## 書簡と内容（要約、推定）
| 書簡 | 日付・宛先 | 状態 | 内容 |
|---|---|---|---|
| f.39r–v | 1568年3月6日、王妃宛 | 部分的 | ザクセン公ヨハン・ヴィルヘルム（Jehan Guillaume）がフランス王のための出兵に、フラキウス派の説教師6人を連れて行ったこと。兄ヨハン・フリードリヒの幽閉。皇帝が内戦の終結に尽力するつもりであること |
| f.79r | 1568年7月17日、王妃宛 | 部分的 | スペイン王子（ドン・カルロス）の解放のため、カール大公をスペインへ送る話が宮廷で出ていること |
| f.94r | 1568年8月14日、王妃宛 | 全文 | 皇帝本人が、カール大公をスペインへ送る理由を語った：王子の件とフランドルの件 |
| f.100r | 1568年9月4日、国王宛 | 全文 | 結婚の交渉。「le prince d'Espaigne estoit mort」と読める箇所があり、障害がなくなったと皇帝が語る |
| f.158r | 1569年10月29日、国王宛 | 全文 | 国王の戦勝（モンコントゥールと推定）の後、皇帝が和平の仲介を申し出て、臣下への寛大さを勧める |

史実との照合はしていません。読みの全文は [docs/READING.md](docs/READING.md)、未解決の点は [docs/OPEN.md](docs/OPEN.md)。

## 先行研究の成果と、この読みで加えたこと
**前提にしたもの**
- 鍵：友清理士氏の復元表（[Cryptiana](https://cryptiana.web.fc2.com/code/frencheastern.htm)）。表の画像はこのリポジトリに含めていない。
- この巻の書簡が部分的に暗号で、読まれていない部分があるという指摘（同氏）。

**この読みで加えたこと**
1. 5通の暗号部分（6ページ、146行、5,422記号）を、記号名で行ごとに書き起こした（`data/transcription_*.txt`）。
2. 表にない記号と無効字の値を、この書簡群の文脈から補った（`data/key.tsv` の inferred。例：数字16＝ce、ꝭs＝t、ß＝r、平文の字の組 par・moy・bro などは無効字）。
3. 解読文と内容の要約。

## 使い方
```
python3 src/decode.py data/key.tsv data/transcription_f094.txt               # 推定も使う
python3 src/decode.py data/key.tsv data/transcription_f094.txt --table-only  # 表の記号だけ
python3 src/control.py data/key.tsv data/transcription_f094.txt 1000         # 対照実験（wordfreq が必要）
python3 src/ind_compare.py > second/ind/compare_run1.tsv                     # 独立の2回目との比較
python3 -m unittest discover -s tests
```
src/trackline.py・lineimgs.py・strips.py（行の切り出し）と src/posctl.py（陽性対照）は、このリポジトリに含めていない画像と刊本の OCR を入力にする。

## ファイル
| 場所 | 中身 |
|---|---|
| data/key.tsv | 鍵（記号名・値・出典 table／inferred・形の説明） |
| data/transcription_*.txt | 書き起こし（1回目）。注記に修正の記録 |
| data/decoded_*.txt | src/decode.py の出力 |
| docs/READING.md | 書簡ごとの数字と解読文（確・推の印つき） |
| docs/METHOD.md | 方法・数字・AI の使用・限界 |
| docs/OPEN.md | 未解決の点 |
| docs/PRIOR_CHECK.md | 先行の確かめ（否定するつもりの調査） |
| second/run0/ | 照合と修正の記録（1回目を直すのに使った Codex の3回分。独立ではない） |
| second/ind/ | 独立の2回目（Codex の出力、プロンプト、比較の結果） |
| src/・tests/ | スクリプトとテスト |

## 更新履歴
- 2026-10-20：初めての版。

## ライセンス
コードは MIT、文書とデータは CC BY 4.0（[LICENSE](LICENSE)）。鍵の table の値の権利は友清理士氏にある。
