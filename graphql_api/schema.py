from graphene import (
    List,
    ObjectType,
    Schema,
    String,
)
from graphene_django import DjangoObjectType
from tweets.models import Tweet


class TweetType(DjangoObjectType):
    class Meta:
        model = Tweet
        fields = ('id', 'content', 'created_at', 'updated_at')


class Query(ObjectType):
    tweets = List(TweetType)

    def resolve_tweets(root, info):
        return Tweet.objects.all()


schema = Schema(query=Query)
