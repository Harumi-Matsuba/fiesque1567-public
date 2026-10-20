# Sources and prior work

[日本語](SOURCES.md)

Images, PDFs and the image of the key table are not redistributed here. Sources are cited by shelfmark and view number.

## Primary source
| Item | Reference |
|---|---|
| Manuscript | BnF Français 15919 (formerly Harlay 238 (8)). Catalogue https://archivesetmanuscrits.bnf.fr/ark:/12148/cc46124x |
| Images | Gallica ark:/12148/btv1b90573568 (183 views). f. 39r = view 43 right, f. 39v = view 44 left, f. 79r = view 83 right, f. 94r = view 99 right, f. 100r = view 105 right, f. 158r = view 163 right. For the other pages the transcription name gives the view and side (e.g. v007l = view 7 left, v150r = view 150 right). Fetched from https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b90573568/f{view}/full/max/0/default.jpg (2026-10-20) |
| Edition (replies) | H. de La Ferrière (ed.), *Lettres de Catherine de Médicis*, vol. 3 (Internet Archive lettresdecatheri03cathuoft). Prints Catherine's minutes to Fiesque, fr. 15919 f. 118 (21 Oct 1568) and f. 122 (16 Nov 1568). The text of f. 118 was used for the positive control |

## Key
- Satoshi Tomokiyo, "French Ciphers for German (and Eastern) Affairs", Cryptiana, https://cryptiana.web.fc2.com/code/frencheastern.htm (version of 2026-03-15, consulted 2026-10-20); table image easternScipion.png. The `table` values in data/key.tsv are this table rewritten with sign names.

## Prior-work check (by the reader, 2026-10-19/20)
| Where | Version / date | Result |
|---|---|---|
| Cyphersolver (D. Bourdeau) | origin/main 0258b8a (2026-10-18); 46 issues and PRs; public pages (2026-10-19); 10 forks | no reading of fr. 15919 / Fiesque |
| Cryptoole | idx.json (854 entries, 2026-10-17) | nothing |
| Cryptiana | unsolved.htm (2026-10-13), ai.htm (2026-10-19), GL.htm (Lasry's solutions list, 2026-10-15), blog feed (150 posts) | only the publication of the key (2026-03-15); no report of a reading |
| NoAutopilot/cipher-lab | 969df2c (2026-10-19) | no work on fr. 15919 (only an index entry for frencheastern.htm) |
| BravoBravoIX (B. Burford); other repositories of GeorgeLasry and WAINUTAI | 2026-10-20 | nothing |
| GitHub search (repositories, issues, code) | 2026-10-20 | nothing |
| Web search (English, French) | 2026-10-20 | nothing |

- Dates are the pages' Last-Modified.
- Afterwards, someone not involved in the reading searched again, aiming to find earlier work, in the same places and in DECODE, OpenAlex, Persée, the BnF catalogue and others (2026-10-20, [docs/PRIOR_CHECK.en.md](docs/PRIOR_CHECK.en.md)). No earlier reading was found there either. Some places remain unchecked (JSTOR, the Gallica literature search, the text of Patrouch, BnF fr. 17020 ff. 227–228, Lasry's publication list), so this is not a claim of being first.

## Tools
- wordfreq (French word frequencies; model for the control)
- OpenAI Codex CLI 0.163.0-alpha.10.2 (second transcription)
