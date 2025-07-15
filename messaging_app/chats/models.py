from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=21, null=False, blank=False, unique=True)
    user_id = models.UUIDField(default=uuid4, primary_key=True)
    def __str__(self):
        return self.email

class Message(models.Model):
    message_id = models.BigAutoField(primary_key=True)
    message_body = models.TextField(null=False, blank=False)
    sent_at = models.DateTimeField(auto_now=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    def __str__(self):
        return self.message_id

class conversation(models.Model):
    conversation_id = models.BigAutoField(primary_key=True)
    participants = models.ManyToManyField(User, related_name='conversationS')
    def __str__(self):
        return self.conversation_id