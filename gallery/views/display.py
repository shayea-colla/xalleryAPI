from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from django.contrib import messages
from django.contrib.auth.decorators import permission_required

from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, ProcessFormView


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


class DetailRoomView(DetailView, FormMixin):
    """
    __Discription:
        Display indivitual room via the primary key specified in the url
    __Specification: 
        ...
    """

    template_name = "gallery/detail_room.html"
    model = Room
    http_method_names = ["get"]
    form_class = AddPictureForm
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        """
            Set the initial value of room_pk to current room id
        """
        context['form'].initial['room'] = context['room']
        return context



