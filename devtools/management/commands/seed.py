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

    def initialize_superusers(self):
        get_user_model().objects.create_superuser(
            username='superuser_01',
            password='password',
            email='superuser_01@example.com',
            first_name='Elliot',
            last_name='Alderson',
        )

    def initialize_users(self):
        return (
            get_user_model().objects.create_user(
                username='alex.walters',
                password='password',
                email='alex.walters@example.com',
                first_name='Alex',
                last_name='Walters',
            ),
            get_user_model().objects.create_user(
                username='harry.potter',
                password='password',
                email='harry.potter@example.com',
                first_name='Harry',
                last_name='Potter',
            ),
        )

    def initialize_tweets(self, users):
        user_1, user_2 = users
        tweets = [
            {
                'content': 'My very first tweet. Yay!',
                'user': user_1,
            },
            {
                'content': 'Yet another tweet from yours, truly.',
                'user': user_2,
            },
            {
                'content': 'Third time\'s a charm, indeed!',
                'user': user_1,
            },
            {
                'content': 'Make good choices. #MagpaRehistroKa',
                'user': user_2,
            },
        ]

        for tweet in tweets:
            Tweet.objects.create(**tweet)

    @flush_database
    def handle(self, *args, **options):
        self.initialize_superusers()
        users = self.initialize_users()
        self.initialize_tweets(users)
