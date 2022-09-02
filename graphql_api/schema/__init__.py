from graphene import (
    List,
    ObjectType,
    Schema,
)
from graphql_jwt import (
    ObtainJSONWebToken,
    Verify,
    Refresh,
)
from graphql_jwt.decorators import login_required
from tweets.models import Tweet
from .tweet import TweetType


class Query(ObjectType):
    all_tweets = List(TweetType)

    @login_required
    def resolve_all_tweets(root, info):
        user = info.context.user
        return Tweet.objects.all()


class Mutation(ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    verify_token = Verify.Field()
    refresh_token = Refresh.Field()


schema = Schema(query=Query, mutation=Mutation)
