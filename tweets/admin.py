from django.contrib.admin import ModelAdmin, register
from .models import Tweet


@register(Tweet)
class TweetAdmin(ModelAdmin):
    fields = ('content',)
    list_display = ('id', 'content', 'created_at', 'updated_at')
