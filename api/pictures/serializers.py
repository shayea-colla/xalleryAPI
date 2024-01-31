from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from accounts.api.serializers import UserSerializer
from accounts.profiles import Designer
from core import debug
from gallery.models import Picture

from core.mixins import SetOwnerTheCurrentUserMixin


class PictureSerializer(SetOwnerTheCurrentUserMixin, FlexFieldsModelSerializer):
    class Meta:
        model = Picture
        fields = ("id", "owner", "image", "room")
        read_only_fields = ("owner",)

    def validate(self, data):
        """
        check if the user ( request.user ) is the owner of the room.
        - this method will be called for every save or update to the data,
        """
        user = self.context["request"].user
        # Get the room
        room = data.get("room")
        # Check room value
        if room is not None:
            # room exist in the data provided , check the room owner
            if room.owner != user:
                raise serializers.ValidationError(
                    "you can not add pictures to this room"
                )
        # room doesn't exist in the data provided, no need to check the room owner
        return super().validate(data)
