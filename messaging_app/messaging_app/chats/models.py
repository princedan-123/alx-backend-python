from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Conversation(models.Model):
    participants = models.ManyToManyField(User)
    start_time = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender_id = models.ForeignKey(User, models.on_delete=CASCADE)
    recipient = models.ForeignKey(User, models.on_delete=CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
