from django.db import models
from django.contrib.auth.models import User

#  used django default User instance

class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.sender} to {self.receiver}'

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='notifications')
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Notification for {self.user.username} about message {self.message.id}'