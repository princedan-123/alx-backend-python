from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Message, Conversation
from .serializers import UserSerializer, MessageSerializer, ConversationSerializer
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsOwner, IsParticipantOfConversation
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['message_body']

    @action(detail=True, methods=['get'])
    def message_by_id(self, request, pk=None):
        message = self.get_object()
        serialized_message = MessageSerializer(message)
        data = serialized_message.data
        return Response(data, status=status.HTTP_200_OK)
    
    def get_queryset(self):
        """A method that filters queryset for nested urls."""
        conversation_id = self.kwargs.get('conversation_pk')
        filterd_message = Message.objects.filter(conversation_id=conversation_id)
        if filterd_message:
            return filterd_message
        return Message.objects.all()

class ConversationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsParticipantOfConversation, IsAuthenticated]
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer