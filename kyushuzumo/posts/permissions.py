"""Handling custom permissions for our API"""
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """We are overriding default has_object_permission"""
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author
        return obj.author == request.user
