from rest_framework import permissions
from django.contrib.auth.models import AnonymousUser

class IsOwner(permissions.BasePermission):
    """A permission class that ensures a user can only access his message."""
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False

class IsParticipantOfConversation(permissions.BasePermission):
    """ 
        A custom permission class that does the following
        Allow only authenticated users to access the api
        Allow only participants in a conversation to send,
        view, update and delete messages
    """
    def has_permission(self, request, view):
        """This method grants permission if the user is authenticated."""
        return request.user.is_authenticated

    def has_object_permission(self, request, view, message):
        methods = ["PUT", "PATCH", "DELETE"]
        if request.method in methods:
            user_id = request.user.user_id
            conversation = message.conversation
            return conversation.participants.filter(id=user_id).exists
        return True
            

            
