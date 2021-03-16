from .Label import Label
import graphene

class Classification(graphene.ObjectType):
    label = graphene.Field(Label, name='label')
    confidence = graphene.Float()
