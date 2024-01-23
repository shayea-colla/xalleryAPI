from django.shortcuts import render
from rest_flex_fields import FlexFieldsModelViewSet
from gallery.models import Picture

from .serializers import PictureSerializer
from .permissions import PicturePermissions


# Create your views here.
