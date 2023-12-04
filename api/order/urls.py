from django.urls import path, include
from rest_framework import routers
from .views import OrderViewSet
from . import views


router = routers.SimpleRouter()
router.register(r"orders", OrderViewSet)

urlpatterns = router.urls
