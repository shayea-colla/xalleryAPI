from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from core.permissions import IsDesigner

from .models import Tags
from .serializers import TagsSerializer


# Create your views here.


class ListTagsAPIView(ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [AllowAny]


class CreateTagsAPIView(CreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [IsDesigner]
