from django.db import models

# creating a custom manager for custom logic
class UnreadMessagesManager(models.Manager):
    def unread_for_user(self, user):
        """Returns only unread messages."""
        return super().get_queryset().filter(is_read=False, receiver=user).only(
            'sender', 'content', 'timestamp')