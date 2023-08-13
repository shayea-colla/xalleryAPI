from django.db.models import (
    CharField,
    ImageField,
)

from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.
class User(AbstractUser):
    discription = CharField(
        max_length=1000,
        help_text="Write a short bio about yourself ( required )",
        blank=False,
    )

    profile_picture = ImageField(upload_to="profiles/", null=True, blank=True)

    def get_absolute_url(self):
        return reverse("profile", args=[self.username])
