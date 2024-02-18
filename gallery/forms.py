from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Room, Picture


#class CreateRoomForm(ModelForm):
#    # Add a form-controle class to all form fields
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        for visible in self.visible_fields():
#            visible.field.widget.attrs["class"] = "form-control"
#
#    class Meta:
#        model = Room
#        fields = ["name", "background", "discription"]
#
#
#class AddPictureForm(ModelForm):
#    #    room = forms.UUIDField(widget=forms.HiddenInput)
#    class Meta:
#        model = Picture
#        fields = ["image", "room"]
#
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#
#        for visible in self.visible_fields():
#            visible.field.widget.attrs["class"] = "form-control"
