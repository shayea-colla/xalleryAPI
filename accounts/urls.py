from django.urls import path, include
from accounts import views


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("create/", views.add_user, name="create-user"),
    path("<str:username>/", views.profile, name="profile"),
]
