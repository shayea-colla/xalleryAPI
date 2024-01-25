from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


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

    picture = models.ImageField(upload_to="profiles/", null=True, blank=True)

    type = models.CharField(
        "Type", max_length=50, choices=Types.choices, default=Types.NORMAL
    )

    birth_date = models.DateField(
        "Birth Date", auto_now=False, auto_now_add=False, null=True
    )
    base_type = Types.SYSTEM

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = self.base_type
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("profile", args=[self.pk])


class DesignerMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    favorate_application = models.CharField(
        "Favorate Application", max_length=100, null=False, blank=False
    )

    def __str__(self) -> str:
        return f"designer: {self.user.username},favorate_application: {self.favorate_application}"
