from rest_flex_fields.views import FlexFieldsModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


from core.permissions import IsObjectOwnerOrReadOnly, IsDesignerOrReadOnly
from core.debug import debug
from gallery.models import Room

from .serializers import RoomSerializer
from .filters import RoomTagsFilter
from .utils import clean_tags, create_tags


# Create your views here.
class RoomViewSet(FlexFieldsModelViewSet):
    # Queryset and serializer
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    # Permissions
    permission_classes = [
        IsDesignerOrReadOnly,
        IsObjectOwnerOrReadOnly,
    ]

    # Filter config
    filter_backends = [DjangoFilterBackend, RoomTagsFilter]
    filterset_fields = ["name", "owner"]
