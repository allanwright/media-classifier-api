import graphene

from .Classification import Classification
from .Entity import Entity

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
