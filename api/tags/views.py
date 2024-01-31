from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_flex_fields.views import FlexFieldsMixin
from rest_flex_fields import is_expanded

from core.permissions import IsDesigner

from .models import Tag
from .serializers import TagSerializer

# Create your views here.


class ListTagsAPIView(ListAPIView):
    permit_list_expands = ["rooms"]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]


class CreateTagsAPIView(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsDesigner]
