from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """A permission class that ensures a user can only access his message."""
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False