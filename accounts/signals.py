from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.dispatch import receiver

from .models import User

from api.designers.models import Designer
from gallery.utils import debug


@receiver(post_save, sender=Designer)
def assign_designers_group(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name="designers")
        instance.groups.add(group)
