from django.urls import path, include
from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter
from .views import UserViewSet, MessageViewSet, ConversationViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

route = routers.DefaultRouter()
route.register(r'user', UserViewSet)
route.register(r'message', MessageViewSet)
route.register(r'conversation', ConversationViewSet)
conversation_nested_router = NestedDefaultRouter(route, r'conversation', lookup='conversation')
conversation_nested_router.register(r'messages', MessageViewSet, basename='conversation-message')
urlpatterns = [
    path('', include(route.urls)),
    path('', include(conversation_nested_router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]