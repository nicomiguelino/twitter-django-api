from graphene import (
    List,
    ObjectType,
    Schema,
)
from tweets.models import Tweet
from .tweet import TweetType


class Query(ObjectType):
    all_tweets = List(TweetType)

    def resolve_all_tweets(root, info):
        return Tweet.objects.all()


schema = Schema(query=Query)
