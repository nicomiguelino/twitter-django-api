from pytest import fixture
from django.contrib.auth import get_user_model
from ..models import Tweet


@fixture
def user_1(db):
    instance = get_user_model().objects.create_user(
        username='mickey.mouse',
        password='hotdoghotdiggetydog',
        email='mickey.mouse@gmail.com',
        first_name='Mickey',
        last_name='Mouse',
    )
    assert instance.tweets.count() == 0
    return instance


def test_create_tweet_success(db, user_1):
    tweet = Tweet.objects.create(
        content='I\'ve finally created my Twitter account. Hello everyone!',
        user=user_1,
    )

    assert tweet.user == user_1
    assert user_1.tweets.count() == 1

    assert hasattr(tweet, 'created_at')
    assert hasattr(tweet, 'updated_at')
