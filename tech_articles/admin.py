from django.contrib import admin
from tech_articles.models import tech_Article
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

admin.site.register(tech_Article)


