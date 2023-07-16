import uuid
from django.db import models

# Create your models here.
class Picture(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	image = models.ImageField(upload_to='pictures/')


class Room(models.Model):
	pass
