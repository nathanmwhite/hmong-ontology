# hmong-ontology
A semantic ontology resource for the Hmong language, inspired by WordNet (Fellbaum, 1998).

This resource is intended for data science and natural language processing purposes, such as computational modeling of semantics or cleaning of raw data for deep learning.

This repository currently contains the following files:
1. hmong_ontology.xml : The xml file containing the lexemes (nouns and verbs) and their semantic categories.
2. stopwords_base.txt : A text file containing Hmong stopwords, excluding classifiers and verbal bound roots/affixes.
3. stopwords_classifiers.txt : A text file containing Hmong classifiers.
4. stopwords_verbal_adjuncts.txt : A text file containing Hmong verbal adjuncts, such as bound roots and affixes.
5. hmongnet.py : A Python code file providing WordNet-style access to the ontology.

TODO:
1. Create Python code to load the Hmong ontology as a WordNet-style library. Begun as hmongnet.py.
2. Expand vocabulary based on additional forms attested in speaker community using an automated approach.
3. Label forms as White Hmong where distinct and add Green Mong forms.
4. Implement stopword files.
5. Write documentation.

To consider:
1. Revisit distinction between object and artifact categories: it does not seem to have significance in Hmong.
2. Provide an additional xml file containing roots with additional bound root possibilities.
