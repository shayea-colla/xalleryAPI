from django.db.models import (
        CharField,
        ImageField,
     )

from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    discription = CharField(max_length=1000, help_text="Write a short bio about yourself ( Optional )", blank=True)

    profile_picture = ImageField(upload_to='profiles/', null=True, blank=True)

