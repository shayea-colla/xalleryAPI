from django.urls import path, include
from rest_framework import routers
from .views import ListDesignersView, RetrieveDesignerView


urlpatterns = [
    path("", ListDesignersView.as_view()),
    path("<int:pk>/", RetrieveDesignerView.as_view()),
]
