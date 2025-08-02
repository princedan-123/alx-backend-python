from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Conversation(models.Model):
    participants = models.ManyToManyField(User, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    """A model class representing chat messages."""
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_message'
        )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_messages'
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=False, blank=False)
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, null=False, blank=False,
        related_name='messages'
        )

    def __str__(self):
        return f'From {self.sender.username} to {self.receiver.username} at {self.timestamp}'