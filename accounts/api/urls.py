from django.urls import path
from .views import  follow_user_view, unfollow_user_view, list_create_accounts_view, retrieve_update_destroy_account_view

urlpatterns = [
    path("", list_create_accounts_view, name="list-accounts"),
    path(
        "<int:pk>/",
        retrieve_update_destroy_account_view,
        name="user-detail",
    ),
    path("<int:pk>/follow/", follow_user_view, name='user-follow'),
    path("<int:pk>/unfollow/", unfollow_user_view, name='user-unfollow'),
]
