from django.urls import path
from .views import ListTagsAPIView, CreateTagsAPIView

app_name = "tags"

urlpatterns = [
    path("", ListTagsAPIView.as_view(), name="list"),
    path("create/", CreateTagsAPIView.as_view(), name="create"),
]
