from django.contrib import admin
from .models import Message, Notification
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Message)
admin.site.register(Notification)