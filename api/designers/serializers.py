from rest_framework import serializers
from accounts.models import User
from drf_dynamic_fields import DynamicFieldsMixin


class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "date_joined",
            "profile_picture",
            "discription",
        )
