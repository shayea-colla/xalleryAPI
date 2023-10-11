from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView

from gallery.models import Picture, Room
from gallery.forms import CreateRoomForm, AddPictureForm



class UpdateRoom(UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    def test_func(self):
        # Only the owner of the Room can edit it 
        return self.get_object().owner == self.request.user


    model = Room
    form_class = CreateRoomForm
    template_name = "gallery/room_edit_form.html"


