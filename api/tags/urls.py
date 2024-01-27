from django.urls import path
from .views import ListTagsAPIView, CreateTagsAPIView

urlpatterns = [
    path("", ListTagsAPIView.as_view(), name="list-tags"),
    path("create/", CreateTagsAPIView.as_view(), name="create-tags"),
]
