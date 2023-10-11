from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import SingleObjectMixin
from gallery.models import Picture, Room
from gallery.forms import CreateRoomForm, AddPictureForm

class ExperView(UserPassesTestMixin, SingleObjectMixin,  TemplateView):
    template_name = 'gallery/exper.html'
    model = Room
    context_object_name = 'object'

    def test_func(self):
        print("%" * 100)
        print(self.get_object())
        self.object = self.get_object()
        return True

