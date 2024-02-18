from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .viewsets import RoomViewSet

from .views import like_room_view, unlike_room_view
from rest_framework.routers import SimpleRouter
from django.urls import reverse

from core.debug import debug

app_name = 'rooms'


# Register ViewSet with custom router
router = SimpleRouter()
router.register('rooms', RoomViewSet)




#router = SimpleRouter()
#router.register("",RoomViewSet)

urlpatterns = [
    path("rooms/<uuid:pk>/like/", like_room_view, name="like"),
    path("rooms/<uuid:pk>/unlike/", unlike_room_view, name="unlike"),
    path("", include(router.urls)),
]
