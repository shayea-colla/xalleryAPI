from django.urls import path, include
from accounts import views

## Commenting the old url

#urlpatterns = [
#    path("", include("django.contrib.auth.urls")),
#    path("add/", views.CreateUserView.as_view(), name="create-user"),
#    path("<int:pk>/", views.ProfileView.as_view(), name="profile"),
#    path("<int:pk>/edit/", views.EditProfileView.as_view(), name="edit-profile"),
#]
