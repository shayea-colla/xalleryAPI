from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import permission_required

from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView


from gallery.models import Picture, Room
from gallery.forms import AddPictureForm


# Index page
class ListAllRooms(ListView):
    """
    Class-based view for displaying a list
    of all rooms available in the website
    """

    model = Room
    template_name = "gallery/list_all_rooms.html"
    paginate_by = 20


class DetailRoomView(DetailView):
    """
    Display indivitual room
    via the primary key specified in the url
    """

    template_name = "gallery/detail_room.html"
    model = Room
    http_method_names = ["get"]

    def get_context_data(self, **kwargs):
        """
        add the "add_picture_form" into detail view
        with the room as initial value for the room field
        """

        context = super().get_context_data(**kwargs)
        """
        Set the initial value of room in AddPictureForm to current room
        """
        form = AddPictureForm()
        form["room"].initial = context["room"]
        context["add_picture_form"] = form
        return context
