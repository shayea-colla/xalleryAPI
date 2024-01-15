from rest_framework import serializers
from gallery.models import Room
from api.designers.serializers import  UserSerializer
from drf_dynamic_fields import DynamicFieldsMixin


class RoomSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Room
        fields = ("id", "name", "owner", "background", "discription", "created_at")
