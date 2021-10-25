from django.contrib.auth import get_user_model
from pytest import fixture

from tweets.models import Tweet


@fixture
def user_1(db):
    return get_user_model().objects.create_user(
        username='donald.duck',
        password='scrooge',
        email='donald.duck@gmail.com',
        first_name='Donald',
        last_name='Duck',
    )


def test_query_all_tweets(client, user_1):
    tweet_args_set = [
        {
            'content': 'Hello, Twitter!',
            'user': user_1,
        },
        {
            'content': 'This is my second tweet.',
            'user': user_1,
        },
    ]

    for tweet_args in tweet_args_set:
        Tweet.objects.create(**tweet_args)

    response = client.execute(
        '''
        {
            allTweets {
                id
                content
                user {
                    username
                    email
                }
                createdAt
                updatedAt
            }
        }
        '''
    )

    data = response['data']

    assert len(data['allTweets']) == len(tweet_args_set)
