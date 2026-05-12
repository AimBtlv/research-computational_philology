**Workflow 2**
____  
1.**Text Preparation**  
Before running UDPipe, both texts must be cleaned and broken into sentences manually, as the sentence markup in the original text does not match.  
**For Latin:**
Remove extra spaces, standardize punctuation. 

**Tool:**  
Text editor  
Python script  
**output:** txt

---
2.**Set UdiPipe**  
link: https://lindat.mff.cuni.cz/services/udpipe  
Model:   
For Latin - `latin-proiel`  
**output:** CoNll-U

---
3.**Set Arborator-Grew**  
link: https://arborator.grew.fr/  
Documentations: https://arborator.github.io/arborator-documentation/#/ 


---
4.**Comparisons**
>note: Align sentences manually using Arborator-Grew

**Unit of Comparison**  
For syntactic comparison, we compare sentence to sentence.   
**Markup System.** UD (for Arborator).  
**Identifiers.** In CoNLL-U, each sentence requires an 'id'.  
**Markup System.** UD (for Arborator)
**Identifiers.** In CoNLL-U, each sentence requires an 'id'.   
**Compare DEPREL(1) For Each Pair Of Sentences**  
Find differences in syntactic roles for semantically equivalent words. 

---
**Annotating Fragment A**
For each sentence, in order:   
1.Find ROOT — the finite verb of the main clause.  
2.Determine clause levels.    
3.Annotate tokens in Arborator: UPOS → FEATS → HEAD → DEPREL → subrel.   
4.Export CoNLL-U
> `MISC` in CoNLL-U - fix disputed passages directly in the process. 

---
**Annotating Fragment B**
For each sentence, in order:  
1.Find ROOT — the finite verb of the main clause.  
2.Determine clause levels.  
3.Annotate tokens in Arborator: UPOS → FEATS → HEAD → DEPREL → subrel.  
4.Export CoNLL-U

> Make notes in a separate document with controversial cases and decisions made.

**output:** CoNll-U  
**output** Notes 

---
5.**Analyses**  
Make analysis:  
Syntactic features of Latin version of witness 1.  
Syntactic features of English version of witness 2.

After labeling both fragments:   
1.How deep are the trees?   
Do Parataxis (`conj` chains) or hypotaxis (`advcl`, `acl:relcl`) predominate?   
Where is the ROOT—closer to the beginning or to the end?   
2. Quantitative analysis?  
3. Real patterns?

**output:** Report (most interesting features)  
**output:** CoNLL-U
**output:** Table

