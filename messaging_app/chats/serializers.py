from rest_framework import serializers
from .models import User, Message, Conversation

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    first_name = serializers.CharField()
    class Meta:
        model = User
        fields = [
            'email', 'full_name', 'first_name', 'last_name',
            'phone_number', 'country_code', 'user_id'
            ]
        read_only_fields = ['user_id']

    def get_full_name(self, obj):
        first_name = obj.first_name
        last_name = obj.last_name
        full_name = f'{first_name} {last_name}'
        return full_name
    
    def validate_phone_number(self, value):
        """Validates if phone_number are digits."""
        if not value.isdigit():
            raise serializers.ValidationError('phone_number must be a digit')
        return None

class MessageSerializer(serializers.ModelSerializer):
    message_id = serializers.IntegerField(read_only=True)
    user = UserSerializer()
    class Meta:
        model = Message
        fields = [
            'message_body', 'sent_at',
            'created_at', 'conversation'
            ]

class ConversationSerializer(serializers.ModelSerializer):
    conversation_id = serializers.IntegerField(read_only=True)
    participants = UserSerializer()
    messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Conversation
        fields = '__all__'