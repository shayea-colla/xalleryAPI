from rest_framework import serializers
from gallery.models import Room
from accounts.api.serializers import UserSerializer
import json


class RoomSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Room
        fields = (
            "id",
            "name",
            "owner",
            "background",
            "discription",
            "created_at",
            "pictures",
        )
