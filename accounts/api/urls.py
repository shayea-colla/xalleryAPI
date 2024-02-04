from django.urls import path
from .views import ListCreateAccountsAPIView, RetrieveUpdateDestroyAccountAPIView

urlpatterns = [
    path("", ListCreateAccountsAPIView.as_view(), name="list-accounts"),
    path(
        "<str:username>/",
        RetrieveUpdateDestroyAccountAPIView.as_view(),
        name="user-detail",
    ),
]
