from gallery.models import Room
from accounts.api.serializers import DesignerSerializer
from rest_flex_fields import FlexFieldsModelSerializer

from core.mixins import SetOwnerTheCurrentUserMixin
from core.debug import debug

from .utils import clean_tags, create_tags


class RoomSerializer(SetOwnerTheCurrentUserMixin, FlexFieldsModelSerializer):
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
            "tags",
            "likes",
        )
        # this field is automatically set by the serializer
        read_only_fields = (
            "owner",
            "pictures",
            "created_at",
        )
        expandable_fields = {"owner": DesignerSerializer}


#    def validate_tags(self, tags):
#        """Clean tags"""
#        debug(tags)
#        return clean_tags(tags)
#
#    def create(self, validated_data):
#        """Create all tags attached to the room"""
#        tags = validated_data.get("tags")
#        # Check if no tags provided
#        if tags != None:
#            create_tags(tags)
#        return super().create(validated_data)
#
