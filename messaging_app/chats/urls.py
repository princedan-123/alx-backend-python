from django.urls import path, include
from rest_framework import router
from .views import UserViewset, MessageViewset, ConversationViewset

router = router.DefaultRouter()
router.register(r'user', UserViewset)
router.register(r'message', MessageViewset)
router.register(r'Conversation', ConversationViewset)
urlpatterns = [
    path('', include(router.urls))
]