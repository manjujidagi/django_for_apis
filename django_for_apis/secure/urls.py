from django.urls import path
from .views import UserCreate, LoginView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("users/", UserCreate.as_view(), name="user_create"),
]