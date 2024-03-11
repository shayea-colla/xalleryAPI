from django.shortcuts import render
from rest_flex_fields import FlexFieldsModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


from core.permissions import IsDesignerOrReadOnly, IsObjectOwnerOrReadOnly
from core.debug import debug
from gallery.models import Picture

from .serializers import PictureSerializer


class PictureViewSet(FlexFieldsModelViewSet):
    """
    Viewset for the Picture model,
    it handle all standard actions provided by ModelViewSet
    """

    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = [
        IsDesignerOrReadOnly,
        IsObjectOwnerOrReadOnly,
    ]

    # Filter config
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["room", "owner"]
