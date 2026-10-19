# 資料と先行研究

[English](SOURCES.en.md)

画像・PDF・表の画像は、このリポジトリで再配布していない。資料は参照コードとコマ番号で示す。

## 一次資料
| 資料 | 参照 |
|---|---|
| 原本 | BnF Français 15919（旧 Harlay 238 (8)）。目録 https://archivesetmanuscrits.bnf.fr/ark:/12148/cc46124x |
| 画像 | Gallica ark:/12148/btv1b90573568（183コマ）。f.39r＝コマ43の右、f.39v＝コマ44の左、f.79r＝コマ83の右、f.94r＝コマ99の右、f.100r＝コマ105の右、f.158r＝コマ163の右。取得は https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b90573568/f{コマ}/full/max/0/default.jpg （2026-10-20） |
| 刊本（返信） | H. de La Ferrière 編『Lettres de Catherine de Médicis』t.3（Internet Archive lettresdecatheri03cathuoft）。fr.15919 f.118（1568-10-21）・f.122（1568-11-16）の Catherine から Fiesque へのミニュートが載る。陽性対照に f.118 の本文を使った |

## 鍵
- 友清理士（Satoshi Tomokiyo）「French Ciphers for German (and Eastern) Affairs」、Cryptiana、https://cryptiana.web.fc2.com/code/frencheastern.htm （2026-03-15 版、2026-10-20 に参照）。復元表の画像 easternScipion.png。data/key.tsv の table の値は、この表を記号名に置き換えたもの。

## 先行の確かめ（解いた側のセッションによる、2026-10-19〜20）
| 先 | 版・日付 | 結果 |
|---|---|---|
| Cyphersolver（D. Bourdeau） | origin/main 0258b8a（2026-10-18）、issue・PR 46件、公開ページ（2026-10-19）、フォーク10件 | 15919・Fiesque の解読なし |
| Cryptoole | idx.json（854件、2026-10-17） | 該当なし |
| Cryptiana | unsolved.htm（2026-10-19）、ai.htm、GL.htm（Lasry の解読一覧、2026-10-15）、ブログ feed 150件 | 鍵の公開（2026-03-15）だけ。解読の報告なし |
| NoAutopilot/cipher-lab | 969df2c（2026-10-19） | fr.15919 の作業なし（索引に frencheastern.htm があるだけ） |
| BravoBravoIX（B. Burford）、GeorgeLasry・WAINUTAI の他のリポジトリ | 2026-10-20 | 該当なし |
| GitHub の検索（リポジトリ・issue・コード） | 2026-10-20 | 該当なし |
| Web 検索（英・仏） | 2026-10-20 | 該当なし |

- 調べていない先：DECODE の検索画面、pangoleen/cipher-readings、Lasry の論文一覧、BnF fr.17020 f.227–228（この巻の明細）。
- 解いたのとは別のセッションによる、否定するつもりの先行の確かめ（docs/PRIOR_CHECK.md）は、まだしていない。上の範囲で先行の解読が見当たらないというだけで、「初めて」とは言わない。

## 使った道具
- wordfreq（仏語の語の頻度、対照実験の模型）
- OpenAI Codex CLI 0.163.0-alpha.10.2（2回目の書き起こし）
