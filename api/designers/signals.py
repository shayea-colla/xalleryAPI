from gallery.utils import debug
from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.dispatch import receiver

from .models import Designer, DesignerMore
from .utils import create_designers_group
from gallery.utils import debug


@receiver(post_save, sender=Designer)
def create_designer_more_instance(sender, instance, created, **kwargs):
    debug("")
