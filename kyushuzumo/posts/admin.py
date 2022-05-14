"""Registering the Post model on the
default admin app provided by Django"""
from django.contrib import admin
from .models import Contact, Post, Pro

admin.site.register(Post)
admin.site.register(Contact)

@admin.register(Pro)
class ProAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank', 'place_of_birth')
