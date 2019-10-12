import graphene

class Class(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()

    @staticmethod
    def resolve_id(parent, info):
        return parent['id']
    
    @staticmethod
    def resolve_name(parent, info):
        return parent['name']