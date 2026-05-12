**Workflow**
____  
1.**Text Preparation**
Before running UDPipe, the texts must be cleaned and broken into sentences manually, as the sentence markup in the original text does not match.  
**For Latin:**
Remove extra spaces, standardize punctuation. Check sentence boundaries against English text.  
**For English:**
Break the text into sentences at Latin text boundaries. Remove extra spaces.  
**Tool:**  
Text editor  
Python script  
**output:** txt

---
2.**Set UdiPipe**  
link: https://lindat.mff.cuni.cz/services/udpipe  
Model:   
For Latin - `latin-proiel`  
For English - `english-ewt`
**output:** CoNll-U

---
3.**Set Arborator-Grew**  
link: https://arborator.grew.fr/  
Documentations: https://arborator.github.io/arborator-documentation/#/ 


---
4.**Comparisons and Corrections**
>note: Align sentences manually using Arborator-Grew

**Compare DEPREL(1) For Each Pair Of Sentences**  
Find differences in syntactic roles for semantically equivalent words.  
**For Example:**  
**Latin:** _Ego Patricius peccator rusticissimus..._   
**English:** _My name is Patrick..._

**Make a table of sentence correspondence:**
Id|Latin|DEPREL|English |DEPREL|
|:---|:---:|:---:|:---:|---:|
|1|_Ego_|`nsubj`|_I_|`nsubj`|
|2|_Patricius_|`appos`/`nsubj`|_Patrick_|`attr`/`nsubj`|
|3|_peccator_|`appos`|_sinner_|`nsubj`|

**output:** CoNll-U  
**output:** Table 

---
5.**Analyses**  
Make analysis:  
Syntactic features of Latin version of text.  
Syntactic features of English version of text.

**output:** Report (most interesting features)  
**output:** CoNLL-U

----
**Prospective analysis:**  
Compare Syntactic features of diferent versions (witnesses) of Latin text.

