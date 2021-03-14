'''Defines a classifier builder.

'''

import json
import pickle

from mccore.classifier import Classifier

from helpers.builder import Builder

class ClassifierBuilder(Builder):
    '''Defines a classifier builder.

    '''

    def build(self, *args):
        '''Builds the object.

        Args:
            args: The args required to build the object.
        '''
        return Classifier(
            pickle.loads(args[0]),
            pickle.loads(args[1]),
            json.loads(args[2]))
