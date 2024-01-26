from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework.serializers import ValidationError
from gallery.models import Picture


class PictureSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Picture
        fields = ("id", "image", "room")
        read_only_fields = ("owner",)

    def validate(self, data):
        """
        check if the user ( request.user ) is the owner of the room or not
        """
        user = self.context["request"].user
        if data["room"].owner != user:
            raise ValidationError("you can not add pictures to this room")

        # Automatically set the owner to be the current user
        data["owner"] = user
        return data
