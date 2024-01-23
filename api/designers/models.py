from django.db.models import CharField
from django.db import models
from django.forms import ChoiceField
from accounts.models import User

from .managers import DesignersManager


class DesignerMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    favorate_application = models.CharField(
        "Favorate Application",
        max_length=100,
        default="Adobe",
        null=False, 
        blank=False
    )


class Designer(User):
    base_type = User.Types.DESIGNER
    designers = DesignersManager()

    class Meta:
        proxy = True

    @property
    def more(self):
        return self.designermore
