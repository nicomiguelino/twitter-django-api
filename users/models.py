from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        if self.first_name == '' or self.last_name == '':
            return self.username
        else:
            return f'{self.first_name} {self.last_name}'
