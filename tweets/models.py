from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db.models import (
    DateTimeField,
    Model,
    TextField,
)


class Tweet(Model):
    content = TextField(
        validators=(
            MinLengthValidator(0),
            MaxLengthValidator(300),
        ),
    )
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
