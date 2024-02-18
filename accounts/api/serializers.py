from rest_framework import serializers

from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_flex_fields.serializers import (
    FlexFieldsModelSerializer,
    FlexFieldsSerializerMixin,
)

from core.debug import debug

from ..profiles import Designer, NormalUser
from ..models import DesignerMore, User


class UserSerializer(FlexFieldsModelSerializer):
    followers = serializers.PrimaryKeyRelatedField(
                queryset=User.objects.exclude(type="SYSTEM"),
                many=True,
                required=False
            )

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
            "liked_pictures",
            "liked_rooms",
            "followers",
            "following",
        )

        read_only_fields = (
            "id",
            "type",
            "date_joined",
            "liked_pictures",
            "liked_rooms",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        set the password manually ,
        or it will call model.objects.create() and store unhashed password

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
        fields = ("favorate_application", "tags")


class DesignerSerializer(UserSerializer, WritableNestedModelSerializer):
    designermore = DesignerMoreSerializer(required=True)

    class Meta(UserSerializer.Meta):
        """
        Meta options.

        Note: don't forget to learn how to inherit the fields of UserSerializer
        and *append* to the fields list without explicitly specifying each field
        that has been already declared in the UserSerializer
        """

        model = Designer
        fields = UserSerializer.Meta.fields + (
            "designermore",
        )
