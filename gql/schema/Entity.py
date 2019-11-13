import graphene

class Entity(graphene.ObjectType):
    type = graphene.String()
    value = graphene.String()