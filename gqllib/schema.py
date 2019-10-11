import graphene
from mccore import prediction

class Label(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()

    @staticmethod
    def resolve_id(parent, info):
        return parent['id']
    
    @staticmethod
    def resolve_name(parent, info):
        return parent['name']

class Query(graphene.ObjectType):
    labels = graphene.List(Label)

    @staticmethod
    def resolve_labels(parent, info):
        labels = prediction.get_labels()
        return [{ 'id': k, 'name': v } for (k, v) in labels.items()]