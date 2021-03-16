'''Defines a graphene context builder.

'''

import json
import pickle

from mccore.classifier import Classifier
from mccore.entity_recognizer import EntityRecognizer
from mccore import ner

from gql.helpers.builder import Builder

class ContextBuilder(Builder):
    '''Defines a graphene context builder.

    '''

    def build(self, *args):
        '''Builds the object.

        Args:
            args: The args required to build the object.
        '''
        classifier = Classifier(
            pickle.loads(args[1]),
            pickle.loads(args[0]),
            json.loads(args[2]))

        label_dict = json.loads(args[2])
        label_list = [{ 'id': k, 'name': v } for (k, v) in label_dict.items()]
        label_json = json.dumps(label_list)

        nlp, _ = ner.get_model()
        nlp_bytes = pickle.loads(args[3])
        nlp.from_bytes(nlp_bytes)
        recognizer = EntityRecognizer(nlp)

        return {
            "labels": label_list,
            "classifier": classifier,
            "recognizer": recognizer
        }
