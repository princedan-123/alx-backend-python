from django.shortcuts import render
from rest_framework import viewsets
from .models import Message, Conversation
from .serializers import MessageSerializer, ConversationSerializer, UserSerializer
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.views.decorators.cache import cache_page

User = get_user_model()

@cache_page(60)
def my_messages_view(request, pk):
    """List all messages within a conversation (cached for 60 seconds)."""
    if request.method != 'GET':
        return Response({'detail': 'Method not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    try:
        conversation = Conversation.objects.get(pk=pk)
    except Conversation.DoesNotExist:
        return Response(
            {'Error': f'This conversation {pk} does not exist'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    messages = conversation.messages.all()
    serialized_message = MessageSerializer(messages, many=True)
    return Response(
        {f'messages_in_{pk}_conversation': serialized_message.data}
    )

class MessageView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
