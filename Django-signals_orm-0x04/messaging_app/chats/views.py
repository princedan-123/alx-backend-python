from django.shortcuts import render
from rest_framework import viewsets
from .models import Message, Conversation
from .serializers import MessageSerializer, ConversationSerializer, UserSerializer
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from rest_framework.response import Response
# from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

User = get_user_model()

class ConversationView(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    @cache_page(60)
    @action(methods=['get'], detail=True)
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

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
