"""Registering the Post model on the
default admin app provided by Django"""
from django.contrib import admin
from .models import Post

admin.site.register(Post)
