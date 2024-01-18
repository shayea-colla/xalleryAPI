from django.shortcuts import render
from dynamic_rest.viewsets import DynamicModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from gallery.models import Picture

from .serializers import PictureSerializer
from .permissions import PicturePermissions


# Create your views here.
class PictureViewSet(DynamicModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = [PicturePermissions]
