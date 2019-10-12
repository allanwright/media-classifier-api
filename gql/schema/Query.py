import graphene
from mccore import prediction
from .Class import Class

class Query(graphene.ObjectType):
    classes = graphene.List(Class)

    @staticmethod
    def resolve_classes(parent, info):
        labels = prediction.get_labels()
        return [{ 'id': k, 'name': v } for (k, v) in labels.items()]