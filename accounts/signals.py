from logging import raiseExceptions
from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.dispatch import receiver

from gallery.utils import debug

from .profiles import Designer
from .models import DesignerMore


@receiver(post_save, sender=Designer)
def assign_designers_group(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name="designers")
        instance.groups.add(group)
