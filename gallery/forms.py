from django.forms import ModelForm, Form, ImageField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from gallery.models import Room, Picture


class CreateRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ["name", "discription"]


class AddPictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ["image"]
