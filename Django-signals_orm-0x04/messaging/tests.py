from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification

# Create your tests here.

class TestSignal(TestCase):
    """Testing the signal if it works."""
    def test_signal(self):
        sender = User.objects.create_user('Daniel', 'simrop@mtn.ng', 'test')
        receiver = User.objects.create_user('Frank', 'dlcm@mtn.ng', 'test')
        message = Message.objects.create(
            content='Hello support engineers', sender=sender,
            receiver=receiver
            )
        self.assertEqual(Notification.objects.count(), 1)
        self.assertFalse(Notification.objects.first().is_read)
        self.assertEqual(Notification.objects.first().user.username, 'Frank') 