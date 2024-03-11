from logging import raiseExceptions
from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.dispatch import receiver

from core.debug import debug

from .profiles import Designer
from .models import DesignerMore


@receiver(post_save, sender=Designer)
def assign_designers_group(sender, instance, created, **kwargs):
    if created:
        group, created = Group.objects.get_or_create(name="designers")
        instance.groups.add(group)
