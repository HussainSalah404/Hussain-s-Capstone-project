"""
Defines custom permission for recipes.

- IsOwnerOrReadOnly: Allows read access to everyone but write access only to recipe owners.
"""
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """Only recipe owners can modify; others can view."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(obj, 'owner', None) == request.user