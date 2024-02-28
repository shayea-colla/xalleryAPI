from django.urls import path
from .views import (
    follow_user_view,
    unfollow_user_view,
    list_create_accounts_view,
    retrieve_update_destroy_account_view,
    user_profile_view,
)


app_name = "accounts"

urlpatterns = [
    path("", list_create_accounts_view, name="list"),
    path("profile/", user_profile_view, name="profile"),
    path(
        "<int:pk>/",
        retrieve_update_destroy_account_view,
        name="detail",
    ),
    path("<int:pk>/follow/", follow_user_view, name="follow"),
    path("<int:pk>/unfollow/", unfollow_user_view, name="unfollow"),
]
