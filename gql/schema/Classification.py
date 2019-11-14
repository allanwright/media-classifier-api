from .Class import Class
import graphene

class Classification(graphene.ObjectType):
    label = graphene.Field(Class, name='class')
    confidence = graphene.Float()