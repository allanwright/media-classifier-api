'''Defines a classifier builder.

'''

import json
import pickle

from mccore.entity_recognizer import EntityRecognizer
from mccore import ner

from helpers.builder import Builder

class EntityRecognizerBuilder(Builder):
    '''Defines an entity recognizer builder.

    '''

    def build(self, *args):
        '''Builds the object.

        Args:
            args: The args required to build the object.
        '''
        nlp, _ = ner.get_model()
        nlp_bytes = pickle.loads(args[0])
        nlp.from_bytes(nlp_bytes)
        return EntityRecognizer(nlp)
