# Hmong ontology
# Original code Copyright © 2022 Nathan M. White

# Copyright notice
__copyright__ = "Copyright © 2022 Nathan M. White"

# author
__author__ = "Nathan M. White"
__author_email__ = "nathan.white1@jcu.edu.au"

import xml.etree.ElementTree as ET


class Ontology:
    def __init__(self):
        self._load_ontology_data()

    def _load_ontology_data():
        self.tree = ET.parse('hmong_ontology.xml')
        word_set_idx = 3
        self.word_set = self.tree.getroot)[word_set_idx]

    def _get_lemma(word):
        word = word.replace(' ', '_')
        for lemma in word_set.iter('lemma'):
            form = lemma[0]
            if form.text == word:
                return lemma
        return None

    def lexname(word):
        lemma = _get_lemma(word)
        if lemma == None:
            return []
        else:
            pass
