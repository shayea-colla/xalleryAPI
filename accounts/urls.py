from django.urls import path, include
from accounts import views


urlpatterns = [
        path("", include("django.contrib.auth.urls")),
        path("create/", views.create_new_account, name='create'),
        path("profile/", views.profile, name="profile"),
            
]
