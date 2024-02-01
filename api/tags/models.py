from django.db import models

# Create your models here.


class Tag(models.Model):
    """
    Tags model holds info about tags
    that will be used with filtering rooms.

    Args:
        Model (django Model): Base Model class provided by Django
    """

    name = models.CharField(primary_key=True, max_length=150, unique=True)

    def __str__(self) -> str:
        return self.name
