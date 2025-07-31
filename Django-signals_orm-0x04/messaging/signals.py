"""A module containing signal implementation for the messaging app."""
from django.db.models.signals import post_save, pre_save, post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory
from django.utils import timezone

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)

@receiver(pre_save, sender=Message)
def save_old_message(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_message = Message.objects.get(pk=instance.pk)
            if old_message.content != instance.content:
                instance.edited = True
                instance.edited_by = instance.sender
                instance.edited_at = timezone.now()
                MessageHistory.objects.create(
                    message=old_message, content=message.content,
                    timestamp=message.timestamp
                    )
        except Exception as e:
            print(f'An error occured {e}')


@receiver(post_delete, sender=User)
def delete_user_data(sender, instance, **kwargs):
    messages = Message.objects.filter(sender=instance)
    messages.delete()