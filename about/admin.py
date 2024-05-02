from django.contrib import admin
from .models import About, Subscribe
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)
