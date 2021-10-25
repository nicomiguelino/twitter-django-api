from graphene import Field
from graphene_django import DjangoObjectType
from tweets.models import Tweet
from .user import UserType


class TweetType(DjangoObjectType):
    user = Field(UserType, description='The user who created the tweet')

    class Meta:
        model = Tweet
        fields = (
            'id',
            'content',
            'user',
            'created_at',
            'updated_at',
        )
