from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework.serializers import ValidationError
from gallery.models import Picture


class PictureSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Picture
        fields = ("id", "image", "room")

    def validate(self, data):
        """
        check if the user is the owner of the room or not
        """
        user = self.context["request"].user
        if data["room"].owner != user:
            raise ValidationError("you can not add pictures to this room")

        # Automatically set the owner to the current user
        data["owner"] = user
        return data
