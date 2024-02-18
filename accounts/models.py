from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from api.tags.models import Tag


# Main User Model in Xallery
class User(AbstractUser):
    """
    Base User model for this project ,
    """

    class Types(models.TextChoices):
        DESIGNER = "DESIGNER", "Designer"
        NORMAL = "NORMAL", "Normal"
        SYSTEM = "SYSTEM", "System"

    discription = models.CharField(
        max_length=1000,
        help_text="Write a short bio about yourself ( required )",
        blank=False,
    )

    picture = models.ImageField(
        upload_to="profiles/", verbose_name="Profile picture", null=True, blank=True
    )

    type = models.CharField(
        "Type", max_length=50, choices=Types.choices, default=Types.NORMAL
    )

    birth_date = models.DateField(
        "Birth Date", auto_now=False, auto_now_add=False, null=True
    )

    base_type = Types.SYSTEM

    following = models.ManyToManyField("self", related_name="followers", symmetrical=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = self.base_type
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("accounts:detail", args=[self.pk])


class DesignerMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    favorate_application = models.CharField(
        "Favorate Application", max_length=100, null=False, blank=False
    )

    tags = models.ManyToManyField(
        Tag, verbose_name="Tags", related_name="designers", blank=True
    )

    def __str__(self) -> str:
        return f"designermore: {self.user.username}"
