from rest_framework import serializers
from accounts.models import User
from django.db import transaction
from drf_writable_nested.serializers import WritableNestedModelSerializer

from ..profiles import Designer, NormalUser
from ..models import DesignerMore

from gallery.utils import debug


class NormalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalUser
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "discription",
            "date_joined",
        )
        read_only_fields = ["date_joined"]


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
