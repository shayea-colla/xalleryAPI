from rest_framework import serializers
from gallery.models import Room
from api.designers.serializers import UserSerializer
from drf_dynamic_fields import DynamicFieldsMixin
from dynamic_rest import serializers


class RoomSerializer(serializers.DynamicModelSerializer):
    # owner = UserSerializer(read_only=True)
    class Meta:
        model = Room
        fields = ("id", "name", "owner", "background", "discription", "created_at", "pictures")
