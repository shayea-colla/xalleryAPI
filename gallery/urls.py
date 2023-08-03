from django.urls import path, include

from gallery.views import display_views as get
from gallery.views import edit_views as edit

from gallery.views import tmp_views as tmp

urlpatterns = [
    # Get views
    path("", get.ListAllRooms.as_view(), name="list-all-rooms"),
    path("room/<uuid:pk>", get.detail_room, name="detail-room"),
    # Edit views
    path("room/add/", edit.add_room, name="add-room"),
    path("room/<uuid:room_pk>/delete/", edit.delete_room, name="delete-room"),
    path("picture/<uuid:room_pk>/add/", edit.add_picture_to_room, name="add-picture"),
    path(
        "picture/<uuid:picture_pk>/delete/", edit.delete_picture, name="delete-picture"
    ),
    # Temporary views for testing porpuses
    path("tmp/", tmp.perms_view, name="tmp"),
]
