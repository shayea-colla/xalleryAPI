from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .viewsets import RoomViewSet

from .views import like_room_view, unlike_room_view


router = SimpleRouter()
router.register(r"rooms", RoomViewSet, basename="rooms")
urlpatterns = [
    path("rooms/<uuid:pk>/like/", like_room_view, name="room_like"),
    path("rooms/<uuid:pk>/unlike/", unlike_room_view, name="room_unlike"),
    path("", include(router.urls)),
]
