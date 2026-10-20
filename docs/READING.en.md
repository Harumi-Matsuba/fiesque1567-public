# Reading (five letters in BnF fr. 15919)

[日本語](READING.md)

The key is Satoshi Tomokiyo's reconstructed table (rows marked `table` in data/key.tsv). Values of signs not in the table were inferred from the context of these letters (`inferred`). How the figures were obtained and their limits: [METHOD.en.md](METHOD.en.md); open points: [OPEN.en.md](OPEN.en.md).

**No human has checked the transcription.** Both transcriptions are by AI: Claude (first) and Codex (independent second).

## Figures per letter (as in the first version)

**This table and the readings below are from the first version (2026-10-20).** The transcriptions were later corrected after image checks (ff. 39r, 39v, 79r and others); current figures and status are in [PAGES.en.md](PAGES.en.md), current mechanical decipherments in data/decoded_*.txt. Summaries of the other pages of the volume are also in [PAGES.en.md](PAGES.en.md).


| Letter | Date, addressee | Gallica view | Lines | Signs | Signs with a value (table+inferred / table only) | Control: true key / best of 1000 shuffled keys (table+inferred) | Same (table signs only) | Independent second transcription (value agreement) | Status |
|---|---|---|---|---|---|---|---|---|---|
| f.39r | 6 March 1568, Vienna, to the Queen Mother | view 43, right | 28 | 1182 | 99.4%／92.7% | -3.464／-4.805（0/1000） | -3.236／-4.327（0/1000） | 76.1% | partial |
| f.39v | (continuation of f.39r) | view 44, left | 19 | 729 | 98.4%／92.9% | -3.328／-4.743（0/1000） | -3.036／-4.435（0/1000） | 82.4% | partial |
| f.79r | 17 July 1568, Vienna, to the Queen Mother | view 83, right | 24 | 802 | 99.6%／93.3% | -3.141／-4.756（0/1000） | -2.945／-4.289（0/1000） | 81.5% | partial |
| f.94r | 14 August 1568, Vienna, to the Queen Mother | view 99, right | 25 | 867 | 99.9%／92.5% | -3.081／-4.592（0/1000） | -2.868／-4.253（0/1000） | 91.9% | full |
| f.100r | 4 September 1568, Vienna, to the King (endorsed "au Roy"; the text begins "Madame") | view 105, right | 27 | 996 | 99.7%／94.1% | -3.254／-4.677（0/1000） | -3.089／-4.446（0/1000） | 87.5% | full |
| f.158r | 29 October 1569, Vienna, to the King | view 163, right | 23 | 846 | 99.4%／92.1% | -3.091／-4.639（0/1000） | -2.873／-3.979（0/1000） | 90.5% | full |

- Control: in 1000 keys with the letter values shuffled, none gave a more French-like text than the true key, for every letter. French-likeness is the mean log-likelihood of letter trigrams built from the top 50,000 French words of wordfreq (src/control.py).
- Status follows [METHOD.en.md](METHOD.en.md) §8 (full reading needs, among others, ≥85% agreement with the independent second transcription; partial reading ≥70%). Even in letters meeting the full-reading criteria, most lines are marked "inf." below and include word division and filled-in spelling.
- Marks: "dir." = the key output reads directly as words. "inf." = includes word division, filled-in spelling, choosing s/p for the y-shaped sign, or re-reading similar signs. (?) = unread or a guess. [ ] = supplied letters.

## f. 39r–v (6 March 1568, to the Queen Mother)

**f. 39r** (preceding plain text: Madame, ma derniere l[ett]re a esté du penultiesme du passé, depuis laquelle)
| Line | Reading | Mark |
|---|---|---|
| c02 | J'ay entendu que le duc [J]ehan Guillaume | dir. |
| c03 | [de] Saxe, qui est allé en France pour vostre service, a amené avec | dir. |
| c04 | luy six [p]rescheu[r]s, qui sont d'une secte qui s'appelle Flacciani | inf. (output "srecheuis"; Flacciani taken to be the followers of Flacius Illyricus) |
| c05 | et luy a dit … qu'avec eulx et les armes il y [a] esperance (?) | inf. |
| c06 | [de] chastier les … (?) et huguenots, de quoy je ne faisoys | inf. |
| c07 | pas … grand compte, me semblant qu'il n'avoit a[ss]ez forces | inf. |
| c08 | pour faire ung tel exploict, mais … qu'il en fault | inf. |
| c09 | faire … j'estime que je ne pense, car il n'est … qu'il ne tache que | inf. |
| c10 | [à] croistre et augmenter la dicte secte, de laquelle | dir. |
| c11 | il y a long temps que son frere le duc Jehan Frederic, qu'il tient | dir. |
| c12 | prisonnier en estroict[e garde], et depuis les a chassés (?), et ledict duc | inf. |
| c13 | Jehan Guillaume les a recueillys, qu'il(s) esta[ient] … (?) | inf. |
| c14 | attendu que plusieurs de ses cappitaines sont parens et | inf. (output "srusieurs") |
| c15 | amys ceulx du … (?) et quasi d'une mesme secte que | inf. |
| c16 | vous … service que vous … (?) | inf. |
| c17 | non pas qu'il doubte que ledict duc Jehan Guillaume vous faille | inf. |
| c18 | [ny] face chose qui soit contre son honneur, et plusieurs | inf. |
| c19 | [à] ceste heure trouvent fort estrange que luy … (?) | inf. |
| c20 | [ayt] si grande charge, estant beau fils du comte [⊸] qui a esté | inf. (⊸ is not in the table; read as "Palatin", since Johann Wilhelm's father-in-law was the Elector Palatine) |
| c21 | cause … semble … ceste | inf. |
| c22 | guerre, et que ne vous perceviez que luy et le … (?) | inf. |
| c23 | … à ceste cause je croys | inf. |
| c24 | qu'il seroict le grand prouffit du roy … je vous ay | inf. |
| c25 | par plusieurs fois escript que ces gens … (?) | inf. |
| c26 | le royaume et vos forces françoises … (?) | inf. |
| c27 | et mesmes … (?) | inf. |
| c28 | sur ce faict est d'advis qu'il seroict … meilleur | inf. |
| c29 | que … ung seul … rigueur envers ceulx qui | inf. |

**f. 39v**
| Line | Reading | Mark |
|---|---|---|
| c01 | l'ont offencé, pourveu qu'ilz ne veuillent aucunes fortes | inf. |
| c02 | places en leurs mains, et … à aucunes leurs | inf. |
| c03 | demand[es] … livrer ces troupes … (?) | inf. |
| c04 | … que ces guerres durent … et que … ne peuvent | inf. |
| c05 | porter que grande ruyne et dommaige [16] royaulme, et | inf. (16 is not in the table; read "ce" from "ce royaume", "ce mariage" in f. 100 and f. 158) |
| c06 | selon la responce qu'il … qu'il vous a envoyé(e) | inf. |
| c07 | il s'employera pour vous veoir hors [de] ces guerres intesti- | dir. |
| c08 | nes, et à ce que je puis … je vous ay | inf. |
| c09 | … escris … avoir sur cela | inf. |
| c10 | volunté du roy … pour après … celuy | inf. |
| c11 | semblable … roy d'Espaigne pour le prier | inf. |
| c12 | … ceulx de Flandres | inf. |
| c13 | … a envoyé … ung courrier en Espaigne, qui n'esto[it] | inf. |
| c14 | pour aultre chose que pour … et moyenner | inf. |
| c15 | que … [reconc]iliation (?) entre luy et son fils … | inf. |
| c16 | est arrivé … ung courrier d'Espaigne, mais jusques | inf. |
| c17 | à ceste heure je n'en ay rien sceu apprendre … bien | inf. |
| c18 | … la cause de la prinse du prince | inf. (taken to be the arrest of Don Carlos, January 1568) |
| c19 | … qu'il tient secrette. | inf. |

Following plain text (read by eye, partly conjectural): Madame, voyant qu'à ceste heure je ne vous puis faire aucun service, et n'ayant aucune occasion pour y demeurer long temps, je vous prie tres humblement, s'il est à vostre bon plaisir, de me donner congé de m'en pouvoir retourner en France … De Vienne ce 6e de mars 1568. Signed Scipione Fiesco.

### Summary (conjectural; not checked against historical sources)
1. Duke Johann Wilhelm of Saxony ("Jehan Guillaume"), campaigning for the French king, brought six preachers of the Flacian sect.
2. His brother Johann Friedrich ("Jehan Frederic") is held prisoner.
3. Johann Wilhelm's captains are relatives and friends of the same sect.
4. The Emperor intends to work for an end of the civil war in France.
5. A courier to Spain, and the cause of "la prinse du prince", are kept secret.



## f. 79r (17 July 1568, to the Queen Mother)
Preceding plain text: Madame, ma derniere lettre a esté du … de ce moys, par laquelle je vous escripvis … ("Jay receu" is plain text). All lines are "inf."
- c01–c04：… que le sieur … grand [escuyer] de l'Empereur devoict aller en Espaigne, lequel n'est encores party … ne au[c]un courrier, et je n'ay sceu entendre à quoy tient ceste longue[ur].
- c05–c08：De mesme l'archeduc Charles est venu icy parler à l'Empereur, et aucuns m'ont voulu dire que c'est la grande [de]meure de la deliberation d'y envoier … courrier … avec … 
- c09–c12：… delivrance du prince, et qu'il s'est tenu quelques propos que l'archeduc Charles mesmes entrepren[droit] ce voyage, y ayans l'Empereur et l'imperatrice grand desir, et estans deliberés de [s']employer
- c13–c16：de tout leur pouvoir pour la delivrance dudict prince ; toutesfois je ne le puis asseurer, car les maniemens sont si secrets que jusques à ceste heure je n'en ay rien
- c17–c20：sceu descouvrir, dont je me suis efforcé (?) … et aussi que je n'en ay osé toucher aucunement à l'Empereur, par ce que … derniers propos que eu[smes] ensemble … que apres qu'il auroict
- c21–c24：despesché en Espaigne, qu'il me diroict encores combien de temps … il espereroict avoir responce, et que n'estant encores personne party, il m'a semblé que si je voyoie … de [p]ouvoir … quelque chose

### Summary (conjectural; not checked against historical sources)
At the imperial court there is talk of sending Archduke Charles to Spain for the "délivrance" of the Spanish prince Don Carlos (arrested January 1568, died 24 July 1568). Fiesque has not dared raise the matter with the Emperor.

## f. 94r (14 August 1568, to the Queen Mother)
Preceding plain text: Madame, J'ay receu vostre lettre du 9e de Juillet, par laquelle me escripvez (then the nulls "fi ol par moy"). All lines are "inf."
- c01–c03：que [vous] ayez … de bien entendre par le menu ce que les courriers d'Espaigne ont apporté, que j'ay faict les plus dili[gem]-
- c04–c07：ment qu'il m'a esté possible, de quoy toutesfois je n'ay peu aprendre aultre chose que ce que je vous ay escrist par les miennes precedentes ; vous aurez sceu par celle du [20?] de ce moys
- c08–c11：comme l'Empereur me disoict tousjours qu'il parleroict à moy depuis. Il m'a dict que ce qu'il me vouloict dire estoict qu'il envoye son frere l'archeduc Charles en Espaigne pour deux raisons, l'une
- c12–c15：le faict du prince d'Espaigne, et l'autre les affaires de Flandres, lesquelles semblent estre en estat d'avoir bon besoing de bonne provision, le bien du pays, repos de l'Allemaigne et de toute la
- c16–c19：chrestienté ; et qu'ayant la charge qu'il a, il est contrainct d'y faire toutes ses diligences, lesquelles il ne sçauroict faire avec plus grande efficace que d'envoyer son frere mesmes devers
- c20–c25：le Roy [d'Espaigne], luy faire entendre son advis et ce que jugent estre necessaire tous les princes d'Allemaigne, pour le bien de son pays de Flandres ; il sera bien aise s'il est en ambassade … trouvé bonne, et qu'elle sorte fruict, et si elle ne prouffite à tout le moings sera il deschargé envers Dieu et tout

### Summary (conjectural; not checked against historical sources)
The Emperor told Fiesque that he is sending his brother Archduke Charles to Spain, for two reasons: the affair of the prince (Don Carlos) and the affairs of Flanders. This confirms, from the Emperor himself, what f. 79 reported as rumour.

## f. 100r (4 September 1568, to the King)
Preceding plain text: Madame, J'ay receu vostre lettre du … du passé
| Line | Reading | Mark |
|---|---|---|
| c01 | et dict | inf. |
| c02 | … que l'homme que je vous avois envoyé estoict revenu (?) | inf. |
| c03 | et que ne m'aviez envoyé [res]ponce plus tost, attendant | inf. |
| c04 | que l'Em[pereur] fut [b]ien guery, … qu'il s'avoict eu plus | inf. (output "ciengueryle"; the sign for b could not be decided between the t-shape and 4 on the image, so it stays a t-shape (c); "bien" is supplied from context) |
| c05 | vingt jours la fievre, mais qu'il se sortoict | inf. (reading after ⊣ and # were corrected, checked on the image) |
| c06 | bien quand mon homme … qui fut le | inf. (reading after ⊢ = q was corrected) |
| c07 | vingt-huict … il avoict desja huict jours que | inf. |
| c08 | … la joye aussi que vous m'aviez | inf. |
| c09 | escrist que trouviez bon ce que [il] trouvoict bon, il que | inf. |
| c10 | vous estiez bien aise que de me[ttre] en ceste … volunté | inf. |
| c11 | d'achever le mariage en la … que … vous trouver | inf. (ϖ corrected to m after checking the image; the output then reads "le mariage en") |
| c12 | tousjours … desirant que ceste … | inf. |
| c13 | que vous avez … estrainte avec une | inf. |
| c14 | … alliance, il m'a dict qu'à ceste heure il n'y a plus | inf. (after ⊢ = q was corrected, the output reads like this) |
| c15 | aucune difficulté que le mariage [ne se] face | inf. |
| c16 | [puisque le pr]ince d'Espaigne estoict [mort], mais que | inf. ("mort" re-reads the output "um?ct"; Don Carlos died on 24 July 1568) |
| c17 | … immediate … mariage … | inf. |
| c18 | en quoy il n'estoict … qu'il … | inf. |
| c19 | … que vous en … | inf. |
| c20 | que je croy … seurement que vous trouverez … que | inf. |
| c21 | … le remede … l'alliance … intelligence | inf. |
| c22 | que aviez ensemble, il [dit] que ja vous luy aviez faict entendre | inf. (output after ⊢ = q was corrected: "queauiesensemoleil") |
| c23 | … que vous estiez … avec sa majesté | inf. |
| c24 | ce mariage … intention | inf. |
| c25 | … alliance que pensez … | inf. |
| c26 | tenant … son fils … amys … | inf. |
| c27 | il … qu'il envoye … en Espaigne que … | inf. |

### Summary (conjectural; not checked against historical sources)
The negotiation of the marriage of the King (Charles IX) with the Emperor's daughter. The Emperor seems to have told Fiesque that, the Spanish prince (Don Carlos) being dead, there is now no obstacle to the marriage.

## f. 158r (29 October 1569, to the King)
Preceding plain text: Sire, J'ay receu voz lettres du … et … de ce moys. (then the nulls "Il ri ol")
| Line | Reading | Mark |
|---|---|---|
| c01–c02 | avec la co[ntinuatio]n (?) de la … responce que avez faicte à ma …, qui vient (?) dict | inf. |
| c03 | comme vous estiez [p]rest à partir pour aller trou- | inf. (p is the y-shaped sign) |
| c04 | ver ce camp (?) pour poursuyvre le fruict de la victoire | inf. (taken to be the victory of Moncontour, 3 October 1569) |
| c05 | que Dieu vous a donnée (?) … sous les principaulx seig- | inf. |
| c06 | neurs et cappitaines de ce royaume, avec lesquelz | inf. |
| c07 | prendre … que bonne resolution, et mesmes sur l'o[ffre] | inf. |
| c08 | qu'il vous a faict de se vouloir employer à traicter l[a paix] | inf. |
| c09 | que, … quelques bonnes … pacification sur les troubles (?) qui | inf. |
| c10 | sont, et [vostre majesté] m'a commandé de le remercier fort | inf. |
| c11 | de la demonstration qu'il [a] faict d'avoir tousjours | dir. |
| c12 | en singuliere recommandation le bien, prouffit et | inf. |
| c13 | utilité de ce royaume, et que comme … desire | inf. |
| c14 | … en tout ce que l'un touchera l'autre (?) | inf. |
| c15 | m'a dict qu'il ne s'est meu à mettre en avant ce parti (?) | inf. |
| c16 | que pour une sincere affection et grand desir qu'il a de | inf. |
| c17 | veoir delivré de ceste guerre intestine, et mesme- | inf. |
| c18 | ment à ceste heure qu'il n'aura (?) ceste estroicte alliance de ce | inf. |
| c19 | mariage avec sa fille … de faire tout ce que ser[a] | inf. |
| c20 | en son pouvoir, estant en la mesme opinion qu'il a tou- | inf. |
| c21 | jours esté, que en ce que pourriez remedier avec dou- | inf. |
| c22 | ceur, que n'y usiez de rigueur, estant [de] nature vo[stre majesté] | inf. |
| c23 | tousjours encline à clemence envers vos subjects (?) | inf. |
Following plain text: Il luy ay dict que depuis la victoire …

### Summary (conjectural; not checked against historical sources)
The Emperor congratulates the King on his victory (taken to be Moncontour) and offers to mediate an end of the civil war (peace with the Huguenots). In his words, with the "estroicte alliance" of the marriage with his daughter, he recommends clemency towards the subjects ("douceur" rather than "rigueur").
