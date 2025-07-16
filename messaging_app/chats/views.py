from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Message, Conversation
from .serializers import UserSerializer, MessageSerializer, ConversationSerializer

# Create your views here.

class UserViewset(viewsets.ModelViewset):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MessageViewset(viewsets.ModelViewset):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class ConversationViewset(viewsets.ModelViewset):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer