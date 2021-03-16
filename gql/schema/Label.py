import graphene

class Label(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
