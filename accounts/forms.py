from django.forms import ModelForm, CharField

from accounts.models import User


class CreateUserForm(ModelForm):
    
    # Add a form-controle class to all form fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "discription",
            "password",
        ]
