from rest_framework.routers import SimpleRouter
from .viewsets import RoomViewSet


router = SimpleRouter()
router.register(r"rooms", RoomViewSet, basename="rooms")
urlpatterns = router.urls
