import graphene
from .Class import Class
from .Entity import Entity

class Media(graphene.ObjectType):
    name = graphene.String()
    label = graphene.Field(Class, name='class')
    confidence = graphene.Float()
    entities = graphene.List(Entity)