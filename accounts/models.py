from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db.models import (
    CharField,
    ImageField,
    TextChoices,
)

from django.contrib.auth.models import AbstractUser, Group
from django.urls import reverse


# Create your models here.
class User(AbstractUser):
    class Types(TextChoices):
        DESIGNER = "DESIGNER", "Designer"
        NORMAL = "NORMAL", "Normal"

    discription = CharField(
        max_length=1000,
        help_text="Write a short bio about yourself ( required )",
        blank=False,
    )

    base_type = Types.NORMAL

    picture = ImageField(upload_to="profiles/", null=True, blank=True)

    type = CharField("Type", max_length=50, choices=Types.choices, default=Types.NORMAL)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = self.base_type
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("profile", args=[self.pk])
