from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView

from gallery.models import Picture, Room

# Index page
#@require_http_methods(['GET'])
class ListAllRooms(ListView):
    model = Room
    template_name = 'gallery/list_all_rooms.html'


class DetailRoomView(DetailView):
    model = Room
    template_name = 'gallery/detail_room.html'
