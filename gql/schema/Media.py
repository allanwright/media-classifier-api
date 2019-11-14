import graphene
from .Class import Class
from .Classification import Classification
from .Entity import Entity
from mccore import Classifier
from mccore import EntityRecognizer

classifier = Classifier.load_default()
recognizer = EntityRecognizer.load_default()

class Media(graphene.ObjectType):
    name = graphene.String()
    classification = graphene.Field(Classification)
    entities = graphene.List(Entity)

    @staticmethod
    def resolve_classification(parent, info):        
        label, confidence = classifier.predict(parent.name)
        classification = Classification()
        classification.label = label
        classification.confidence = confidence
        return classification
    
    @staticmethod
    def resolve_entities(parent, info):        
        return [{ 'type': k, 'value': v } for (k, v) in recognizer.predict(parent.name)]