from django.urls import path
from .views import LoginView
from knox.views import LogoutView, LogoutAllView

app_name = "knox"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("logoutall/", LogoutAllView.as_view(), name="logoutall"),
]
