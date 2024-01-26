from django.urls import path
from .views import ListCreateAccounts, RetrieveUpdateDestroyAccountAPIView

urlpatterns = [
    path("", ListCreateAccounts.as_view(), name="list-accounts"),
    path(
        "<str:username>/",
        RetrieveUpdateDestroyAccountAPIView.as_view(),
        name="user-detail",
    ),
]
