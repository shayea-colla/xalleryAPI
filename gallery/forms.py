from django.forms import ModelForm, Form, ImageField, CharField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from gallery.models import Room, Picture


class CreateRoomForm(ModelForm):
    # Add a form-controle class to all form fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Room
        fields = ["name", "background", "discription"]


class AddPictureForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Picture
        fields = ["image", "room"]
