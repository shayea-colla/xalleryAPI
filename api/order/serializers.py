from rest_framework import serializers
from .models import Order
from drf_dynamic_fields import DynamicFieldsMixin

from accounts.api.serializers import UserSerializer


class OrderSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    """
    Main Serializer for Order model, modified the update method to only update the state of an order
    """

    # Set nested Serializer for the orderer so you can get more info about it when making requests, instead of making another request using the id provided by default,
    # set it to read_only and handle it in the view to reflect the requested user
    orderer = UserSerializer(read_only=True)

    def update(self, instance, validated_data):
        """
        Raise validationError if the state is not provided in partial update,
        """
        if "state" not in validated_data:
            raise serializers.ValidationError("you can only update the state field")

        # Only update the state no matter what the validated_data has
        instance.state = validated_data.get("state", instance.state)
        instance.save()
        return instance

    class Meta:
        model = Order
        fields = ["id", "state", "message", "orderer", "receiver", "date"]
