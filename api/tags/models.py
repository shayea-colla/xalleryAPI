from django.db import models

# Create your models here.


class Tags(models.Model):
    """
    Tags model holds info about tags
    that will be used with rooms and pcitures to filter them

    Args:
        Model (django Model): Base Model class provided by Django
    """

    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name
