from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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
def detail_room(request, pk):
    template_name = "gallery/detail_room.html"

    """
        function based view for displaying all 
        the information about a single room

        url args: request, pk(uuid for the room)

    """
    room = get_object_or_404(Room, pk=pk)

    context = {
        "room": room,
    }
    return render(request, template_name, context)
