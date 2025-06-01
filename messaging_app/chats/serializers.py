"""A module for serializing my models."""
from rest_framework import serializers
from .models import User, Conversation, Message

class SerializeUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SerializeConversation(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'

class SerializeMessage(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'