from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db.models import (
    DateTimeField,
    ForeignKey,
    Model,
    TextField,
    PROTECT,
)


class Tweet(Model):
    content = TextField(
        validators=(
            MinLengthValidator(0),
            MaxLengthValidator(300),
        ),
    )
    user = ForeignKey(
        get_user_model(),
        related_name='tweets',
        on_delete=PROTECT,
        null=True,
    )
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
