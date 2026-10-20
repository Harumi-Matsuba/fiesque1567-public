# Scipion de Fiesque の暗号書簡（ウィーン、1567〜69年）の読み

[English README](README.en.md)

| | |
|---|---|
| 状態 | **巻の中の暗号のページ 44 ページ（822 行、29,707 記号）を書き起こして読んだ。全文の読み 43 ページ、部分的な読み 1 ページ。** ページごとの数字と状態は [docs/PAGES.md](docs/PAGES.md)。どのページも、解読文には語の切れ目や綴りを補った推定の読みが多い |
| 先行との関係 | 2026-10-19〜20 に調べた先（[SOURCES.md](SOURCES.md)）では、この巻の暗号部分の先行の読みが見当たらない。友清理士氏は鍵を復元して公開し、「The reconstructed key below will allow reading undeciphered portions」と書いている。読みにかかわっていない調べ手が否定するつもりで調べ直した先でも見当たらない（[docs/PRIOR_CHECK.md](docs/PRIOR_CHECK.md)。検索は巻（fr.15919）と人名で行ったので、巻のどのページにも当てはまる）。ただし、巻の中に当時の解読文が1つある（コマ23右は、コマ22右の暗号書簡を「deschiffré」と題して平文で写したもの）。調べていない先が残るので、「初めて」とは言わない |
| 人の確認 | **人は書き起こしを確かめていない。** 書き起こしは1回目が Claude、独立の2回目が OpenAI Codex（参考に Claude Sonnet）、食い違いの画像の確かめは Codex と Claude Sonnet。AI どうしの一致は、人の確認の代わりにならない |
| 数字 | 対照：鍵をかき混ぜた1000回で本物以上は全ページ0回／較正：なし（コマ23右の当時の解読文は、AI による草書の読み取りが不確かで使えていない、[docs/OPEN.md](docs/OPEN.md)）／独立の2回目（Codex、1回目を見せずに）との値の一致：判定に使う回の低い方で 80.3〜93.6%（全文の読みの 43 ページは 85.0〜93.6%、部分的な読みはコマ168右の 80.3%）。詳しくは [docs/METHOD.md](docs/METHOD.md) |
| AI の使用 | 書き起こし・鍵の補い・解読・スクリプト・文書は Claude（Claude Opus 5.5）、2回目の書き起こしと画像の確かめは OpenAI Codex と Claude Sonnet。人は対象の選定・画像の取得の許可・公開の判断（[docs/METHOD.md](docs/METHOD.md) §9） |

フランス国立図書館 BnF fr. 15919 には、Scipion de Fiesque（Scipione Fiesco）が皇帝マクシミリアン2世の宮廷（ウィーン）から、国王シャルル9世と王妃カトリーヌ・ド・メディシスに送った書簡（1567年10月〜1569年11月）が綴じられています。国王とエリザベート・ドートリッシュの結婚の交渉のための使節でした。このリポジトリは、書簡の暗号部分を、友清理士氏の復元表で読んだ記録です。初版（2026-10-20）では友清氏が挙げた5通（6ページ）だけでしたが、この版で巻の中の暗号のページ全部（洗い出した範囲）に広げました。

## 書簡と内容（要約、推定）
ページごとの要約は [docs/PAGES.md](docs/PAGES.md)。主な話題：
- 1567年秋〜1568年春：コンスタンティノープルへの大使、Lignerolles の使節、ドイツでの新教徒のための募兵の噂、Fulda の会議と Condé 公との和解の仲介、ザクセン公 Johann Wilhelm と Flacius 派の説教師。
- 1568年夏：スペインの王子（Don Carlos）の拘束と死、Karl 大公のスペイン行き、国王の結婚の交渉、フランドル。
- 1568年秋〜1569年春：Condé 公・Orange 公への救援、Aumale 公、ドイツ騎兵の募集、Guise 枢機卿のスペイン行き、ポルトガル王との縁組。
- 1569年秋：王妃 Elisabeth de Valois の死の後の結婚の決定、Poitiers の包囲、新教諸侯の同盟、勝利（Moncontour と推定）の後の和平の仲介。

史実との照合はしていません。最初の5通の行ごとの読みは [docs/READING.md](docs/READING.md)、ほかのページの解読文は data/decoded_*.txt、未解決の点は [docs/OPEN.md](docs/OPEN.md)。

## 先行研究の成果と、この読みで加えたこと
**前提にしたもの**
- 鍵：友清理士氏の復元表（[Cryptiana](https://cryptiana.web.fc2.com/code/frencheastern.htm)）。表の画像はこのリポジトリに含めていない。
- この巻の書簡が部分的に暗号で、読まれていない部分があるという指摘（同氏）。

**この読みで加えたこと**
1. 暗号部分 44 ページ（822 行、29,707 記号）を、記号名で行ごとに書き起こした（`data/transcription_*.txt`）。
2. 表にない記号と無効字の値を、この書簡群の文脈から補った（`data/key.tsv` の inferred。例：数字16＝ce、ꝭs＝t、ρ＝e、ꝑꝑ＝ff、平文の字の組 par・moy・bro などは無効字）。
3. 解読文と内容の要約。

## 使い方
```
python3 src/decode.py data/key.tsv data/transcription_f094.txt               # 推定も使う
python3 src/decode.py data/key.tsv data/transcription_f094.txt --table-only  # 表の記号だけ
python3 src/control.py data/key.tsv data/transcription_f094.txt 1000         # 対照実験（wordfreq が必要）
cd src && python3 ind_compare4.py ind15                                      # 独立の2回目との比較（ページ単位）
python3 -m unittest discover -s tests
```
行の切り出し（src/trackline.py ほか）と画像の確かめの切り出し（src/mkcheck.py）は、このリポジトリに含めていない画像を入力にする。

## ファイル
| 場所 | 中身 |
|---|---|
| data/key.tsv | 鍵（記号名・値・出典 table／inferred・形の説明） |
| data/transcription_*.txt | 書き起こし（1回目）。注記に修正の記録。名前の f… は葉番号、v… は Gallica のコマ番号と左右 |
| data/decoded_*.txt | src/decode.py の出力 |
| data/figures.tsv | ページごとの数字（行・記号・値の付いた割合・対照） |
| docs/PAGES.md | ページごとの数字・状態・要約 |
| docs/READING.md | 最初の5通の行ごとの解読文（確・推の印つき） |
| docs/METHOD.md | 方法・数字・AI の使用・限界 |
| docs/OPEN.md | 未解決の点 |
| docs/PRIOR_CHECK.md | 先行の確かめ（否定するつもりの調査） |
| second/run0/ | 照合と修正の記録（初版で1回目を直すのに使った Codex の3回分。独立ではない） |
| second/ind/・second/ind2/〜 | 独立の2回目（Codex と Sonnet の出力、プロンプト、比較の結果）。second/sind*/ は Sonnet の回 |
| second/check/ | 食い違いの画像の確かめ（問い・Codex と Sonnet の答え・決定の一覧）。切り出しの画像は含めていない |
| src/・tests/ | スクリプトとテスト |

## 更新履歴
- 2026-10-20：初めての版（5通、6ページ）。
- 2026-10-20（同日の更新）：巻の中の暗号のページ全部に広げた。食い違いの画像の確かめを、Codex と Claude Sonnet で行い、読み手がそろった箇所だけを直した（前に直した箇所も、取り直しで支えられない所は戻した）。値の推定を足した（ρ＝e、ꝑꝑ＝ff）。

## ライセンス
コードは MIT、文書とデータは CC BY 4.0（[LICENSE](LICENSE)）。鍵の table の値の権利は友清理士氏にある。
