import graphene
from mccore import Classifier
from mccore import EntityRecognizer
from mccore import prediction
from .Class import Class
from .Media import Media

class Query(graphene.ObjectType):
    classes = graphene.List(Class)
    media = graphene.Field(Media, name=graphene.String(required=True))

    @staticmethod
    def resolve_classes(parent, info):
        labels = prediction.get_labels()
        return [{ 'id': k, 'name': v } for (k, v) in labels.items()]
    
    @staticmethod
    def resolve_media(parent, info, name):
        media = Media()
        media.name = name
        return media