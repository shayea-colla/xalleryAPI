from django.forms import ModelForm, CharField

from accounts.models import User


class CreateUserForm(ModelForm):
    discription = CharField(max_length=1000, required=False)

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
