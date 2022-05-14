"""Imports the Post model and serializers to
create API views. Viewsets or routers have
not been implemented to keep things simpler.
"""
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Admission, Contact, Post, Pro
from .permissions import IsAuthorOrReadOnly
from .serializers import AdmissionSerializer, ContactSerializer, PostSerializer, ProSerializer, UserSerializer


class AdmissionView(generics.CreateAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer


class ContactView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    

class ProList(generics.ListCreateAPIView):
    """A simple ListCreateAPIView that
    allows user to view a list or add more items
    to it, i.e. a blog feed."""
    queryset = Pro.objects.all()
    serializer_class = ProSerializer


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


class ProDetail(generics.RetrieveUpdateDestroyAPIView):
    """RetrieveUpdateDestroyAPIView that allows
    users to view individual posts that they can update or
    destroy, etc. """
    permission_classes = (IsAdminUser,)
    queryset = Pro.objects.all()
    serializer_class = ProSerializer

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
