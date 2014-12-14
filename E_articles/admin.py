from django.contrib import admin
from E_articles.models import Article, Comment, CommentSecond
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(CommentSecond)


