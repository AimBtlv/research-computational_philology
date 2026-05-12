**6.Sentence_5 - Find Root:** The sentence begins with _et Dominus induxit_ — this is the main clause. **ROOT = `induxit`** (The Lord brought wrath upon us).
Find Clause: Then comes a long chain of coordination via _et_ — all coordinated verbs depend on _induxit_ via `conj`:

|Level|Clause|Verb|Relationship|
|---|---|---|---|
|0|main|**induxit**|ROOT|
|0|conj 1|dispersit|conj → induxit|
|0|conj 2|aperuit|conj → induxit|
|0|conj 3|custodiuit|conj → induxit|
|0|conj 4|muniuit|conj → induxit|
|0|conj 5|consolatus est|conj → induxit|

**Characteristics of Sentence 5**:
**1. The chain `conj` throughout the entire period.** Patrick constructs the sentence as one long narrative—six verbs coordinate with one ROOT. This is characteristic of early medieval Latin: rhetorical stringing.
**2. The relative clause `qui respexit`** is an _embedded_ clause within the chain. _qui_ refers to _Dominum Deum meum_ and introduces a whole block of three clauses (`misertus est`, `custodiuit`, `muniuit`, `consolatus est`)—all of them `conj` within the relative clause.
**3. Double 'antequam'** — two parallel adverbial clauses with 'custodiuit': _antequam scirem eum_ and _antequam saperem uel distinguerem_. Within the second, there is also the coordination _saperem uel distinguerem_.
**4. The comparative clause 'ut pater filium'** is ellipsis: the verb is omitted (_consolatur/confortat_ is implied). In UD, this is ellipsis-based 'advcl', 'filium' becomes 'orphan'.
**5. 'esse uidetur'** is a copula construction: _uidetur_ = passive of _uideo_ meaning "to seem/appear". In UD, this 'cop' or 'aux' is debatable. **7. Features in sentences 6-7:**
1. What is the root verb: **Which verb is ROOT — _possum_ or _tacere_?** In UD, with the construction _possum + infinitivus_, the infinitive ive is `xcomp` with _possum_, and **ROOT = `possum`** is a finite verb, the head of the entire sentence. **ROOT = `possum
> The rule is **indirectly derived** from section **3.3.6 (Infinitive verbs, p. 11)**:
_"This includes both verbs that function as traditional direct objects (as in dabo ei edere de ligno vitae) as well as those that are **complete verbs like possum, volo, or incipio**."_
There, _possum, volo, and incipio_ are directly named—and the infinitive for them is treated as **OBJ**, that is, dependent on the finite verb. It follows that the finite verb (_possum_) is the head, and the infinitive (_tacere_) is its dependent, labeled OBJ.
2. **Double construction with negation.** _Unde autem tacere non possum, neque expedit quidem_ is a rhetorical pair: "I cannot remain silent, and it is not proper." Two verbs are coordinated by `neque...quidem`, with _possum_ = ROOT, _expedit_ = `conj`.
3. **_digno + infinitivus_** — the construction _praestare dignatus est_ is a periphrase: "he was honored to render" = "he deigned to render." In UD, _dignatus_ is the main verb, _praestare_ is `xcomp`
4. **Relative clause with _quam_.** _quam mihi Dominus praestare dignatus est_ — _quam_ refers to _beneficia et gratiam_ and is the `obj` within the relative clause with _praestare dignatus est_.
5. **_Unde_** is a relative adverb in the role of a discourse connector ("from where / that's why"). In UD, it is `advmod` or `discourse` with ROOT.
**Sentence Features**
**1. Multi-level nesting in a single period**
This is not a set of simple sentences—it is a **single rhetorical period** with 4 levels of nesting and 6 clauses. ROOT (`possum`) holds the entire tree from `Inde` to `caelo`. For comparison, classical Ciceronian Latin constructs periods in a similar way, but Patrick's structure is less symmetrical and more strung together.
**2. _Possum_ as ROOT with a semantically weaker meaning**
_Possum_ is a modal verb, lexically poorer than _tacere_. Intuitively, the "main word" is _tacere_ (what are we talking about), but ROOT = _possum_ because only it is finite. This is a typical trap for modal constructions in UD.
**3. Gap: _quam mihi dignatus [est praestare]_**
The manuscript omits verbs—we reconstruct _praestare dignatus est_ from context. This is a **textual problem** that affects the annotation: we need to decide what `xcomp` is for _dignatus_ and where _quam_ and _mihi_ get their arguments from. In CoNLL-U, such gaps are usually marked with `reparandum` or simply reconstructed without a special label.
**4. _Est_ in two different syntactic roles**
In one period, _est_ occurs twice—and each time, it has a different role:

|Place|Role|Why|
|---|---|---|
|_haec **est** retributio_|`cop`|there is a nominal predicate → copula|
|_quae **est** sub omni caelo_|`root` rel. clauses|locative/existential _esse_ without a predicate|

This is the key difference: the copular _est_ is never the ROOT, while the existential is always the ROOT of its clause.
**5. The _Quia_-clause as 'advcl' with ROOT**
_Quia haec est retributio nostra_ is not an independent clause, but a causative clause with _possum_. Within it, the predicate _retributio_ becomes **local ROOT**, but in the tree of the entire period, it is 'advcl'. It is this point that has given rise to the "double standard"—it depends on whether we take the fragment in isolation or in context.
those.
**6. _Ut_ ​​+ infinitive instead of subjunctive**
_Ut exaltare et confiteri_ — classically, _ut_ governs the subjunctive (_ut exaltemus_). Patrick uses infinitives. This is a **Late Latin feature**, characteristic of Biblical Latin and the Irish-Latin tradition of the 5th century. In UD, it is annotated as `csubj` with _retributio_, `mark(exaltare, ut)`.
**7. _Csubj_ with a predicative**
_Ut exaltare et confiteri mirabilia_ is a **clausal subject** with _retributio_. Structure: "our retribution is [to] exalt." In UD, it's `csubj(retributio, exaltare)`—a rare case where `csubj` is attached to a predicative noun rather than a verb.
**8. Double _quam_: Morphology vs. Syntax**
The pronoun _quam_ agrees in gender and number with _gratiam_ (Acc. Sg. Fem), but semantically refers to the entire pair _beneficia et gratiam_. In Basic UD, it's `obj(praestare, quam)`, with antecedent = `beneficia` (the head of the NP). In Enhanced UD, you can add `ref(gratiam, quam)` for completeness.
**9. Double Coordination of Infinitives**
_Exaltare **et** confiteri_—two infinitives coordinated. Both govern the same object _mirabilia eius_. In UD, the object is attached to the first conjunct (_exaltare_), and _confiteri_ "inherits" it via `conj`. This is the standard **shared dependents** convention in basic UD.
**10. Style: Patrick vs. Classical Latin**
The combination of all these features—_ut_ + Inf, stringing coordination, lacunae—reflects Patrick's **rustica latinitas**, which he himself acknowledges at the beginning of the Confessio (_rusticissimus_). His syntax is closer to colloquial late antique Latin and biblical translation than to Cicero or Caesar.

---
**10. Features of Sentence 9**
**1. Find ROOT**:**Two Readings - Two Different Meanings** -Option A: ROOT = `est` (existential) There is no [other God] _Est_ carries the entire statement—the fact of existence/non-existence. _Deus_ = the subject of existence. The negation _non_ hits _est_—"does not exist." This accurately conveys Patrick's meaning.
**Option B: ROOT = `Deus` (copulatory)** Another God is not [...] A predicative is needed here—"another God is not _true_" or "is not _God_." But the text lacks a predicative. This construction is syntactically incomplete. Existential _est_ = ROOT—not a copula.** This is a direct application of the rule from the Latin UD guidelines: purely existential clauses treat _sum_ as the clause head. [Universal Dependencies](https://universaldependencies.org/la/) This differs from all previous analyses where _est_ was `cop`.

**2. Triple temporal coordination with ellipsis.**
_Nec umquam fuit / nec ante / nec erit post haec_ are three temporal conjuncts. The middle (_nec ante_) is an ellipsis: the verb _est/fuit_ is omitted. In UD, this is `orphan` or the elevation of _ante_ to the head of the conjunct.
**3. Aposition as theological explication.**
_Deum Patrem ingenitum_ is not just a noun phrase, but a **theological unfolding**: "God the Father unbegotten." Three words describe one referent through aposition + attributes. In UD: `appos(Deus, Patrem)`, _ingenitum_ = `amod`.
**4. Double relative clause with _Patrem_.**
_a quo est omne principium_ and _omnia tenentem_ are two clauses, both modify _Patrem_:
- _a quo est omne principium_ → `acl:relcl(Patrem, est)` — from Whom all things begin
- _omnia tenentem_ → `acl(Patrem, tenentem)` — upholding all things (participle, not `acl:relcl`)
**5. _Ut didicimus_ as an epistemic marker.**
_Ut didicimus_ — "how we learned/came to know." This is a **discursive clause** expressing the source of knowledge. In UD, it's 'advcl' at ROOT, but semantically closer to 'discourse'. Patrick constantly uses such markers ('ut didicimus', 'ut credimus')—this is a feature of his apologetic rhetoric.
**6. _Nec ... nec ... nec_** is a triple negation as a rhetorical figure.
The classic **tricolon** structure with temporal progression: past (_fuit_) → present (_est_ elliptically) → future (_erit_). Each conjunct is introduced by 'cc' with the lemma _nec_.

---
**10. Features of Sentence 9**
**1. The longest period of Confessio**—132 tokens, 4 levels of nesting, 8 conjuncts at ROOT. This is an expanded Trinitarian Confession of Faith.

**2. Accusativus cum Infinitivo pri testamur.** _Quem cum Patre semper fuisse testamur_ is a classic indirect discourse. _Fuisse_ = `ccomp`, _quem_ = `nsubj` of the infinitive clause. Antecedent _quem_ = _filium_.

**3. Stringing participles without a verb.** _Genitum... factum... receptum_ — three participles depend on _filium_ through `acl`, describing its properties sequentially: born → became human → received into heaven. This is characteristic of early Christian Latin.

**4. Ablativus absolutus: _morte deuicta_.** _Morte deuicta in caelis ad Patrem receptum_ — _deuicta_ = `advcl:abs` with _receptum_. Death is the subject of the participle, and the phrase itself = the adverbial clause "when death was conquered."

**5. _Quia_ as "what" instead of cause.** _Omnis lingua confiteatur ei quia Dominus et Deus est Jesus Christus_ — here _quia_ introduces the **content** of the confession (= classical _quod_), not the cause. This is Late Latin