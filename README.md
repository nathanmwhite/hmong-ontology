# hmong-ontology
A semantic ontology resource for the Hmong language, inspired by WordNet (Fellbaum, 1998).

This resource is intended for data science and natural language processing purposes, such as computational modeling of semantics or cleaning of raw data for deep learning.

This repository currently contains the following files:
1. hmong_ontology.xml : The xml file containing the lexemes (nouns and verbs) and their semantic categories.
2. stopwords_base.txt : A text file containing Hmong stopwords, excluding classifiers and verbal bound roots/affixes.
3. stopwords_classifiers.txt : A text file containing Hmong classifiers.
4. stopwords_verbal_adjuncts.txt : A text file containing Hmong verbal adjuncts, such as bound roots and affixes.

TODO:
1. Create Python code to load the Hmong ontology as a WordNet-style library.
2. Write documentation.
3. Revisit distinction between object and artifact categories: it does not seem to have significance in Hmong.
