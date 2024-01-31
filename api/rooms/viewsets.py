from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_flex_fields.views import FlexFieldsModelViewSet

from core.permissions import IsObjectOwnerOrReadOnly, IsDesignerOrReadOnly
from core.debug import debug
from gallery.models import Room

from .serializers import RoomSerializer
from .utils import clean_tags


# Create your views here.
class RoomViewSet(FlexFieldsModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [
        IsDesignerOrReadOnly,
        IsObjectOwnerOrReadOnly,
    ]

    def get_queryset(self):
        # Get queryset
        queryset = super().get_queryset()

        # Get the tags from url paramaters
        tags = self.request.query_params.get("tags")

        # Check if tags provided or not
        if tags is not None:
            # Clean Tags ( white spaces, empty strings )
            tags = clean_tags(tags.split(","))

            # Filter the queryset by provided tags
            for tag in tags:
                queryset = queryset.filter(tags=tag)

        return queryset
