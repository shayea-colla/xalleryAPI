from django.urls import path, include


from gallery.views import display
from gallery.views import edit
from gallery.views import add
from gallery.views import delete

urlpatterns = [
    # display views
    path(
        "",
        display.ListAllRooms.as_view(),
        name="list-all-rooms"
    ),
    path(
        "room/<uuid:pk>", 
        display.detail_room, 
        name="detail-room"
    ),

    # Add views
    path(
        "room/add/",
         add.add_room, 
         name="add-room"
    ),
    path(
        "picture/<uuid:room_pk>/add/",
        add.add_picture_to_room,
        name="add-picture",
    ),

    # Delete views
    path(
        "room/<uuid:room_pk>/delete/",
        delete.delete_room,
        name="delete-room"
    ),
    path(
        "picture/<uuid:picture_pk>/delete/",
        delete.delete_picture,
        name="delete-picture",
    ),
]
