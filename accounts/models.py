from django.db.models import (
    CharField,
    ImageField,
    SlugField,
)

from django.contrib.auth.models import AbstractUser, Group
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
        return reverse("profile", args=[self.pk])

    def is_designer(self) -> bool:
        designers_group = Group.objects.get(name="designers")
        return designers_group in self.groups.all()

    def is_owner(self, obj: any) -> bool:
        return obj.owner == self
