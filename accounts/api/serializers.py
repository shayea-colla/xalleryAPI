from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from ..profiles import Designer, NormalUser
from ..models import DesignerMore, User

from gallery.utils import debug
from rest_flex_fields.serializers import (
    FlexFieldsModelSerializer,
    FlexFieldsSerializerMixin,
)


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "password",
            "email",
            "type",
            "discription",
            "date_joined",
        )
        read_only_fields = ["id", "date_joined", "type"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        set the password manually ,
        or it will call model.objects.create() and store the row value of the password

        Args:
            validated_data (dictionary): Dictionary containing all the validated data

        Returns:
            model instance: return the created model instance ( user )
        """
        user = super().create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class NormalUserSerializer(UserSerializer):
    """Normal User serializer ,

    Args:
        UserSerializer (serializers.ModelSerializer): inherit from the UserSerializer,
        change the model Meta attribute to  NormalUser
    """

    class Meta(UserSerializer.Meta):
        model = NormalUser


class DesignerMoreSerializer(FlexFieldsModelSerializer):
    favorate_application = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = DesignerMore
        fields = ["favorate_application"]


class DesignerSerializer(UserSerializer, WritableNestedModelSerializer):
    designermore = DesignerMoreSerializer(required=True)

    class Meta(UserSerializer.Meta):
        model = Designer
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "password",
            "email",
            "type",
            "date_joined",
            "discription",
            "designermore",
        )
