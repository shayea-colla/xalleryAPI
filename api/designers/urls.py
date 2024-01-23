from django.urls import path, include
from rest_framework import routers
from .views import CreateDesigner, ListDesignersView, RetrieveDesignerView


urlpatterns = [
    path("", ListDesignersView.as_view(), name="list_designers"),
    path("create/", CreateDesigner.as_view(), name="create_designer"),
    path("<int:pk>/", RetrieveDesignerView.as_view(), name="retrieve_designer"),
]
