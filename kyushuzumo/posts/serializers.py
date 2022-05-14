from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Contact, Post, Pro


class ProSerializer(serializers.ModelSerializer):
    """Setting up the Post model as a serialized
    entry in DRF"""
    class Meta:
        fields = ('id', 'name', 'rank', 'date_of_birth', 'place_of_birth', 'height', 'weight', 'wins', 'losses', 'no_contest', 'championships', 'image')
        model = Pro

class PostSerializer(serializers.ModelSerializer):
    """Setting up the Post model as a serialized
    entry in DRF"""
    class Meta:
        fields = ('id', 'author', 'title', 'content', 'created_at',)
        model = Post

class UserSerializer(serializers.ModelSerializer):
    """Setting up the default user model as a serialized
    entry in DRF"""
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)

class ContactSerializer(serializers.ModelSerializer):
    """Setting up the default user model as a serialized
    entry in DRF"""
    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'phone', 'message')
