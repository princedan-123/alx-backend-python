from rest_framework import permissions
from django.contrib.auth.models import AnonymousUser

class IsOwner(permissions.BasePermission):
    """A permission class that ensures a user can only access his message."""
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False

class IsParticipantOfConversation(permission.BasePermission):
    """ 
        A custom permission class that does the following
        Allow only authenticated users to access the api
        Allow only participants in a conversation to send,
        view, update and delete messages
    """
    def has_object_permission(self, request, view, obj):
        if request.user and not isinstance(request.user, AnonymousUser):
            return request.user ==  obj.participants
            
