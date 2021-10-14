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

    @flush_database
    def handle(self, *args, **options):
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
