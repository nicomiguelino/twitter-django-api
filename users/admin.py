from django.contrib.admin import ModelAdmin, register
from django.contrib.auth import get_user_model


@register(get_user_model())
class UserAdmin(ModelAdmin):
    fields = (
        'username',
        'email',
        'first_name',
        'last_name',
    )
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'is_superuser',
    )
