from django.urls import path, include
from django.views.generic import TemplateView

from .views import (
    display,
    edit,
    add,
    delete,
)


"""
Commenting the old url pattern and replace it with the patern found in the api/rooms/ application
"""

#urlpatterns = [
#    # display views
#    path("", display.ListAllRooms.as_view(), name="list-all-rooms"),
#    path("room/<uuid:pk>", display.DetailRoomView.as_view(), name="detail-room"),
#    # Add views
#    path("room/add/", add.CreateRoomView.as_view(), name="add-room"),
#    # Edit views
#    path(
#        "room/<uuid:pk>/edit/",
#        edit.UpdateRoom.as_view(),
#        name="edit-room",
#    ),
#    # Delete views
#    path("room/<uuid:pk>/delete/", delete.DeleteRoomView.as_view(), name="delete-room"),
#    path(
#        "picture/add/",
#        add.AddPictureView.as_view(),
#        name="add-picture",
#    ),
#    path(
#        "picture/<uuid:pk>/delete/",
#        delete.DeletePictureView.as_view(),
#        name="delete-picture",
#    ),
#]
