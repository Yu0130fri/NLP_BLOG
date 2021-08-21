from django.contrib import admin

from .models import PostArticle, Comment

admin.site.register(PostArticle)
admin.site.register(Comment)