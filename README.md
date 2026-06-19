## reasearch-Computational Philology

### A Computational Syntactic Analysis: Testing Style Hypotheses On The Confessio Patricii Through Dependency Syntax

**A Case Study on C. Mohrmann and D. Howlett's Theories of Patrick's Latin**

*****


##### About Project: 
This project applies computational, dependency-based syntactic analysis to Confessio Patricii, the fifth-century autobiographical text attributed to Saint Patrick. The goal is to bring quantitative evidence to a long-standing scholarly disagreement about the nature of Patrick's Latin style. The project uses a CoNLL-U annotation of the text. The annotation was produced with UDPipe and manually corrected in Arborator Grew. Two opposing characterizations of Patrick's prose are turned into measurable syntactic indicators. The first is Christine Mohrmann's claim that the prose is simple and paratactic. The second is David Howlett's claim that it conceals a deliberate rhetorical architecture of parallelism and chiasmus. Both indicators follow methods presented in the Computational Philology course. The chiasmus indicator is also adapted from recent computational work on chiasmus detection. The analysis finds partial, direction-consistent support for Mohrmann's hypothesis. It finds weak and inconsistent support for Howlett's hypothesis. The project also shows the methodological limits of testing literary-critical claims through dependency-tree statistics alone.


***
##### Research Questions and Hypotheses:
**RQ:** Can quantitative dependency tree syntactic analysis, applied to Confessio Patricii, provide a testable and replicable basis for the long-standing academic debate about the style of Patrick's Latin? This debate is built around two opposing positions, Mohrmann's thesis of a simple, colloquial, paratactic language, and Howlett's thesis of hidden rhetorical complexity, including parallelism and chiasmus. If such a basis can be provided, the further question is to what extent computational methods confirm, complicate, or refute each of these qualitative interpretations.

**H1:** The first hypothesis follows directly from Mohrmann's thesis, and it asks to what extent the syntactic structure of Confessio Patricii supports her view once that structure is measured directly. The structure is measured through the ratio of parataxis to hypotaxis, based on the UD labels conj and cc for coordination, against acl, advcl, ccomp, and csubj for subordination. If Mohrmann is right that Patrick's Latin is a simple, additive, colloquial register (rustica latinitas) rather than classical periodic prose with deep subordination, then this ratio should shift systematically toward coordination across the text, so that coordinating relations clearly outweigh subordinating ones in most or all sentences.

**H2:** The second hypothesis follows from Howlett's thesis instead, and it takes a more cautious form, since his claim concerns meaning and lexical repetition rather than grammar alone. The question is whether statistically significant traces of hidden parallelism or chiasmus, as Howlett describes them in Patrick's prose, can be detected through the symmetry of part-of-speech sequences (UPOS) within the sentences of Confessio. If such a hidden biblical-style rhetorical structure is present, as Howlett argues, then the symmetry of the UPOS sequence around the midpoint of a sentence should significantly exceed the level of symmetry expected from a random arrangement of the same grammatical categories, and this effect should appear consistently across the text rather than only in a few short sentences, where a chance match is more likely to occur on its own.
 
***
##### Repository Structure:
- intro/
- datasets/
- notebooks/
- scripts/
- images/
- bibliography/
- documentation/
- outputs/
***
##### Methodology:
**Method of measurement 1**    
The method was built in analogy with a recent 2025 paper that addresses exactly this task on biblical texts. The idea is to replace Howlett's semantic chiasmus with a rough syntactic analogue. Each sentence is split into a first half and a second half by part of speech, that is, by UPOS tags such as VERB, NOUN, and ADJ. Two types of matches are then checked. The first checks whether the first half matches the second half in the same order, and this is the test for parallelism. The second checks whether the first half matches the second half in reverse, mirrored order, and this is the test for chiasmus. Whichever version produces the higher match is taken as the sentence's mirror_score.
What each column in the table means. The column sent_id is the sentence number in the text. The column n_tokens is the length of the sentence in words. The column mirror_score is the main number in this table. It is the share of matching positions between the two halves of the sentence, ranging from 0, no matches at all, to 1, a complete match. The higher the number, the more symmetrical the sentence's grammatical structure. The column pattern_type shows which type of symmetry turned out to be stronger. A value of parallelism-like means the direct order wins, and a value of chiasmus-like means the mirrored order wins.

**Method of measurement 2**
The hypothesis was tested through the parataxis/hypotaxis ratio, that is, the relationship between parataxis and hypotaxis, measured through CoNLL-U syntactic labels. In this work, the method was applied in an expanded form. Subordination was counted using four labels, acl, advcl, ccomp, and csubj, while coordination was counted using two labels, conj and cc. Each of the two measures was calculated as a share of the sentence length, that is, how many words out of a hundred carry that syntactic role. If Mohrmann is right, the share of coordination should be clearly higher than the share of subordination across the whole text.
The results table has several columns, and each one shows a different part of the picture. The column n_subordinate_rel is simply the count of subordinating relations in a sentence, and the column n_coordinate_rel is the count of coordinating relations. These two columns give raw numbers, but raw numbers are hard to compare across sentences of different lengths, so two more columns sit next to them. The column subordination_ratio is the share of subordination, that is, the count of subordinating relations divided by the sentence length. The column coordination_ratio is the same calculation for coordination.


***
##### Data:
Sources: https://www.confessio.ie/etexts/confessio_italian#
Format: .txt
Language: Latin
Period: 5 c.ad 
***
##### Tools:
Python 3.x
Arborator Grew. "Arborator Grew." Accessed June 18, 2026. https://arborator.grew.fr.
Guillaume, Bruno, and Marie Candito.    
"Arborator-Grew: A Toolbox for Multi-layer Annotated Corpora." Accessed June 18, 2026. https://arborator.grew.fr.

Universal Dependencies. "Latin." Accessed June 18, 2026. https://universaldependencies.org/la/.

UDPipe. "UDPipe Online Processing Service." Accessed June 18, 2026. https://lindat.mff.cuni.cz/services/udpipe.

Universal Dependencies. "Latin ITTB Treebank." Accessed June 18, 2026. https://universaldependencies.org/treebanks/la_ittb/index.html.

***
##### Author:
Aim Batalova — Ca'Foscari University — email: aim.b14.04git@gmail.com
***
##### License:

