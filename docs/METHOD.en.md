# Method, figures, use of AI, limits

[日本語](METHOD.md)

## 1. Source and images
- BnF Français 15919 (formerly Harlay 238 (8)), 174 folios: letters of Scipion de Fiesque (Scipione Fiesco) from the court of Emperor Maximilian II (Vienna) to King Charles IX and the Queen Mother Catherine de Médicis, October 1567 – November 1569. Catalogue: https://archivesetmanuscrits.bnf.fr/ark:/12148/cc46124x
- Images: Gallica ark:/12148/btv1b90573568 (digitized from microfilm MF 15717; 183 views of openings). Full-size images (about 7000 px wide) were fetched from BnF's IIIF service (openapi.bnf.fr), 5 seconds apart. Images are not included in this repository.
- Scope: the first version covered the five letters named by Satoshi Tomokiyo as partly in cipher (ff. 39, 79, 94, 100, 158). This version extends to all pages with cipher found in the volume (44 pages) (§11).

## 2. Key
- Satoshi Tomokiyo's reconstructed table (Cryptiana, "French Ciphers for German (and Eastern) Affairs", https://cryptiana.web.fc2.com/code/frencheastern.htm, version of 2026-03-15). He writes: "The reconstructed key below will allow reading undeciphered portions." The table image is not included.
- data/key.tsv: the table's signs, given names, with their values (source `table`). Signs not in the table and nulls were inferred from the context of these letters (source `inferred`); see column 4 of key.tsv and [OPEN.en.md](OPEN.en.md).

## 3. First transcription
- Claude (Claude Code, Claude Opus 5.5) transcribed the signs by name from line images (src/trackline.py and others) into data/transcription_*.txt. Thin separator lines were not written. Plain-text words were written as null names (.par etc.) or left out (see the notes in each file).
- Similar signs (four cross shapes, the y-shape) were meant to be named by shape only. However, s and p in the looped y-shape could not be told apart by shape and are chosen by context ([OPEN.en.md](OPEN.en.md) §1).
- Mechanical decipherment: src/decode.py (data/decoded_*.txt).

## 4. Cross-check used for corrections (second/run0/)
- First, the 74 line images of ff. 39r, 39v and 100r were transcribed three times by Codex without seeing the first transcription, and compared (second/run0/RESULT.md). The sign list used then (PROMPT.md) had confusing descriptions.
- Corrections were made after looking at the disagreements. Only corrections confirmed on the enlarged image were kept:
  - 50 places changed to the Codex majority: 47 confirmed and kept, 3 not confirmed and reverted (table in second/run0/RESULT.md, section on the review of the 50 places).
  - 25 places Codex read as +: 8 corrected to ⊢, 3 to +, 12 kept as t-shape; 1 had been set to 4 from context and was reverted; 1 could not be checked (same file, t-shape and +).
  - 18 places in "qu": 14 corrected to ⊢, 4 kept as t-shape (same file, ⊢ and the y-shape).
  - 4 places in f. 100 written as W were confirmed on the image as ϖ and corrected.
- Because this comparison was used to correct the first transcription, it is not called "independent".

## 5. Independent second transcription (second/ind/, first version)
- After all corrections, the line images of the six pages (146 lines) were transcribed by Codex, once per letter, each in a fresh context. Codex = OpenAI Codex CLI (codex-cli 0.163.0-alpha.10.2 bundled with the ChatGPT app; default model, the model name is not shown in the logs), run as `codex exec --ephemeral --skip-git-repo-check -s read-only --json` from an empty folder, given only the line images and a sign list with shape descriptions (second/ind/PROMPT2.md). No values, key or first transcription were given. The logs contain only one reply each, with no commands run and no files read (checked by tests/test_second.py).
- The first transcription was not corrected after seeing these results.
- Comparison (src/ind_compare.py): signs aligned line by line by edit distance; agreement counted by name and by value (same letter under the key). The first transcription's name tt is the same ŧŧ/# shape and was treated as H#. The looped y-shape (v = s and 3p = p in the first transcription) was treated as one class (value s/p); figures without this class are also given.

| Letter | Signs (first) | Name agreement | Value agreement | Value agreement excluding the y-shape |
|---|---|---|---|---|
| f. 39r | 1,169 | 75.2% | 76.1% | 75.3% |
| f. 39v | 717 | 78.8% | 82.4% | 83.1% |
| f. 79r | 793 | 76.5% | 81.5% | 81.8% |
| f. 94r | 855 | 91.5% | 91.9% | 91.6% |
| f. 100r | 977 | 85.6% | 87.5% | 87.7% |
| f. 158r | 832 | 85.3% | 90.5% | 90.1% |

- The shortfall in ff. 39r and 79r is mainly that Codex left out the thin, faint double strokes "//" (value a) as separators (50 and 37 places). Seven of them were enlarged: all are two strokes of letter height, and reading them as a gives sense. The run was not repeated with a revised prompt, since that would amount to choosing a better run.

## 6. Control
- 1000 keys with the values of the single-letter signs shuffled were compared with the true key for French-likeness (src/control.py: mean log-likelihood of letter trigrams from the top 50,000 French words of wordfreq; nulls skipped), also using table signs only. For every letter, no shuffled key scored as high as the true key (figures in [READING.en.md](READING.en.md)).
- Positive control (src/posctl.py): the text of Catherine's letter to Fiesque (minute, fr. 15919 f. 118, printed by La Ferrière, vol. 3) was enciphered with this key, with substituted signs mixed in. With about 200 signs and 10% errors the true key was still distinguished (0/1000); a random sign sequence was not (619/1000).

## 7. Calibration
- None. The first version said that no contemporary decipherment was found in the volume; that is wrong: view 23 right has a contemporary decipherment (plain-text copy) of the cipher letter on view 22 right. Its cursive could not be read reliably by AI, so it is not used ([OPEN.en.md](OPEN.en.md) §7). La Ferrière's edition prints only Catherine's replies, not the plain text of Fiesque's ciphered passages.

## 8. Criteria for full and partial reading
| Status | Conditions |
|---|---|
| partial reading | no shuffled key ≥ true key in 1000; at least one passage that makes sense; ≥70% agreement with the independent second transcription (with calibration: ≥65% letters) |
| full reading | the partial-reading conditions plus ≥85% agreement with the independent second transcription and ≥95% of signs with a value (with calibration: ≥90% signs or ≥85% letters) |

- In the first version ff. 94r, 100r and 158r were full readings and ff. 39r, 39v and 79r partial. The status in this version is in §14 and [PAGES.en.md](PAGES.en.md) (full reading on all 44 pages).
- Agreement is judged by value; name agreement is also given.

## 9. Use of AI
- First transcription, inferred values, decipherment, scripts and documents: Anthropic's Claude (Claude Code, Claude Opus 5.5).
- Second transcription and image checks: OpenAI Codex (above) and Anthropic Claude Sonnet (§12, §13).
- Done by a human: choice of target, permission to fetch the images, decision to publish. **No human has checked the transcription.** Agreement between AIs is no substitute for human checking.

## 10. Limits
- Most lines of the reading are "inf." and include word division, supplied spelling and the s/p choice for the y-shape.
- Not checked against historical sources.
- Some signs have no value (ρ, K, ⊸, ꝺʒ, ꝑꝑ) and some values are inferred (16 = ce, ꝭs = t, …) ([OPEN.en.md](OPEN.en.md)).

## 11. Extending to the whole volume (this version)
- All 183 views were looked through at reduced size and every page with cipher found was transcribed (some may have been missed). Views 26 and 94 have plain text only; view 163 right is f. 158. Lines were cropped with src/autopage.py (line centres from ink peaks, then src/trackline.py follows each line).
- In the later hand (from view 125), the triangle ▲ is Δ (tri = i), a sign distinct from the round a (e); the ℌ-like sign with a tail is n (3n) and the 3-like sign with a tail is y (3y). The triangle was first written as a, so seven pages were re-transcribed from the images (notes in each file).
- Comparison: without fixing line correspondence, all signs of a page are joined and aligned by edit distance (src/ind_compare4.py). On 21 pages this differs from the line-by-line comparison by 0–1.0 points.

## 12. Image check of disagreements
- Places where two runs of the independent second transcription (two Codex runs, or Codex and Sonnet) disagreed with the first transcription in the same way became questions (src/mkcheck.py). A crop around the estimated place, enlarged 2.5× with a triangle mark, and the two readings (A and B, in random order) were shown to separate readers: Codex (fresh context) and Claude Sonnet (fresh context, a few dozen images per agent), later two Sonnet agents.
- A place was corrected only when the readers agreed on the second transcription's reading. Names in the y-shape class (s/p) and names not in the key were not changed (src/apply_checkp.py; decision lists in second/check/decisions*.tsv).
- Re-check: in some of the first Sonnet checks the images failed to load and the agent answered anyway (by its own report). Those answers were set aside (second/check/sonnet1_old/) and all were redone with an instruction to re-read failed images. Earlier corrections not supported by the redone answers were reverted.
- Some places that the check removed as "no sign here" were looked at again: where the crop did not show the place, or where a // is clearly visible, the first reading was restored (notes in each transcription).
- After correction, new independent second transcriptions not used for any correction were made; only those are used for the status ([PAGES.en.md](PAGES.en.md)).

## 13. Independent second transcription by Claude Sonnet (reference)
- Sonnet was given PROMPT3 and the line images. Whole line images (about 3000 px wide) were shown reduced, small signs were lost, and on f. 39v the value agreement was 63.4%. Given each line in left and right halves at full size, and asked to write each line straight after viewing it, Sonnet reached 78.0% (thirds: 76.5%). The two Codex runs on the same page reached 89.4% and 90.1%.
- Typical confusions: ⊣ read as t-shape, + or 1; the lr ligature (b) as L; Þ as a triangle; the 7-shaped sign left unnamed. They occurred although the sign list describes these differences, so they are taken as a limit of this reader.
- Sonnet runs are therefore shown for reference only and are not used for the status.

## 14. Status
- Only independent second transcriptions not used to correct that transcription count. The lower value agreement, the share of signs with a value and the control are applied to the criteria of §8 ([PAGES.en.md](PAGES.en.md)).

## 15. Prompt for view 168 right (v168r)
- On this page the Codex second transcription varied between 74.8% and 83.0% over four runs. By line and by type, triangle→a (43 in four runs) and Þ→triangle (21) were the most frequent consistent disagreements, while in the image check two Sonnet readers chose the first reading (triangle, Þ) every time, and swapping the readings lowers the French-likeness. In this hand Þ is an upright stroke with a black filled wedge at its upper right, which does not fit PROMPT3's description ("a closed loop on the upper right"); Codex called Þ a triangle and the flat black ▲ an a. Line cropping is not the cause (the number of signs per line is close).
- A prompt with only the descriptions of a, the triangle and Þ adapted to these letter forms, with no values (second/PROMPT3_v168r.md), was used for two new runs in fresh contexts (second/ind21, ind22): value agreement 88.5% and 85.6%. Triangle→a fell from 16 to 2 per run and Þ→triangle from 5 to 0. The status of this page rests on these two runs ("Codex*" in [PAGES.en.md](PAGES.en.md)). The transcription was not changed meanwhile.
