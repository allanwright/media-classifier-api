import graphene
from .Class import Class

class Media(graphene.ObjectType):
    name = graphene.String()
    label = graphene.Field(Class, name='class')
    confidence = graphene.Float()