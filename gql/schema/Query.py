import graphene

from .Label import Label
from .Media import Media

class Query(graphene.ObjectType):
    labels = graphene.List(Label)
    media = graphene.Field(Media, name=graphene.String(required=True))

    @staticmethod
    def resolve_labels(parent, info):
        return info.context['labels']

    @staticmethod
    def resolve_media(parent, info, name):
        media = Media()
        media.name = name
        return media
