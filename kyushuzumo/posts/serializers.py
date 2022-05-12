from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """Setting up the Post model as a serialized
    entry in DRF"""
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'date_posted',)
        model = Post

class UserSerializer(serializers.ModelSerializer):
    """Setting up the default user model as a serialized
    entry in DRF"""
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
