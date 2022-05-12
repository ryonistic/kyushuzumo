"""Imports the Post model and serializers to
create API views. Viewsets or routers have
not been implemented to keep things simpler.
"""
from django.contrib.auth import get_user_model
from rest_framework import generics
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostList(generics.ListCreateAPIView):
    """A simple ListCreateAPIView that
    allows user to view a list or add more items
    to it, i.e. a blog feed."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """RetrieveUpdateDestroyAPIView that allows
    users to view individual posts that they can update or
    destroy, etc. """
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserList(generics.ListCreateAPIView):
    """A simple ListCreateAPIView that
    allows user to view a list or add more items
    to it, i.e. a user list."""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """RetrieveUpdateDestroyAPIView that allows
    users to view individual users that they can update or
    destroy, etc. """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
