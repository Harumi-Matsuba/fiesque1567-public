# 読み（BnF fr.15919 の5通）

[English](READING.en.md)

鍵は友清理士氏の復元表（data/key.tsv の table の行）。表にない記号の値は、この書簡群の文脈から補った（inferred）。数字の出し方と限界は [METHOD.md](METHOD.md)、未解決の点は [OPEN.md](OPEN.md)。

**人は書き起こしを確かめていない。** 書き起こしは Claude（1回目）と Codex（独立の2回目）による。

## 書簡ごとの数字（初版のときの数字）

**この表と下の解読文は初版（2026-10-20）のもの。** その後、画像の確かめで書き起こしを直した（f.39r・f.39v・f.79r など）ので、今の数字と状態は [PAGES.md](PAGES.md)、今の機械的な解読は data/decoded_*.txt を見る。巻のほかのページの要約も [PAGES.md](PAGES.md)。


| 書簡 | 日付・宛先 | Gallica のコマ | 行 | 記号 | 値の付いた割合（表＋推定／表だけ） | 対照：本物の鍵／かき混ぜの最大（表＋推定） | 同（表の記号だけ） | 独立の2回目（値の一致） | 状態 |
|---|---|---|---|---|---|---|---|---|---|
| f.39r | 1568年3月6日、ウィーン、王妃宛 | v43 の右ページ | 28 | 1182 | 99.4%／92.7% | -3.464／-4.805（0/1000） | -3.236／-4.327（0/1000） | 76.1% | 部分的 |
| f.39v | （f.39r の続き） | v44 の左ページ | 19 | 729 | 98.4%／92.9% | -3.328／-4.743（0/1000） | -3.036／-4.435（0/1000） | 82.4% | 部分的 |
| f.79r | 1568年7月17日、ウィーン、王妃宛 | v83 の右ページ | 24 | 802 | 99.6%／93.3% | -3.141／-4.756（0/1000） | -2.945／-4.289（0/1000） | 81.5% | 部分的 |
| f.94r | 1568年8月14日、ウィーン、王妃宛 | v99 の右ページ | 25 | 867 | 99.9%／92.5% | -3.081／-4.592（0/1000） | -2.868／-4.253（0/1000） | 91.9% | 全文 |
| f.100r | 1568年9月4日、ウィーン、国王宛（注記「au Roy」、本文は Madame で始まる） | v105 の右ページ | 27 | 996 | 99.7%／94.1% | -3.254／-4.677（0/1000） | -3.089／-4.446（0/1000） | 87.5% | 全文 |
| f.158r | 1569年10月29日、ウィーン、国王宛 | v163 の右ページ | 23 | 846 | 99.4%／92.1% | -3.091／-4.639（0/1000） | -2.873／-3.979（0/1000） | 90.5% | 全文 |

- 対照：鍵の文字の値をかき混ぜた1000回で、本物の鍵より仏語らしくなった回は、どの書簡も0回。仏語らしさは、wordfreq の仏語上位5万語で作った文字3連の対数尤度の平均（src/control.py）。
- 状態は [METHOD.md](METHOD.md) §8 の基準による（独立の2回目 85% 以上などで全文の読み、70% 以上で部分的な読み）。全文の読みの基準を満たす書簡でも、行の大半は下の【推】で、語の切れ目や綴りの補いを含む。
- 印：【確】は、鍵の出力がそのまま語として読める行。【推】は、語の切れ目・綴りの補い・y 形の s／p の読み分け・似た記号の読み替えを含む行。(?) は読めていないか当て推量。[ ] は補った文字。

## f.39r–v（1568年3月6日、王妃宛）

**f.39r**（前の平文：Madame, ma derniere l[ett]re a esté du penultiesme du passé, depuis laquelle）
| 行 | 解読文 | 印 |
|---|---|---|
| c02 | J'ay entendu que le duc [J]ehan Guillaume | 確 |
| c03 | [de] Saxe, qui est allé en France pour vostre service, a amené avec | 確 |
| c04 | luy six [p]rescheu[r]s, qui sont d'une secte qui s'appelle Flacciani | 推（出力は srecheuis。Flacciani は Flacius Illyricus 派と推定） |
| c05 | et luy a dit … qu'avec eulx et les armes il y [a] esperance (?) | 推 |
| c06 | [de] chastier les … (?) et huguenots, de quoy je ne faisoys | 推 |
| c07 | pas … grand compte, me semblant qu'il n'avoit a[ss]ez forces | 推 |
| c08 | pour faire ung tel exploict, mais … qu'il en fault | 推 |
| c09 | faire … j'estime que je ne pense, car il n'est … qu'il ne tache que | 推 |
| c10 | [à] croistre et augmenter la dicte secte, de laquelle | 確 |
| c11 | il y a long temps que son frere le duc Jehan Frederic, qu'il tient | 確 |
| c12 | prisonnier en estroict[e garde], et depuis les a chassés (?), et ledict duc | 推 |
| c13 | Jehan Guillaume les a recueillys, qu'il(s) esta[ient] … (?) | 推 |
| c14 | attendu que plusieurs de ses cappitaines sont parens et | 推（出力は srusieurs） |
| c15 | amys ceulx du … (?) et quasi d'une mesme secte que | 推 |
| c16 | vous … service que vous … (?) | 推 |
| c17 | non pas qu'il doubte que ledict duc Jehan Guillaume vous faille | 推 |
| c18 | [ny] face chose qui soit contre son honneur, et plusieurs | 推 |
| c19 | [à] ceste heure trouvent fort estrange que luy … (?) | 推 |
| c20 | [ayt] si grande charge, estant beau fils du comte [⊸] qui a esté | 推（⊸ は表にない記号。Johann Wilhelm の義父はプファルツ選帝侯なので「Palatin」と推定） |
| c21 | cause … semble … ceste | 推 |
| c22 | guerre, et que ne vous perceviez que luy et le … (?) | 推 |
| c23 | … à ceste cause je croys | 推 |
| c24 | qu'il seroict le grand prouffit du roy … je vous ay | 推 |
| c25 | par plusieurs fois escript que ces gens … (?) | 推 |
| c26 | le royaume et vos forces françoises … (?) | 推 |
| c27 | et mesmes … (?) | 推 |
| c28 | sur ce faict est d'advis qu'il seroict … meilleur | 推 |
| c29 | que … ung seul … rigueur envers ceulx qui | 推 |

**f.39v**
| 行 | 解読文 | 印 |
|---|---|---|
| c01 | l'ont offencé, pourveu qu'ilz ne veuillent aucunes fortes | 推 |
| c02 | places en leurs mains, et … à aucunes leurs | 推 |
| c03 | demand[es] … livrer ces troupes … (?) | 推 |
| c04 | … que ces guerres durent … et que … ne peuvent | 推 |
| c05 | porter que grande ruyne et dommaige [16] royaulme, et | 推（16 は表にない数字。f.100・f.158 の「ce royaume」「ce mariage」から ce と推定） |
| c06 | selon la responce qu'il … qu'il vous a envoyé(e) | 推 |
| c07 | il s'employera pour vous veoir hors [de] ces guerres intesti- | 確 |
| c08 | nes, et à ce que je puis … je vous ay | 推 |
| c09 | … escris … avoir sur cela | 推 |
| c10 | volunté du roy … pour après … celuy | 推 |
| c11 | semblable … roy d'Espaigne pour le prier | 推 |
| c12 | … ceulx de Flandres | 推 |
| c13 | … a envoyé … ung courrier en Espaigne, qui n'esto[it] | 推 |
| c14 | pour aultre chose que pour … et moyenner | 推 |
| c15 | que … [reconc]iliation (?) entre luy et son fils … | 推 |
| c16 | est arrivé … ung courrier d'Espaigne, mais jusques | 推 |
| c17 | à ceste heure je n'en ay rien sceu apprendre … bien | 推 |
| c18 | … la cause de la prinse du prince | 推（1568年1月のドン・カルロス逮捕と推定） |
| c19 | … qu'il tient secrette. | 推 |

後の平文（目視、推定を含む）：Madame, voyant qu'à ceste heure je ne vous puis faire aucun service, et n'ayant aucune occasion pour y demeurer long temps, je vous prie tres humblement, s'il est à vostre bon plaisir, de me donner congé de m'en pouvoir retourner en France … De Vienne ce 6e de mars 1568. 署名 Scipione Fiesco。

### 内容の要点（推定。史実との照合はしていない）
1. ザクセン公 Johann Wilhelm（Jehan Guillaume）が、フランス王のための出兵に Flacius 派の説教師を6人連れて行ったこと。
2. 兄の Johann Friedrich（Jehan Frederic）が幽閉されていること。
3. Johann Wilhelm の隊長たちが同じ派の縁者であること。
4. 皇帝が、フランスの内戦を終わらせるよう尽力するつもりであること。
5. スペインへの急使と「王子の逮捕」の理由が秘されていること。

いずれも史実との照合はまだしていない。

## f.79r（1568年7月17日、王妃宛）
前の平文：Madame, ma derniere lettre a esté du … de ce moys, par laquelle je vous escripvis …（「Jay receu」は平文）
- c01–c04：… que le sieur … grand [escuyer] de l'Empereur devoict aller en Espaigne, lequel n'est encores party … ne au[c]un courrier, et je n'ay sceu entendre à quoy tient ceste longue[ur].
- c05–c08：De mesme l'archeduc Charles est venu icy parler à l'Empereur, et aucuns m'ont voulu dire que c'est la grande [de]meure de la deliberation d'y envoier … courrier … avec … 
- c09–c12：… delivrance du prince, et qu'il s'est tenu quelques propos que l'archeduc Charles mesmes entrepren[droit] ce voyage, y ayans l'Empereur et l'imperatrice grand desir, et estans deliberés de [s']employer
- c13–c16：de tout leur pouvoir pour la delivrance dudict prince ; toutesfois je ne le puis asseurer, car les maniemens sont si secrets que jusques à ceste heure je n'en ay rien
- c17–c20：sceu descouvrir, dont je me suis efforcé (?) … et aussi que je n'en ay osé toucher aucunement à l'Empereur, par ce que … derniers propos que eu[smes] ensemble … que apres qu'il auroict
- c21–c24：despesché en Espaigne, qu'il me diroict encores combien de temps … il espereroict avoir responce, et que n'estant encores personne party, il m'a semblé que si je voyoie … de [p]ouvoir … quelque chose

### 内容の要点（推定。史実との照合はしていない）
スペイン王子ドン・カルロス（1568年1月に逮捕、7月24日に死去）の「délivrance」について、皇帝の宮廷で、カール大公をスペインへ送る案が話されていること。Fiesque は皇帝にこの件を切り出せずにいる。史実との照合はまだしていない。

## f.94r（1568年8月14日、王妃宛）
前の平文：Madame, J'ay receu vostre lettre du 9e de Juillet, par laquelle me escripvez（その後に無効字 fi ol par moy）
- c01–c03：que [vous] ayez … de bien entendre par le menu ce que les courriers d'Espaigne ont apporté, que j'ay faict les plus dili[gem]-
- c04–c07：ment qu'il m'a esté possible, de quoy toutesfois je n'ay peu aprendre aultre chose que ce que je vous ay escrist par les miennes precedentes ; vous aurez sceu par celle du [20?] de ce moys
- c08–c11：comme l'Empereur me disoict tousjours qu'il parleroict à moy depuis. Il m'a dict que ce qu'il me vouloict dire estoict qu'il envoye son frere l'archeduc Charles en Espaigne pour deux raisons, l'une
- c12–c15：le faict du prince d'Espaigne, et l'autre les affaires de Flandres, lesquelles semblent estre en estat d'avoir bon besoing de bonne provision, le bien du pays, repos de l'Allemaigne et de toute la
- c16–c19：chrestienté ; et qu'ayant la charge qu'il a, il est contrainct d'y faire toutes ses diligences, lesquelles il ne sçauroict faire avec plus grande efficace que d'envoyer son frere mesmes devers
- c20–c25：le Roy [d'Espaigne], luy faire entendre son advis et ce que jugent estre necessaire tous les princes d'Allemaigne, pour le bien de son pays de Flandres ; il sera bien aise s'il est en ambassade … trouvé bonne, et qu'elle sorte fruict, et si elle ne prouffite à tout le moings sera il deschargé envers Dieu et tout

### 内容の要点（推定。史実との照合はしていない）
皇帝が、弟のカール大公をスペインへ送ると Fiesque に告げた。理由は2つで、王子（ドン・カルロス）の件と、フランドルの件。f.79 で噂として書いた話を、皇帝本人から聞いた報告になっている。史実との照合はまだしていない。

## f.100r（1568年9月4日、国王宛）
前の平文：Madame, J'ay receu vostre lettre du … du passé
| 行 | 解読文 | 印 |
|---|---|---|
| c01 | et dict | 推 |
| c02 | … que l'homme que je vous avois envoyé estoict revenu (?) | 推 |
| c03 | et que ne m'aviez envoyé [res]ponce plus tost, attendant | 推 |
| c04 | que l'Em[pereur] fut [b]ien guery, … qu'il s'avoict eu plus | 推（出力は「ciengueryle」。b に当たる記号は、t 形か 4 か画像で決めきれないので t 形（c）のまま。「bien」は文脈による補い） |
| c05 | vingt jours la fievre, mais qu'il se sortoict | 推（2回目の書き起こしとの照合で ⊣・# を直した後の読み） |
| c06 | bien quand mon homme … qui fut le | 推（⊢＝q を直した後の読み） |
| c07 | vingt-huict … il avoict desja huict jours que | 推 |
| c08 | … la joye aussi que vous m'aviez | 推 |
| c09 | escrist que trouviez bon ce que [il] trouvoict bon, il que | 推 |
| c10 | vous estiez bien aise que de me[ttre] en ceste … volunté | 推 |
| c11 | d'achever le mariage en la … que … vous trouver | 推（2回目の書き起こしとの照合で pi を m に直した。直した後の出力は「le mariage en」） |
| c12 | tousjours … desirant que ceste … | 推 |
| c13 | que vous avez … estrainte avec une | 推 |
| c14 | … alliance, il m'a dict qu'à ceste heure il n'y a plus | 推（⊢＝q を直した後、出力がこのとおりになった） |
| c15 | aucune difficulté que le mariage [ne se] face | 推 |
| c16 | [puisque le pr]ince d'Espaigne estoict [mort], mais que | 推（「mort」は出力 um?ct の読み替え。ドン・カルロスは1568年7月24日に死去） |
| c17 | … immediate … mariage … | 推 |
| c18 | en quoy il n'estoict … qu'il … | 推 |
| c19 | … que vous en … | 推 |
| c20 | que je croy … seurement que vous trouverez … que | 推 |
| c21 | … le remede … l'alliance … intelligence | 推 |
| c22 | que aviez ensemble, il [dit] que ja vous luy aviez faict entendre | 推（⊢＝q を直した後の出力「queauiesensemoleil」） |
| c23 | … que vous estiez … avec sa majesté | 推 |
| c24 | ce mariage … intention | 推 |
| c25 | … alliance que pensez … | 推 |
| c26 | tenant … son fils … amys … | 推 |
| c27 | il … qu'il envoye … en Espaigne que … | 推 |

### 内容の要点（推定。史実との照合はしていない）
国王（シャルル9世）と皇帝の娘との結婚の交渉。皇帝は、スペイン王子（ドン・カルロス）が亡くなったので、今は結婚に支障がないと Fiesque に語ったようだ。史実との照合はまだしていない。

## f.158r（1569年10月29日、国王宛）
前の平文：Sire, J'ay receu voz lettres du … et … de ce moys.（その後に無効字 Il ri ol）
| 行 | 解読文 | 印 |
|---|---|---|
| c01–c02 | avec la co[ntinuatio]n (?) de la … responce que avez faicte à ma …, qui vient (?) dict | 推 |
| c03 | comme vous estiez [p]rest à partir pour aller trou- | 推（p は y 形） |
| c04 | ver ce camp (?) pour poursuyvre le fruict de la victoire | 推（1569年10月3日のモンコントゥールの戦勝と推定） |
| c05 | que Dieu vous a donnée (?) … sous les principaulx seig- | 推 |
| c06 | neurs et cappitaines de ce royaume, avec lesquelz | 推 |
| c07 | prendre … que bonne resolution, et mesmes sur l'o[ffre] | 推 |
| c08 | qu'il vous a faict de se vouloir employer à traicter l[a paix] | 推 |
| c09 | que, … quelques bonnes … pacification sur les troubles (?) qui | 推 |
| c10 | sont, et [vostre majesté] m'a commandé de le remercier fort | 推 |
| c11 | de la demonstration qu'il [a] faict d'avoir tousjours | 確 |
| c12 | en singuliere recommandation le bien, prouffit et | 推 |
| c13 | utilité de ce royaume, et que comme … desire | 推 |
| c14 | … en tout ce que l'un touchera l'autre (?) | 推 |
| c15 | m'a dict qu'il ne s'est meu à mettre en avant ce parti (?) | 推 |
| c16 | que pour une sincere affection et grand desir qu'il a de | 推 |
| c17 | veoir delivré de ceste guerre intestine, et mesme- | 推 |
| c18 | ment à ceste heure qu'il n'aura (?) ceste estroicte alliance de ce | 推 |
| c19 | mariage avec sa fille … de faire tout ce que ser[a] | 推 |
| c20 | en son pouvoir, estant en la mesme opinion qu'il a tou- | 推 |
| c21 | jours esté, que en ce que pourriez remedier avec dou- | 推 |
| c22 | ceur, que n'y usiez de rigueur, estant [de] nature vo[stre majesté] | 推 |
| c23 | tousjours encline à clemence envers vos subjects (?) | 推 |
後の平文：Il luy ay dict que depuis la victoire …

### 内容の要点（推定。史実との照合はしていない）
皇帝が、国王の戦勝（モンコントゥールと推定）を祝い、内戦の終結（ユグノーとの和平）の仲介を申し出たことを伝えている。皇帝の言葉として、娘との結婚による「estroicte alliance」と、臣下への寛大さ（rigueur でなく douceur）を勧めることが書かれている。史実との照合はまだしていない。
