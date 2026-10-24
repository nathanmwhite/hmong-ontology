## Overview

This is intended as a quick, but semi-thorough first pass, and provides a preliminary review.

For this review, there are several big-picture caveats to the approach as we discussed in our Zoom chat, which in my opinion would be inevitable for any automated approach and thus worth incorporating into planning:
1. Like other SEA languages, Hmong tends to have vocabulary items with semantic extensions very different from European languages, which are strongly represented in the pivots, etc. The same issue applies to syntactic patterns and transitivity.
2. Online lists of vocabulary for Hmong, including some academically reviewed ones, typically are the result of a Hmong speaker who has been asked to translate English words into Hmong. When encountering a problematic word, a Hmong person may do one of the following, for example:
a. Translate the meaning ad hoc as a phrase,
b. Render the English word in Hmong orthography as if it adhered to Hmong phonology,
c. Give their best guess, sometimes based on a misunderstanding of an English researcher's explanation, or
d. Use a word that bears some semantic similarity.
Thus, we have to be careful about these sources. I'd point out the "translationese" section in my 2022 paper that touches on this issue: https://link.springer.com/article/10.1007/s10579-022-09596-2. And yes, I'll work on making available the resources from that work as well.
3. ISO 639-3 codes for Hmong languages are unfinished work--White Hmong and Green Mong are dialects, not languages, and most Hmong languages have no unique code.
4. We will need to have a robust way to handle regional variants for White Hmong and Green Mong, as discussed. For example, Bertrais-Charrier (1979) is on Thai White Hmong.


## review-conflicts-WH.tsv

My comments here focus on the definitions provided accompanying each ILI.
cai: This word does have the full range of meanings here, at least in the diaspora. "accepted or habitual practice" is the traditional meaning, extended to "rule, law".
dab: the range of meanings is supported for this word. It means "spirit", and potentially an "evil" one.
dej: It's hard to exactly distinguish the two ILIs here. The word means "water; river".
hli: I can confirm that `hli` means the natural satellite of the Earth; I can't confirm whether it refers to the natural satellite of any planet, as I have no evidence of speakers ever talking about such things.
hnoos: It's hard to exactly distinguish the two ILIs here.
hnub qub: It's hard to exactly distinguish the two ILIs here.
hu: It means "call". I'm not convinced of "shout, yell, scream". It does not mean "send for". Is there an ILI that actually means "call" with its core sense? As in "his name is called X" or "we call him X", "call" by phone, etc.?
khw: i56021 is safe. I can't confirm if it's ever been extended to the meaning of i41147.
mob: both are correct.
nceb: It's hard to exactly distinguish the two ILIs here.
noob: i98741 is correct. noob is a seed, not a hard fruit.
nyuj: It means i48233, not the female in particular.
paj: Both are acceptable.
phom: It means "gun" (i54499). I'm sure this covers "pistol" or "handgun", but doesn't specifically mean those.
pob: i50388 is correct; I cannot confirm if the semantic extension to i109982 has been made.
thee: It's hard to exactly distinguish the two ILIs here.
tsev neeg: this is a phrase
tua: Both are acceptable.
ua: Both are acceptable.
xyoob: Both are acceptable.

TODO:
cais
da dej
deb
nqi
ntse
zaub mov
ze


## review-triangulation-GM.tsv

These are all phrases. Other than that, it's probably all right.

review-triangulation-WH.tsv:
This is a mix of things: some individual words, some phrases. I haven't dug into the ILIs themselves, and especially not for the other languages cross-listed. However, for several items the Wiktionary senses listed are straightforwardly not correct.
If two ILIs are equally supported, it might be helpful to spell out the candidate senses for each in the table for quick validation, as often here only one Wiktionary sense appears.
That said, Hmong tends to have vocabulary items with semantic extensions (and transitivity!) very different from European languages, which are strongly represented in the table's pivots.
The comments here are intended as a first pass, and could be enriched or otherwise improved with more attention.

### Individual details
dab tsi, line 8: The Wiktionary sense is not correct: `dab tsi` isn't a fused relative. It's a pronoun meaning `what` and appears in situ. It can also have indefinite reference as "something", "anything".
dhau, lines 10-11: The Wiktionary senses are not correct for `dhau`. `dhau` means to "pass beyond" a point of reference or, with a stative verb, "be too much". The ILI referenced in line 12 corresponding to Wiktionary's "to move past" is a reasonable fit.
heev, line 17: `heev` literally means "be strong". It's used in a degree construction that indicates a high degree, "V very (much), a lot". The Wiktionary sense is too strong: heev doesn't have a superlative sense.
khawb, line 19: khawb doesn't necessarily contain the "remove part of something" component of the Wiktionary entry.
koj puas nyob zoo, line 20: This is a sentence.
koob, line 21: This means "needle, pin". The gloss "quill" refers to those of a porcupine, only in the sense that English uses "quill" for this (the Hmong here are really just saying "needle"). The pivots here do not align well with the Hmong sense.
kuv hlub koj, line 23: This is a sentence. The usage is more generic than "to a lover or spouse".
li cas, line 24: This is a phrase. It's not a fused relative, and the Wiktionary sense is not accurate.
mob, line 25: The Wiktionary sense is not correct. `mob` means "to be sick" or "illness". It doesn't imply causation.
nam pa, line 26: Could you confirm the provenance of this item? I don't recognise it.
nkag siab, lines 27-28: Line 27 has the correct sense.
nrog, line 31: A caution here: `nrog`'s primary function is as a verb meaning "to accompany, be with".
nws, line 33: This is a generic 3rd person singular pronoun; it encodes no gender. Given how frequently languages have this, an ILI for this seems reasonable.
pawg ntseeg, line 34: This is a phrase. It means roughly "believing group (of people)". The Mormon use is probably correct.
pom koj tom qab, line 36: This is a phrase.
qhov no, line 37: This is a phrase.
qhov zoo, line 38: This is a phrase.
rab diav kav fes, line 39: This is a phrase. I question whether it might be an ad hoc expression.
siab, line 42: The Wiktionary sense is not correct. This word means "liver", not "heart". It's used in idiomatic expressions where an English speaker would use "heart" in the figurative sense.
tawv nqaij, line 46: This is a phrase.
thee, line 47: This means "charcoal", not a drawing.
thov txim, line 50: This is a phase. It's literally a request to be excused from one's moral misconduct.
tig, lines 51-54: The best senses are lines 51 and 53. Line 52 is not correct. `tig` is generally intransitive, so line 54 is dubious. This is a good example where inference from equivalent terms in other languages leads to false positives.
tseeb, line 55-56: Line 56 has the right Wiktionary sense; line 55 is not the word usually used for that concept.
tsoo, lines 58-62: Most of these are not correct. The correct Wiktionary senses appears on lines 60-61.
tswv, lines 63-64: The Wiktionary sense on line 63 is the typical meaning, and can extend into historical slavery contexts which might roughly touch on line 64's meaning. The word typically takes on religious tones in the diaspora.
vaj, lines 66-69: This means "garden"--the meaning in line 69. I wouldn't be willing to defend the senses on lines 67-68. Note here: the pivots look odd when comparing against the Wiktionary entries: e.g., for line 68, the entries for each language listed don't match the Wiktionary sense listed, and they are not listed on Wiktionary with those meanings, either.
vaj tsiaj, line 70: This is a phrase, not a word. In a diaspora context, it means "zoo".
xiav, lines 71-72: The boundary between `xiav` "blue" and `ntsuab` "green" in Hmong is not the same as that in English, but to argue that xiav means "grue" is problematic since that concept handles the colour term for languages that lack specific terms for "blue" and "green". The corresponding terms in the other languages for line 71 look correct.

TODO:
faus, line 15: I'm not yet convinced of 'embed' for faus. This would be worth a corpus review.


## review-wiktionary-WH.tsv (a sample)

These are generally as above in review-triangulation-WH.tsv.
qhov zoo, line 2: This is a phrase. It's "good thing" or "goodness" in the most generic sense.
heev, line 3: This is literally "be strong", a stative verb. It's used in a construction to mean "very".
kev, line 4: This is a road, and it doesn't have to be paved, nor does it need to be in a village or town.
tshuab, line 5: None of the ILIs have senses that correspond. This literally just means "to blow", i.e., directed exhalation.
mob, line 6: It's i22102.
siab, line 7: This means "liver".
tseeb, lines 8-9: It's i13638.
ntev, line 10: It's i7833, though i7859 is possible.
dhau, lines 11-12: The best senses are likely i32002, i27684, i31995.
vaj, lines 13-16: It's i54178.
this vis, line 17: This references a physical television set.


## Comments on other files

### class_nouns.tsv

Bisang (1993) did not provide strict language-internal criteria for what he calls a "class noun" vs. "classifier", etc., relying instead to some extent on semantics alone. For "class nouns", the result tends to be (syntactically) a combination of prefixes, standalone words, and classifiers.
My subsequent work provides a definition and then proceeds to clean up Bisang's analysis. True class terms are prefixes, not standalone words, so I wonder if we want these as separate entries in scope, or include all words that have these as prefixes.

### classifiers-white2021.tsv

You appear to distinguish between "mensural" and "group" classifiers. The second subclass likely corresponds to my "collective mensural" classifiers. I'll give this some more thought; the below are preliminary comments.

li/le: This is a possessed classifier. It's derived ultimately from Chinese 的, but syntactically it's a classifier in Hmong.
cov: "group" mapping is probably sufficient
tej: "group" mapping is probably sufficient
pawg: this one has two meanings

TODO:
sab/saab, ntav/nta/ntaav/ntaa, tog
qhov
zaum/zaus 
nplooj, kab/kaab, sob
pob

khawv: Hmong has a lexical process (the tone melody alternation in 2.3.1) where a numeral of the -b tone class changes a following -v tone to an unmarked mid tone.
 The pattern: `khawv N`, `ib khaw N`.
riam/rag: The WH form is riam, which gets realized as riag with the tone melody alternation. The typical GM form is `rag`, of which I also attested a White Hmong-inspired variant riag in my research among diaspora speakers.
 The GM citation form is `rag`, not `*ram`.
family: both, noted as diaspora Hmong.
zaum (lines 195-196): There's a typo on p. 409 of the thesis. It should read "WH zaum/zaus". I have this in a list of errata and corrigenda. GM is `zag`, as it appears elsewhere in the thesis.
phau: This is fine.
measure words: have the syntactic property of numeral classifier syntax, but behave as their own class.
"Classifiers glossed only in the interlinear appendix texts"--I can think of no reason not to include these.

### classifiers.tsv

The LLM-generated comments appear to mix up a few things in its summary of its analysis here, and I've commented below to clarify a few items.

A. "What Bisang adds to White, and where they disagree." To repeat my comment above:
Bisang (1993) did not provide strict language-internal criteria for what he calls a "class noun" vs. "classifier", etc., relying instead to some extent on semantics alone. For "class nouns", the result tends to be (syntactically) a combination of prefixes, standalone words, and classifiers.
My subsequent work provides a definition and then proceeds to reorganise Bisang's analysis. True class terms are prefixes, not standalone words, so I wonder if we want these as separate entries in scope, or include all words that have these as prefixes.

B. "Bisang then supplies what White leaves out -- measure words, class
 nouns, the finer [+-exact]/[+-entity] distinctions -- and the forms White's
 chapter does not reach."
My thesis does cover measure words (Section 7.6.1) and class nouns (Section 3.2.4.1 as "class term prefixes"). If my classifier chapter does not cover it, it is because I determined from syntactic tests that it's not a classifier, and the relevant sections of the thesis can be reviewed by LLM for these other items. Note: I checked every one of the terms in Bisang's appendices in this work.

1. "Measure words, which White excludes and Bisang counts."
They have the syntactic properties of numeral classifiers in my analysis (Section 7.6.1), so they of course can be treated together with classifiers, as was done in my thesis.

2. "Class nouns, which White rejects outright -- see item 5 below."
This is not correct -- see item 5 below.

5. "White rejects Bisang's class-noun analysis of phau, lo and the rest outright: Bisang "does not provide evidence that would support this class noun analysis" (p. 359), it "would obscure otherwise clear grammatical distinctions" (p. 361), and Bisang's pre-/post-adjective ordering test does not hold up (pp. 359-361)."
The LLM here has substantially misunderstood the analysis. My point here is that `phau` and `lo` are in fact classifiers. Other of Bisang's "class nouns" are syntactically prefixes (See section 3.2.4.1, p. 101).

6. "The stopword list files it as mensural, agreeing with none of them."
The word `cov` is polyfunctional, as my thesis states. Bisang's and Colvin's analyses are consonant with mine for selected functions of the word.

7. "yam usually appears with no noun to classify, and in frames like ib yam li it behaves more like an adverb"
This statement is problematic. `yam` and `hom` readily classify nouns. yam can also be used in a quantifier-classifier combination--`ib yam li` is an example of this.

D. "FUNCTION records Bisang's classifier / quantifier / class noun distinction, which White does not draw: it is one of the things Bisang adds."
This statement is misleading: I make the same distinction with different words, then assign based on syntactic behavior.

### dbnary-hmong.tsv

This one mixes words and phrases, and mixes orthographic standards, so we'll want to be careful here. 

A common tendency for diasporic Hmong is to consider something a word based on whether it can be expressed via a single word in English. There are many entries here in regard to this, so we'll want to handle their complex structure as such if we deem them sufficiently conventionalised, which remains to be determined.
For example (a small selection of many):
"ntaub pua chaw" is a noun + relative clause
"rab ncas" is a classifier + noun, as is "lub ntsiab"
"lub tshuab ntaus ntawv" is classifier + noun + relative clause, as is "phau ntawv hla teb chaws"
"roob ris teb" is noun + noun (the second noun modifies the first)
"qhov ntawd" is classifier + localizer
"los nag" is verb + noun
"Yexus Khetos lub Koom Txoos ntawm Tsoom Haiv Neeg Ntseeg hauv Hnub Nyoog Kawg" is a complex noun phrase ([noun phrase] + clf + noun + localizer + [noun phrase] + localizer + [noun phrase])

Some of the "definitions" are also incorrect:
`tus kws txhais lus` "interpreter" (clf + n + rel cl, "lit. [CL] expert (who) translates speech") is an interpreter of language, not music or art

Some of the definitions also drop detail:
`kwv` "younger brother (of a male)" is not just "brother" and certainly not "someone who is a peer, whether male or female".

### kindiv-proposals.tsv

" CHECK: Nathan -- confirm that Hmong `nus`, `muam`, `tij laug` and `kwv` really are indifferent to whether the father's sibling is a brother or a sister. If they are not, these collapse to the existing Fa;Br;* and Fa;Ss;* concepts and no proposal is needed.
No: these words only apply to one's siblings, or one's father's brother's children. Cousins on the father's mother's side use totally different terms.

"Why we doubt it. Hmong clans are patrilineal and exogamous, so a father's
 brother's children belong to ego's clan, but a father's sister's children
 belong to her husband's. The ethnographic expectation is ... that `nus`/`muam`/`tij laug`/`kwv` extend
 only to the father's BROTHER's children (Fa;Br;So, Fa;Br;Da)."
Indeed. Cf. White (2021: 287): "Members of the same clan and generation are considered ‘brothers’ in the Hmong family system."

To be sure: White (2021: 287-288) is designed only to give a quick overview of the most common terms, with an easy to read, accessible gloss; a rigorous ethnographic analysis of the system of kinship terms among the Hmong would be its own monograph, and was therefore out of scope for the thesis.
A lot more work will need to be done here to achieve complete coverage.


### Concepticon part-of-speech disagreements

"Seven unlinked senses have a gloss that is a Concepticon concept set, rejected only because the part of speech disagrees — the familiar verb/adjective and verb/noun pairings of a language with adjectival verbs:

form	gloss	ours	Concepticon	ILI
ziab	dry	v	a	i14155
foom	curse	n	v	i25957
tis	name	v	n	i69761
tu	clean	v	a	i2367
cub	steam	v	n	i116291
qhuas	praise	v	n	i71660
sau	harvest	v	n	i105478
Allowing a cross-part-of-speech link is a judgement call, not a bug fix, so it is listed rather than done. Seven is small, but each is certainly correct in meaning."

The parts of speech are 100% correct in ours:
ziab: "I hung my laundry to dry." (Cf. qhuav "be dry")
tis: "I named my child X."
tu: "I cleaned the house."
cub: "I steamed some vegetables."
qhuas: "I praised my child for doing a good job."
sau: "I harvested the crops."

Note on foom: it's also a verb "wish, bless, curse", as listed already in the ontology; the noun also means "blessing", which wasn't added yet to the ontology. The core meaning here is rather underspecified as regards good vs. bad.

### Second pass review items (24 Oct)

liab ‘red’, daj ‘yellow’ and ntsuab ‘green’ -- These colour terms don't appear in any of the review .tsv files. They are stative verbs in Hmong; for the abstract colour terms, these stative verbs modify a word meaning "color" (e.g., xim) in an unmarked relative clause.

cais
da dej -- this is a phrase, and the verb is `da`--`dej` is "water".
deb
nqi
ntse
zaub mov -- this is a "coordinate compound", and is in a grey area as regards whether they form a word together (literally "vegetable rice" meaning "food", and they can be separated by other content in fixed constructions).
ze


## Additional Sources

1. Heimbach, Ernest E. 1979. White Hmong-English dictionary. Rev. edn. (Southeast Asia Program Data Paper 75). Ithaca, NY: Cornell University Southeast Asia Program.
2. Mottin, Jean. 1978. Eléments de grammaire Hmong Blanc. Mumbai: Don Bosco.
