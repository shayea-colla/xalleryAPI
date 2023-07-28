from django.urls import path, include

from gallery.views import get_views as get

urlpatterns = [
        path("", get.ListAllRooms.as_view(), name='list-all-rooms'),
        path("room/<uuid:pk>", get.DetailRoomView.as_view, name='detail-room'),
]
