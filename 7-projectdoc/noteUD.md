### noteUD

Complete Tagset (UD)

## Core Relations

| Label | Name | Essence |
|-------|---------|------|
| **root** | Root | Root of the tree, usually the main verb |
| **nsubj** | Nominal subject | Noun subject |
| **csubj** | Clausal subject | Clause subject |
| **obj** | Object | Direct object |
| **iobj** | Indirect object | Indirect object (dative) |
| **obl** | Oblique | Indirect argument or adjunct with a preposition/case |
| **xcomp** | Open complement | Complement without its subject (infinitive, PNOM) |
| **ccomp** | Clausal complement | Adverbial clause with its own subject |
| **advcl** | Adverbial clause | Adverbial clause |
| **advmod** | Adverbial modifier | Adverb modifier |
| **amod** | Adjectival modifier | Adjective modifier |
| **nmod** | Nominal modifier | Noun modifier (genitive, etc.) |
| **nummod** | Numeral modifier | Numeral modifier |
| **acl** | Adnominal clause | Participial/relative clause with a noun |
| **appos** | Apposition | Application |
| **det** | Determiner | Determiner (article, demonstrative, etc.) |
| **case** | Case marker | Preposition as a case marker |
| **mark** | Marker | Subordinating conjunction |
| **cc** | Coordinating conjunction | Coordinating conjunction |
| **conj** | Conjunct | Second and subsequent members of a clause |
| **cop** | Copula | Linking verb |
| **aux** | Auxiliary | Auxiliary verb |
| **expl** | Expletive | Formal, semantically empty element |
| **vocative** | Vocative | Address |
| **discourse** | Discourse element | Discourse particle, interjection |
| **dislocated** | Dislocated element | Displaced element (topicalization) |
| **parataxis** | Parataxis | Paratactically attached clause |
| **orphan** | Orphan | Orphaned element in ellipsis |
| **goeswith** | Goes with | Part of a broken word |
| **flat** | Flat | Proper names, multi-word expressions |
| **fixed** | Fixed | Frozen multi-word expressions |
| **compound** | Compound | Compound word |
| **punct** | Punctuation | Punctuation |
| **list** | List | List elements without syntactic connection |
| **reparandum** | Reparandum | Self-correction in speech |
| **dep** | Unspecified dependency | Unspecified dependency (extreme case) |

## Subrel (Subrelations, Qualifications)

| Subrel | When used |
|--------|---------------------|
| **agent** | Agent in the passive construction (obl:agent) |
| **arg** | Required indirect argument (obl:arg) |
| **pass** | Passive voice (aux:pass, nsubj:pass) |
| **relcl** | Relative clause (acl:relcl) |
| **tmod** | Temporal adverb (obl:tmod) |
| **cmp** | Comparison (advcl:cmp, mark:cmp) |
| **neg** | Negation (advmod:neg) |
| **poss** | Possessiveness (nmod:poss) |
| **lvc** | Light verb construction |
| **gov / numgov** | Control in numeric constructions |
| **emph** | Emphasis (advmod:emph) |
| **mod** | General modification |
| **name** | Part of a proper name |
| **prt** | Particle |
| **outer** | External topic |
| **svc** | Serial Verb Construction |

--

# Stage 1: Find the Sentence Skeleton

*What we do:* define **root**, then **nsubj/csubj**, **obj**, **iobj**, **xcomp**, **ccomp**.

This is the foundation. The entire tree is built around the root, and the direction of dependence here is fundamentally different than in Perseus: the head is almost always a substantive word, not a function word.

**root**  hint:
Look for the finite form of the main verb. If it's an analytic form (participle + *esse*), root becomes a participle, and *esse* becomes **cop** or **aux**. If the sentence begins with a conjunction, the conjunction doesn't become the head: it depends on the verb through **mark**, and the verb is still the root.

**nsubj** hint:
The subject of a nominative sentence depends directly on the verb. The test is the same as in Perseus: does this word become the subject of the passive? If subj is expressed by a complete clause (infinitive or subordinate clause), use **csubj**, not nsubj.

**obj**  hint:
Direct object in the accusative. The obligatory test is the same: remove the word, does the sentence break? Then obj. In UD, obj is reserved specifically for direct objects without a preposition; anything with a preposition or in the indirect case without a preposition is most likely **obl**.

**iobj**  hint:
Indirect object, usually dative, with trivalent verbs (*dare, dicere*). It is used less often than you might think: many datives in UD are marked as obl unless they are an explicit "second object" of the verb of transmission.

**xcomp / ccomp** hint:
If the dependent clause or infinitive **doesn't have its own subject** and its subject is the same as the subject of the main verb **xcomp** (this covers many cases of PNOM and accusative infinitivo). If the clause has its own subject **ccomp**.

---

# Stage 2: Find Bridge Function Words

*What we do:* identify **case**, **mark**, **aux**, **cop**, **det**.

The main difference from Perseus: here the function word **depends** on the substantive word, and not vice versa. This changes
The direction of the arrows is different from what you're used to.

**case**  hint:
Did you find a preposition? In UD, it depends on the noun it introduces, not the other way around. *cum Germanis*: the head is *Germanis*, *cum* depends on it through case. The role of the phrase itself (obl, nmod, etc.) is determined by the noun, not the preposition.

**mark**  hint:
The subordinating conjunction (*quod, ut, ne, cum*) depends on the verb of the subordinate clause. The verb of the clause remains the head and itself takes on the role of advcl/ccomp in relation to the main clause. This is a mirror image of Perseus, where it was the other way around.

**aux / cop**  hint:
The auxiliary verb (*est* in the passive perfect) is **aux**, dependent on the participle. The linking verb (*esse, videor, fio* in the role of "to be someone") is **cop**, depending on the noun phrase, which in this case often becomes **root** or **xcomp**.

**det**  hint:
Rare in classical Latin, but found with demonstrative/possessive pronouns as determiners. If a pronoun explicitly defines the reference of a noun rather than describes it, use det, not amod.

---

# Step 3: Mark Punctuation

*What we do:* Anything that is a punctuation mark receives **punct**.

Here, UD is much simpler than Perseus. No division into AuxX/AuxG/AuxK.

**punct**  hint:
Any comma, period, quotation mark, parentheses, or semicolon receives a punct value and depends on the nearest syntactically significant word (often the head of its clause or the root of a final sign). The comma has no special status as a "coordination head" in UD.

---

# Step 4: Mark Up Noun Modifiers

*What we do:* define **amod**, **nmod**, **nummod**, **appos**, **acl**, **compound**, **flat**.

**amod** hint:
An adjective or participle that **attributively** modifies a noun. A direct analog of ATR for adjectives. The test is the same: remove the word, the noun becomes less specific, but the grammaticality is preserved.

**nmod** hint:
A noun modifying another noun, usually in the genitive. *amor laudis* → *laudis* is the nmod of *amor*. If the genitive is possessive, you can specify it using subrel **nmod:poss**.

**nummod**  hint:
A numeral attached to a noun. *septem tubas* → *septem* is the nummod of *tubas*.

**acl** hint:
A participial phrase or relative clause **with antecedent** that limits the noun's reference. A direct analog of ATR for participles and relative clauses. If the clause is introduced by a relative pronoun, use the **acl:relcl** specification.

**appos**  hint:
Appendix. Unlike Perseus, a comma-head is not needed here: the second element of the appositive simply depends directly on the first through appos. The commas between them receive a separate punct.

**compound / flat**  hint:
Compound words and multi-word proper names. *Index Thomisticus* as a single name: the second element depends on the first through flat (or flat:name).

---

# Step 5: Mark Adverbial Clauses and Subordinate Clauses

*What we do:* define **advmod**, **advcl**, **obl** (adjunct use).

**advmod** hint:
An adverb modifying a verb, adjective, or another adverb. Direct analog of ADV for adverbs. *confestim* with *mittuntur* → advmod.

**advcl** hint:
A subordinate adverbial clause (of cause, condition, time), introduced by mark. The clause's verb depends on the main verb through advcl, and the conjunction (mark) depends on this clause's verb.

**obl (adjunct)** hint:
A noun in the oblique case or with a preposition that functions as an adverbial clause rather than an obligatory argument. Optionality test: can it be removed without losing the meaning of the verb? Then **obl**, without specifying **arg**. If the argument is obligatory, use **obl:arg**.

---

# Step 6: Mark Coordination

*What we do:* define **cc** and **conj**.

This is perhaps the most unusual place after Perseus, because the architecture is completely different.

**conj**  hint:
In a UD, the **first conjunct** becomes the head of the coordination. All subsequent members of the list depend on the first through conj, not on the final conjunction or comma.

> *lingua, institutis, legibus* → *institutis* and *legibus* depend on *lingua* through conj. *lingua* itself receives the role that the entire group would play (e.g., obl).

**cc** —hint:
The coordinating conjunction (*et, atque, -que*) depends on the **following conjunct**, not on the first conjunct or on the head of the entire group. It receives the cc label.

**preconj** hint:
If a conjunction comes **before the first** member of the coordination (like *et... et...*, "and... and..."), the first such conjunction receives subrel **cc:preconj** and depends on the first conjunct.

---

# Step 7: Markup Special Constructions

*What we do:* define **vocative**, **discourse**, **expl**, **parataxis**, **orphan**, **dislocated**.

**vocative** hint:
The address depends on the verb through the vocative. Direct correspondence to ExD for addresses in Perseus.

**discourse** hint:
Discursive particles and interjections (*ecce, vero* as exclamations) depend on
A verb through discourse. This is a rough analogue of AuxY, although UD treats it as a discourse element, not a modal one.

**expl** hint:
A formal, semantically empty element in reflexive or impersonal constructions. The closest analogue to AuxR from Perseus: the reflexive *se*, which does not carry an independent objective role, can receive **expl:pass** when used passivistically.

**parataxis** hint:
A clause added without a conjunction, but logically dependent (e.g., direct speech without *quod*). Dependent on the verb that introduces it, through parataxis.

**orphan** hint:
A direct analogue of ExD in Perseus' ellipsis, but without complex compound tags. An orphaned word simply receives the "orphan" tag and depends on the node that occupies the place of the missing head.

> *unam incolunt Belgae, aliam Aquitani* → *Aquitani* gets **nsubj**, and *aliam* gets **orphan**; both depend on *Belgae* (or on the conj structure), preserving parallelism without special ExD indices.

**dislocated** hint:
An element placed at the beginning or end of a sentence for emphasis, syntactically not integrated into the normal clause structure.

---

# Step 8: Clarify with Subrelations

*What we do:* Add subrelations where it clarifies the meaning of the main marker.

**obl:agent** hint:
Agent in a passive construction (*ab Cicerone*). A direct analogue of OBJ-passive-agent from Perseus, but now it is explicitly marked with subrelations instead of being merged with regular OBJ. **aux:pass / nsubj:pass** — hint:
Passive voice markers. Used to clearly indicate that an auxiliary verb or subject is part of a passive construction.

**acl:relcl** hint:
Relative clause with an antecedent. It clarifies the regular acl clause, clearly indicating the relative nature of the clause.

**advmod:neg** hint:
Negative particle (*non*). A direct analog of AuxZ for negation: it depends on the word that negates it and is clearly marked as negation.

**advmod:emph**  hint:
Intensifying particle (*etiam, item*). A direct analog of other instances of AuxZ.

**obl:tmod** hint:
Temporal adverb expressed by a noun without a preposition (ablative of time).

**advcl:cmp / mark:cmp**hint:
Comparative constructions with *quam*. Analogous to AuxC in comparative constructions from Perseus section 4.9.

---

# Stage 9: Verification

*What we do:* Verify the tree against the control criteria.

1. **The direction of the arrows is verified.** For prepositions and conjunctions, the head is a substantive word, not a function word. This is contrary to the intuition developed in Perseus.

2. **Coordination is built from the first conjunct.** Not from the final conjunction or comma.

3. **obj is used only for direct objects without a preposition.** All other indirect arguments and adjuncts are obl, with arg specified if necessary.

4. **Subrels are added where informative**, but are not used excessively: a base label without a subrel is acceptable if the refinement is not critical to the analysis.

---

# Quick Cheat Sheet: Perseus → UD Test Correspondence

| Perseus Test | UD Analogue |
|------------------|------------|
| Remove the word is it broken? | obj vs obl (same distinction: argument vs adjunct) |
| Does the participle limit reference? | acl (instead of ATR) |
| Does the participle refine the verb's modifier? | advcl or just advmod (instead of ADV) |
| Does the word simultaneously agree with the noun and refine the verb? | often xcomp or advcl:cmp (ATV/AtvV have no direct equivalent, determined by context) |
| Does the particle refer to the entire sentence? | discourse (instead of AuxY) |
| Does the particle refer to a single word? | advmod:neg / advmod:emph (instead of AuxZ) |
| Passive construction without an agent? | expl:pass (instead of AuxR) |

---

# Main Change in Thinking

When moving from Perseus to UD, keep one thing in mind: **function words no longer head groups**. In Perseus, the preposition is "more important" than the noun, and the conjunction is "more important" than the verb of the clause. In UD, it's the other way around: the content word is always the head, and the function word simply marks its grammatical role with case, mark, or aux.

If, while marking, you catch yourself thinking, "The preposition should be the head," this is a sign that your thinking has slipped into Perseus logic. Flip the arrow.

---

**Sources:**
- Universal Dependencies: https://universaldependencies.org
- UD Relations Inventory: https://universaldependencies.org/u/dep/index.html
- UD Latin Corpus (Perseus, ITTB, LLCT, PROIEL): https://universaldependencies.org/la/index.html
- Arborator-Grew: https://arborator.grew.fr
- Bamman, Passarotti, Crane, Raynaud. *Guidelines for the Syntactic Annotation of Latin Treebanks* (v. 1.3), 2007 (for comparison)