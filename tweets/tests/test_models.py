from ..models import Tweet


def test_create_tweet_success(db):
    tweet = Tweet.objects.create(
        content='I\'ve finally created my Twitter account. Hello everyone!'
    )

    assert hasattr(tweet, 'created_at')
    assert hasattr(tweet, 'updated_at')
