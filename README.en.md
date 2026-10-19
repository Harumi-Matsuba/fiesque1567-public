# Reading the cipher letters of Scipion de Fiesque (Vienna, 1568–69)

[日本語 README](README.md)

| | |
|---|---|
| Status | **ff. 94r, 100r, 158r: full reading (agreement with the independent second transcription 87.5–91.9%, over 99% of signs with a value). ff. 39r, 39v, 79r: partial reading (agreement 76.1–82.4%).** In every letter most lines are conjectural readings with word division and supplied spelling ("inf." in [docs/READING.en.md](docs/READING.en.md)) |
| Prior work | In the places checked on 2026-10-19/20 ([SOURCES.en.md](SOURCES.en.md)) no earlier reading of these five letters was found. Satoshi Tomokiyo reconstructed and published the key, writing "The reconstructed key below will allow reading undeciphered portions". Nor was any found by someone not involved in the reading who searched again aiming to find earlier work ([docs/PRIOR_CHECK.en.md](docs/PRIOR_CHECK.en.md)). Some places remain unchecked, so this is not a claim of being first |
| Human checking | **No human has checked the transcription.** Both transcriptions are by AI (first Claude, second Codex). Agreement between AIs is no substitute for human checking |
| Figures | Control: in 1000 shuffled keys none scored as high as the true key, on all six pages / Calibration: none (no contemporary decipherment or plain text) / Value agreement with the independent second transcription (Codex, without seeing the first): f. 39r 76.1%, f. 39v 82.4%, f. 79r 81.5%, f. 94r 91.9%, f. 100r 87.5%, f. 158r 90.5%. See [docs/METHOD.en.md](docs/METHOD.en.md) |
| Use of AI | Transcription, inferred values, decipherment, scripts and documents by Claude (Claude Opus 5.5); second transcription by OpenAI Codex. A human chose the target, permitted the image download and decides on publication ([docs/METHOD.en.md](docs/METHOD.en.md) §9) |

BnF fr. 15919 holds the letters of Scipion de Fiesque (Scipione Fiesco), sent from the court of Emperor Maximilian II in Vienna to King Charles IX and the Queen Mother Catherine de Médicis, during the negotiation of the King's marriage with Elisabeth of Austria. This repository records a reading of the ciphered passages of five of these letters with Satoshi Tomokiyo's reconstructed key.

## Letters and contents (summary, conjectural)
| Letter | Date, addressee | Status | Contents |
|---|---|---|---|
| f. 39r–v | 6 March 1568, to the Queen Mother | partial | Duke Johann Wilhelm of Saxony, campaigning for the French king, brought six Flacian preachers; his brother Johann Friedrich is a prisoner; the Emperor means to work for an end of the French civil war |
| f. 79r | 17 July 1568, to the Queen Mother | partial | Talk at court of sending Archduke Charles to Spain for the "délivrance" of the Spanish prince (Don Carlos) |
| f. 94r | 14 August 1568, to the Queen Mother | full | The Emperor himself explains why he sends Archduke Charles to Spain: the prince's affair and Flanders |
| f. 100r | 4 September 1568, to the King | full | The marriage negotiation; a passage reads "le prince d'Espaigne estoit mort", and the Emperor says there is no obstacle any more |
| f. 158r | 29 October 1569, to the King | full | After the King's victory (taken to be Moncontour), the Emperor offers to mediate peace and recommends clemency |

Not checked against historical sources. The full reading is in [docs/READING.en.md](docs/READING.en.md); open points in [docs/OPEN.en.md](docs/OPEN.en.md).

## What was taken from earlier work, and what is added here
**Taken as given**
- The key: Satoshi Tomokiyo's reconstructed table ([Cryptiana](https://cryptiana.web.fc2.com/code/frencheastern.htm)). The table image is not included.
- His observation that letters in this volume are partly in cipher with undeciphered portions.

**Added here**
1. A sign-by-sign transcription of the ciphered passages of five letters (6 pages, 146 lines, 5,422 signs) (`data/transcription_*.txt`).
2. Values for signs not in the table and for nulls, inferred from the context of these letters (`inferred` in `data/key.tsv`; e.g. numeral 16 = ce, ꝭs = t, ß = r; plain letter groups par, moy, bro … are nulls).
3. A reading and a summary of the contents.

## Usage
```
python3 src/decode.py data/key.tsv data/transcription_f094.txt               # with inferred values
python3 src/decode.py data/key.tsv data/transcription_f094.txt --table-only  # table signs only
python3 src/control.py data/key.tsv data/transcription_f094.txt 1000         # control (needs wordfreq)
python3 src/ind_compare.py > second/ind/compare_run1.tsv                     # comparison with the independent second transcription
python3 -m unittest discover -s tests
```
src/trackline.py, lineimgs.py, strips.py (line cropping) and src/posctl.py (positive control) need the images and the OCR of the edition, which are not included.

## Files
| Path | Contents |
|---|---|
| data/key.tsv | key (sign name, value, source table/inferred, shape note) |
| data/transcription_*.txt | first transcription, with a record of corrections in the notes |
| data/decoded_*.txt | output of src/decode.py |
| docs/READING.en.md | figures and reading per letter (marked dir./inf.) |
| docs/METHOD.en.md | method, figures, use of AI, limits |
| docs/OPEN.en.md | open points |
| docs/PRIOR_CHECK.en.md | adversarial prior-work check |
| second/run0/ | cross-check used for corrections (three Codex runs; not independent) |
| second/ind/ | independent second transcription (Codex output, prompt, comparison) |
| src/, tests/ | scripts and tests |

## Change log
- 2026-10-20: first version.

## Licence
Code MIT; documents and data CC BY 4.0 ([LICENSE](LICENSE)). The rights in the `table` values of the key belong to Satoshi Tomokiyo.
