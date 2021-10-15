from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from devtools.decorators import flush_database
from tweets.models import Tweet


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--flush',
            action='store_true',
            help='flushes the database before loading data',
        )

    def initialize_users(self):
        get_user_model().objects.create_superuser(
            username='superuser_01',
            password='password',
            email='superuser_01@example.com',
            first_name='Elliot',
            last_name='Alderson',
        )
        get_user_model().objects.create_user(
            username='alex.walters',
            password='password',
            email='alex.walters@example.com',
            first_name='Alex',
            last_name='Walters',
        )

    def initialize_tweets(self):
        tweets = [
            {
                'content': 'My very first tweet. Yay!',
            },
            {
                'content': 'Yet another tweet from yours, truly.',
            },
            {
                'content': 'Third time\'s a charm, indeed!',
            },
            {
                'content': 'Make good choices. #MagpaRehistroKa',
            },
        ]

        for tweet in tweets:
            Tweet.objects.create(**tweet)

    @flush_database
    def handle(self, *args, **options):
        self.initialize_users()
        self.initialize_tweets()
