<<<<<<< HEAD
=======


## Project Idea:
**"Syntactic Variation Across Witnesses of the Confessio"**.    
Confessio сохранилась в двух главных редакциях рукопись Book of Armagh (807 г.) и более поздние версии. Это тема из лекции 6 (stemmatology).   
Можно аннотировать оба варианта и сравнить не только лексические варианты, но и синтаксические?
Изменился ли порядок слов в копиях?     
Появились ли новые conj цепочки или они упростились?

Aims: 
- Цель не автоматическая истина а лучшая филологическая интерпритация через явные проверяемые предстовления
- One of the mos Philological criticall discussion: Синтактические деревья могут отражать современную аннотационную схему, а не историческую грамматику. 

>>>>>>> main
**Algorithm:**  
1.**Clean of texts (Latin and English)**  
Manually clean and align sentences.  
**output:** txt

------
2.**UdiPipe analyse**  
Run both texts through UDPipe.  
**output:** CoNll-U

-------
3.**Arborator-Grew**  
Run both texts through Arborator-Grew for visual verification.
Compare the results of the two texts.  
**output:** tree 

-------
4.**Analyse**  
Perform syntactic analysis of texts in English and Latin.  
Save the corrected version in CoNLL-U format.  
**output:** Report (most interesting features).    
**output:** CoNLL-U
<<<<<<< HEAD
=======

-------
|Лекция                 |Метод                                    |Применение в проекте                                           |
|-----------------------|-----------------------------------------|---------------------------------------------------------------|
|7 Linguistic Analysis|UDPipe, CoNLL-U, deprel                  |Уже сделано: файл `.conllu` готов                              |
|8 Stylometry         |Количественный анализ синтаксических черт|Метрики из деревьев                                            |
|9 Stylistic Analysis |CoNLL-U queries, `deprel` профили        |Запросы типа `deprel=conj` по всему тексту                     |
|5 Alignment          |Сравнение структур через текст           |Сравнение Confessio vs Epistola (оба текста Патрика)           |
|6 Stemmatology       |Textual witnesses, variants              |Confessio передаётся в двух редакциях (рукописи Book of Armagh)|
|`guidelines_latin.pdf` |PDT-style: PRED, SBJ, OBJ, ATV           |Как точка отсчёта — стандарт аннотации                         |
>>>>>>> main
