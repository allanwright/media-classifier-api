import graphene

from .Class import Class
from .Classification import Classification
from .Entity import Entity

from mccore import Classifier
from mccore import EntityRecognizer
from mccore import ner
from mccore import persistence

""" classifier = Classifier(
    persistence.bin_to_obj('models/classifier_vec.pickle'),
    persistence.bin_to_obj('models/classifier_mdl.pickle'),
    persistence.json_to_obj('models/label_dictionary.json'))

nlp, _ = ner.get_model()
nlp_bytes = persistence.bin_to_obj('models/ner_mdl.pickle')
nlp.from_bytes(nlp_bytes)
recognizer = EntityRecognizer(nlp) """

class Media(graphene.ObjectType):
    name = graphene.String()
    classification = graphene.Field(Classification)
    entities = graphene.List(Entity)

    @staticmethod
    def resolve_classification(parent, info):        
        prediction = info.context['classifier'].predict(parent.name)
        classification = Classification()
        classification.label = prediction['label']
        classification.confidence = prediction['probability']
        return classification
    
    @staticmethod
    def resolve_entities(parent, info):        
        return [{ 'type': k, 'value': v } for (k, v) in info.context['recognizer'].predict(parent.name)]
