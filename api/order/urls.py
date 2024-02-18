from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import OrderViewSet
from . import views


router = SimpleRouter()
router.register(r"orders", OrderViewSet)
urlpatterns = router.urls

