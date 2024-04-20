from django.contrib import admin
from .models import Post, Recommendation, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, search fields,
    filter fields and fields to prepopulate a rich-text editor.
    """

    list_display = ('title', 'slug', 'status')
    search_fields = ['title', 'experience']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('experience', 'excerpt',)


@admin.register(Recommendation)
class RecommendationAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, search fields,
    filter fields and fields to prepopulate a rich-text editor.
    """

    list_display = ('holiday_season', 'sites', 'holiday_length', 'restaurants', 'to_avoid', 'cost_expected' )
    search_fields = ['title']
    "list_filter = ('status',)"
    "prepopulated_fields = {'slug': ('title',)}"
    summernote_fields = ('restaurants', 'sites', 'to_avoid', 'bag_recommendation', 'sites')    

# Register your models here.
admin.site.register(Comment)