from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView


from gallery.models import Picture, Room


# Index page
class ListAllRooms(ListView):
    """
    Class-based view for displaying a list
    of all rooms available in the website
    """

    model = Room
    template_name = "gallery/list_all_rooms.html"
    paginate_by = 20


@require_http_methods(["GET"])
@permission_required("gallery.view_room", raise_exception=True)
def detail_room(request, pk):
    """
    function based view for displaying all
    the information about a single room

    url args: request, pk (uuid of the room)

    """
    template_name = "gallery/detail_room.html"

    room = get_object_or_404(Room, pk=pk)

    context = {
        "room": room,
    }
    return render(request, template_name, context)
