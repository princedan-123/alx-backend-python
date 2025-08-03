from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Message, Conversation
from .serializers import MessageSerializer, ConversationSerializer, UserSerializer
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

# Create your views here.

class delete_user(viewsets.ViewSet):
    def destroy(self, request, pk=None):
        """Deletes a user by id"""
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(
                {'deleted': f'user with id {pk} deleted successfully'},
                status=status.HTTP_204_NO_CONTENT
                )
        except User.DoesNotExist:
            return Response(
                {'Error': f'User with id {pk} not found'},
                status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            return Response(
                {'An error occured': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

User = get_user_model()

class ConversationView(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    @action(methods=['get'], detail=True)
    @method_decorator(cache_page(60))
    def my_messages(self, request, pk=None):
        """list all messages within a conversation."""
        try:
            conversation = Conversation.objects.get(pk=pk)
        except Conversation.DoesNotExist:
            return Response(
                {'Error': f'this conversation {pk} does not exist'},
                status=404
                )
        messages = conversation.messages.all()
        serialized_message = MessageSerializer(messages, many=True)
        return Response(
            {f'messages_in_{pk}_conversation':serialized_message.data}
            )

class MessageView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    @action(detail=True, methods=['get'])
    def unread_messages(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'Error': 'User not found'}, status=404)

        unread_messages = Message.unread.unread_for_user(user).only(
            'sender', 'content', 'timestamp'
        )
        serialized_data = MessageSerializer(unread_messages, many=True)
        return Response({'unread_messages': serialized_data.data})


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

