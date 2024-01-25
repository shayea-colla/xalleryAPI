from rest_framework import serializers
from django.db import transaction
from drf_writable_nested.serializers import WritableNestedModelSerializer

from ..profiles import Designer, NormalUser
from ..models import DesignerMore, User

from gallery.utils import debug


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "type",
            "discription",
            "date_joined",
        )
        read_only_fields = ["date_joined", "type"]


class NormalUserSerializer(UserSerializer):
    """Normal User serializer ,

    Args:
        UserSerializer (serializers.ModelSerializer): inherit from the UserSerializer,
        change the model Meta attribute to  NormalUser
    """

    class Meta(UserSerializer.Meta):
        model = NormalUser


class DesignerMoreSerializer(serializers.ModelSerializer):
    favorate_application = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = DesignerMore
        fields = ["favorate_application"]


class DesignerSerializer(WritableNestedModelSerializer):
    designermore = DesignerMoreSerializer(required=True)

    class Meta:
        model = Designer
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "type",
            "date_joined",
            "discription",
            "designermore",
        )

        read_only_fields = ["id", "date_joined", "type"]
