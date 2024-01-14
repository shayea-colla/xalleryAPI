from django.urls import path, include
from rest_framework import routers
from .views import OrderViewSet, ListDesignersView
from . import views


router = routers.SimpleRouter()
router.register(r"orders", OrderViewSet)

urlpatterns =[
    path("designers/", ListDesignersView.as_view()),

] + router.urls

