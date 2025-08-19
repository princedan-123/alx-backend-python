from django.urls import path, include
from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter
from .views import UserViewSet, MessageViewSet, ConversationViewSet


route = routers.DefaultRouter()
route.register(r'user', UserViewSet)
route.register(r'message', MessageViewSet)
route.register(r'conversation', ConversationViewSet)
conversation_nested_router = NestedDefaultRouter(route, r'conversation', lookup='conversation')
conversation_nested_router.register(r'messages', MessageViewSet, basename='conversation-message')
urlpatterns = [
    path('', include(route.urls)),
    path('', include(conversation_nested_router.urls)),
]
