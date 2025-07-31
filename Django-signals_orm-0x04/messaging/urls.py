from django.urls import path
from .views import Delete_User
urlpatterns = [
    path('remove_user/<int:pk>', Delete_User.as_view({'delete': 'destroy'})),
]