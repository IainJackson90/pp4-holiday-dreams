from django.contrib import admin
from .models import Post, Recommendation, Comment


# Register your models here.
admin.site.register(Post)
admin.site.register(Recommendation)
admin.site.register(Comment)