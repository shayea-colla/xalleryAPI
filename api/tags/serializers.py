from rest_framework import serializers
from rest_flex_fields.serializers import FlexFieldsModelSerializer

from api.rooms.serializers import RoomSerializer

from .models import Tag


class TagSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Tag
        fields = ("name", "rooms")
        read_only_fields = ("rooms",)
        expandable_fields = {"rooms": (RoomSerializer, {"many": True})}
