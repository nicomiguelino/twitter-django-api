import functools
from django.core.management import call_command


def flush_database(func):
    @functools.wraps(func)
    def wrapper(self, *args, **options):
        if options['flush']:
            call_command('flush', '--no-input')

        return func(self, *args, **options)

    return wrapper
