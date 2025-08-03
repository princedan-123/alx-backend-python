from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message, Conversation


class UserSerializer(serializers.ModelSerializer):
    """Serializer for Django's built-in User model."""
    
    class Meta:
        model = User
        fields = ['id', 'username']


class MessageSerializer(serializers.ModelSerializer):
    conversation = serializers.PrimaryKeyRelatedField(queryset=Conversation.objects.all())
    
    class Meta:
        model = Message
        fields = [
            'id',
            'sender',
            'receiver',
            'content',
            'timestamp',
            'conversation',
        ]


class ConversationSerializer(serializers.ModelSerializer):
    """Serializer for the Conversation model."""

    participants = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, allow_null=False
        )

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'timestamp']
