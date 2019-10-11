import graphene
from mccore import prediction
from .Label import Label

class Query(graphene.ObjectType):
    labels = graphene.List(Label)

    @staticmethod
    def resolve_labels(parent, info):
        labels = prediction.get_labels()
        return [{ 'id': k, 'name': v } for (k, v) in labels.items()]