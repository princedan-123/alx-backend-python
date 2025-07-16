from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewset, MessageViewset, ConversationViewset

router = DefaultRouter()
router.register(r'user', UserViewset)
router.register(r'message', MessageViewset)
router.register(r'Conversation', ConversationViewset)
urlpatterns = [
    path('', include(router.urls))
]