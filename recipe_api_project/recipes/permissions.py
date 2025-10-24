from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Safe methods: anyone can read
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only author can edit/delete
        return obj.author == request.user
