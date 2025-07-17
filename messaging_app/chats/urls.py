from django.urls import path, include
from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter
from .views import UserViewset, MessageViewset, ConversationViewset

route = routers.DefaultRouter()
route.register(r'user', UserViewset)
route.register(r'message', MessageViewset)
route.register(r'Conversation', ConversationViewset)
conversation_nested_router = NestedDefaultRouter(route, r'conversation', lookup='conversation')
conversation_nested_router.register(r'messages', MessageViewset, basename='conversation-message')
urlpatterns = [
    path('', include(route.urls)),
    path('', include(conversation_nested_router.urls))
]