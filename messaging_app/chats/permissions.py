from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """A permission class that ensures a user can only access his message."""
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False