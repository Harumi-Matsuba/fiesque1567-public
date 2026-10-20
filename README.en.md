# Reading the cipher letters of Scipion de Fiesque (Vienna, 1567–69)

[日本語 README](README.md)

| | |
|---|---|
| Status | **44 pages with cipher in the volume (822 lines, 29,707 signs) transcribed and read. Full reading on all 44 pages.** Figures and status per page in [docs/PAGES.en.md](docs/PAGES.en.md). On every page the decipherment contains many conjectural readings with word division and supplied spelling |
| Prior work | In the places checked on 2026-10-19/20 ([SOURCES.en.md](SOURCES.en.md)) no earlier reading of the ciphered passages of this volume was found. Satoshi Tomokiyo reconstructed and published the key, writing "The reconstructed key below will allow reading undeciphered portions". Nor was any found by someone not involved in the reading who searched again aiming to find earlier work ([docs/PRIOR_CHECK.en.md](docs/PRIOR_CHECK.en.md); the searches were by the volume (fr. 15919) and by name, so they cover every page of the volume). However, the volume itself contains one contemporary decipherment: view 23 right is a plain-text copy, headed "deschiffré", of the cipher letter on view 22 right. Some places remain unchecked, so this is not a claim of being first |
| Human checking | **No human has checked the transcription.** The first transcription is by Claude, the independent second transcription by OpenAI Codex (Claude Sonnet for reference), and the image check of disagreements by Codex and Claude Sonnet. Agreement between AIs is no substitute for human checking |
| Figures | Control: in 1000 shuffled keys none scored as high as the true key, on every page / Calibration: none (the contemporary decipherment on view 23 right could not be used, because AI reading of the cursive is unreliable; [docs/OPEN.en.md](docs/OPEN.en.md)) / Value agreement with the independent second transcription (Codex, without seeing the first), lower of the runs used: 85.0–93.6%. See [docs/METHOD.en.md](docs/METHOD.en.md) |
| Use of AI | Transcription, inferred values, decipherment, scripts and documents by Claude (Claude Opus 5.5); second transcription and image checks by OpenAI Codex and Claude Sonnet. A human chose the target, permitted the image download and decides on publication ([docs/METHOD.en.md](docs/METHOD.en.md) §9) |

BnF fr. 15919 holds the letters of Scipion de Fiesque (Scipione Fiesco), sent from the court of Emperor Maximilian II in Vienna to King Charles IX and the Queen Mother Catherine de Médicis (October 1567 – November 1569), during the negotiation of the King's marriage with Elisabeth of Austria. This repository records a reading of the ciphered passages with Satoshi Tomokiyo's reconstructed key. The first version (2026-10-20) covered only the five letters (six pages) named by Tomokiyo; this version covers all pages with cipher found in the volume.

## Letters and contents (summary, conjectural)
Summaries per page are in [docs/PAGES.en.md](docs/PAGES.en.md). Main topics:
- Autumn 1567 – spring 1568: the ambassador to Constantinople, the mission of Lignerolles, rumours of levies in Germany for the Protestants, the diet of Fulda and the mediation with the Prince of Condé, Duke Johann Wilhelm of Saxony and the Flacian preachers.
- Summer 1568: the detention and death of the Spanish prince (Don Carlos), Archduke Charles's journey to Spain, the King's marriage negotiation, Flanders.
- Autumn 1568 – spring 1569: help for Condé and Orange, the Duke of Aumale, levies of reiters, the Cardinal of Guise in Spain, a match with the King of Portugal.
- Autumn 1569: the marriage decision after the death of Queen Elisabeth de Valois, the siege of Poitiers, a league of Protestant princes, mediation after the victory (taken to be Moncontour).

Not checked against historical sources. Line-by-line readings of the first five letters are in [docs/READING.en.md](docs/READING.en.md), the decipherments of the other pages in data/decoded_*.txt, open points in [docs/OPEN.en.md](docs/OPEN.en.md).

## What was taken from earlier work, and what is added here
**Taken as given**
- The key: Satoshi Tomokiyo's reconstructed table ([Cryptiana](https://cryptiana.web.fc2.com/code/frencheastern.htm)). The table image is not included.
- His observation that letters in this volume are partly in cipher with undeciphered portions.

**Added here**
1. A sign-by-sign transcription of the ciphered passages of 44 pages (822 lines, 29,707 signs) (`data/transcription_*.txt`).
2. Values for signs not in the table and for nulls, inferred from the context of these letters (`inferred` in `data/key.tsv`; e.g. numeral 16 = ce, ꝭs = t, ρ = e, ꝑꝑ = ff; plain letter groups par, moy, bro … are nulls).
3. A reading and a summary of the contents.

## Usage
```
python3 src/decode.py data/key.tsv data/transcription_f094.txt               # with inferred values
python3 src/decode.py data/key.tsv data/transcription_f094.txt --table-only  # table signs only
python3 src/control.py data/key.tsv data/transcription_f094.txt 1000         # control (needs wordfreq)
cd src && python3 ind_compare4.py ind15                                      # comparison with an independent second transcription (per page)
python3 -m unittest discover -s tests
```
Line cropping (src/trackline.py and others) and the crops for the image check (src/mkcheck.py) need the images, which are not included.

## Files
| Path | Contents |
|---|---|
| data/key.tsv | key (sign name, value, source table/inferred, shape note) |
| data/transcription_*.txt | first transcription, with a record of corrections in the notes. Names f… are folios, v… are Gallica views and left/right |
| data/decoded_*.txt | output of src/decode.py |
| data/figures.tsv | figures per page (lines, signs, signs with a value, control) |
| docs/PAGES.en.md | figures, status and summary per page |
| docs/READING.en.md | line-by-line reading of the first five letters (marked dir./inf.) |
| docs/METHOD.en.md | method, figures, use of AI, limits |
| docs/OPEN.en.md | open points |
| docs/PRIOR_CHECK.en.md | adversarial prior-work check |
| second/run0/ | cross-check used for corrections in the first version (three Codex runs; not independent) |
| second/ind/, second/ind2/ … | independent second transcriptions (Codex and Sonnet output, prompts, comparisons). second/sind*/ are Sonnet runs |
| second/check/ | image checks of disagreements (questions, Codex and Sonnet answers, decision lists). The crop images are not included |
| src/, tests/ | scripts and tests |

## Change log
- 2026-10-20: first version (five letters, six pages).
- 2026-10-20 (update the same day): extended to all pages with cipher in the volume. Disagreements were checked on the image by Codex and Claude Sonnet, and only places where the readers agreed were corrected (earlier corrections not supported on re-checking were reverted). Added inferred values (ρ = e, ꝑꝑ = ff).

## Licence
Code MIT; documents and data CC BY 4.0 ([LICENSE](LICENSE)). The rights in the `table` values of the key belong to Satoshi Tomokiyo.
