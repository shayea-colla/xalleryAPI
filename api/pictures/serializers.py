from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from accounts.api.serializers import UserSerializer
from accounts.profiles import Designer
from core import debug
from gallery.models import Picture

from core.mixins import SetOwnerTheCurrentUserMixin
from core.debug import debug


class PictureSerializer(SetOwnerTheCurrentUserMixin, FlexFieldsModelSerializer):
    class Meta:
        model = Picture
        fields = ("id", "owner", "image", "room", "likes")
        read_only_fields = ("owner",)

    def validate_room(self, room):
        """
        check if the user ( request.user ) is the owner of the room.
        """
        user = self.context["request"].user
        if room.owner != user:
            raise serializers.ValidationError("you can not add pictures to this room")
        # room doesn't exist in the data provided, no need to check the room owner
        return super().validate(room)
