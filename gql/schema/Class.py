import graphene

class Class(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()