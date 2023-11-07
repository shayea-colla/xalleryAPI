from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import SingleObjectMixin
from gallery.models import Picture, Room
from gallery.forms import CreateRoomForm, AddPictureForm


class ExperView(TemplateView):
    pass

