from dynamic_rest.serializers import DynamicModelSerializer
from gallery.models import Picture


class PictureSerializer(DynamicModelSerializer):
    class Meta:
        model = Picture
        fields = ("id", "image", "room")
