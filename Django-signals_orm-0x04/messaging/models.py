from django.db import models
from django.contrib.auth.models import User
from .managers import UnreadMessagesManager



#  used django default User instance

class Conversation(models.Model):
    participants = models.ManyToManyField(User, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    parent_message field = models.ForeignKey(
        'Message', on_delete=models.CASCADE, null=True,
        blank=True, related_name='replies'
        )
    edited = models.BooleanField(default=False)
    edited_at = models.DateTimeField(null=True, blank=True)
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='edited_messages', null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    timestamp = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, null=False, blank=False,
        related_name='messages'
        )
    objects = models.Manager()
    unread = UnreadMessagesManager()

    def __str__(self):
        return f'{self.sender} to {self.receiver}'
class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='message_history')
    content = models.TextField()
    timestamp = models.DateTimeField(null=True, blank=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='notifications')
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Notification for {self.user.username} about message {self.message.id}'