from rest_framework.routers import SimpleRouter
from .views import RoomViewSet


router = SimpleRouter()
router.register(r"rooms", RoomViewSet, basename="rooms")
urlpatterns = router.urls
