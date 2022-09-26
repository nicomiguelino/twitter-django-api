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

    # nico start - old code
    # todo nico: remove this block if not needed
    # @login_required
    # def resolve_all_tweets(root, info):
    #     user = info.context.user
    #     return Tweet.objects.all()
    # nico end

    # nico start - new code
    def resolve_all_tweets(root, info):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception('Lorem ipsum dolor sit amet.')
    # nico end


# nico start - new code
class CustomObtainJSONWebToken(ObtainJSONWebToken):
    @classmethod
    def mutate(cls, *args, **kwargs):
        try:
            return super().mutate(*args, **kwargs)
        except:
            raise Exception
# nico end


class Mutation(ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    verify_token = Verify.Field()
    refresh_token = Refresh.Field()


schema = Schema(query=Query, mutation=Mutation)
