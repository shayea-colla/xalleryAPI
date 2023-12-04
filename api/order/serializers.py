from rest_framework import serializers
from .models import Order
from gallery.utils import debug
from accounts.models import User


class OrderSerializer(serializers.ModelSerializer):
    """
    Main Serializer for Order model, modified the update method to only update the state of an order
    """
    def update(self, instance, validated_data):
        """
        Raise validationError if the state is not provided in partial update,

        """
        if 'state' not in validated_data:
            raise serializers.ValidationError('you can only update the state field')


        # Only update the state no matter what the validated_data has
        instance.state = validated_data.get('state', instance.state)
        instance.save()
        return instance

    class Meta:
        model = Order
        fields = ['id','state', 'message','orderer','receiver', 'date']

