from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated

from rest_flex_fields.views import FlexFieldsModelViewSet

from core.permissions import IsObjectOwnerOrReadOnly, IsDesignerOrReadOnly
from gallery.models import Room
from .serializers import RoomSerializer


# Create your views here.
class RoomViewSet(FlexFieldsModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [
        IsDesignerOrReadOnly,
        IsObjectOwnerOrReadOnly,
    ]
