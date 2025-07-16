from django.urls import path, include
from rest_framework import routers
from .views import UserViewset, MessageViewset, ConversationViewset

route = routers.DefaultRouter()
route.register(r'user', UserViewset)
route.register(r'message', MessageViewset)
route.register(r'Conversation', ConversationViewset)
urlpatterns = [
    path('', include(route.urls))
]