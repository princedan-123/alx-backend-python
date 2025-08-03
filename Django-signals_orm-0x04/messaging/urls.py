from django.urls import path, include
from .views import delete_user, ConversationView, MessageView, UserView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'messages', MessageView)
router.register(r'conversation', ConversationView)
router.register(r'user', UserView)

urlpatterns = [
    path('remove_user/<int:pk>', delete_user.as_view({'delete': 'destroy'})),
    path('', include(router.urls))
]