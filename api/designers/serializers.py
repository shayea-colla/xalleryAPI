from rest_framework import serializers
from accounts.models import User
from drf_dynamic_fields import DynamicFieldsMixin
from django.db import transaction

from .models import Designer, DesignerMore

from gallery.utils import debug
from accounts.serializers import UserSerializer


class DesignerMoreSerializer(serializers.ModelSerializer):
    favorate_application = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = DesignerMore
        fields = ["favorate_application"]


class DesignerSerializer(serializers.ModelSerializer):
    more = DesignerMoreSerializer(required=True)

    class Meta:
        model = Designer
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "date_joined",
            "discription",
            "more",
        )

    @transaction.atomic
    def create(self, validated_data):
        more = validated_data.pop("more")
        designer = super().create(validated_data)
        favorate_application = more.pop("favorate_application")
        designer.save()
        DesignerMore.objects.create(
            user=designer, favorate_application=favorate_application
        )

        return designer
