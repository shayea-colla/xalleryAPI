from gallery.models import Room
from accounts.api.serializers import DesignerSerializer
from rest_flex_fields import FlexFieldsModelSerializer

from core.mixins import SetOwnerTheCurrentUserMixin


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
        )
        # this field is automatically set by the serializer
        read_only_fields = ("owner",)
        expandable_fields = {"owner": DesignerSerializer}
