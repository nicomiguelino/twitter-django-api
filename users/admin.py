from django.contrib.admin import ModelAdmin, register
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


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


@register(Permission)
class PermissionAdmin(ModelAdmin):
    fields = (
        'name',
        'codename',
        'content_type',
    )
    list_display = (
        'name',
        'codename',
        'content_type',
    )


@register(ContentType)
class ContentTypeAdmin(ModelAdmin):
    fields = (
        'app_label',
        'model',
    )
    list_display = (
        'app_label',
        'model',
        'name',
        '__str__',
    )
