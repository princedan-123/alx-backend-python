from rest_framework.routers import DefaultRouter
from .views import ConversationView, MessageView, UserView
from django.urls import path, include


router = DefaultRouter()
router.register(r'messages', MessageView)
router.register(r'conversation', ConversationView)
router.register(r'user', UserView)


urlpatterns = [
    path('', include(router.urls))
]
