from django.urls import path, include
from django.views.generic import TemplateView

from .views import (
        display,
        edit,
        add,
        delete,
)

urlpatterns = [
    # display views
    path(
        "",
        display.ListAllRooms.as_view(),
        name="list-all-rooms"
    ),
    path(
        "room/<uuid:pk>", 
        display.DetailRoomView.as_view(), 
        name="detail-room"
    ),

    # Add views
    path(
        "room/add/",
         add.CreateRoomView.as_view(), 
         name="add-room"
    ),
    # "picture/<uuid:room_pk>/add/",
    path(
        "picture/add/",
        add.AddPictureView.as_view(),
        name="add-picture",
    ),

    # Edit views 
    path(
        "room/<uuid:pk>/edit/",
        edit.UpdateRoom.as_view(), 
        name="edit-room",
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



    # expermental view 
    path(
        "exper/",
        TemplateView.as_view(template_name='gallery/exper.html'),
        name="Exper",
    ),
]
