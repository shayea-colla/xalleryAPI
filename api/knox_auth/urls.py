from django.urls import path
from .views import LoginView
from knox.views import LogoutView, LogoutAllView

urlpatterns = [
    path("login/", LoginView.as_view(), name="knox-login"),
    path("logout/", LogoutView.as_view(), name="knox-logout"),
    path("logoutall/", LogoutAllView.as_view(), name="knox-logoutall"),
]
