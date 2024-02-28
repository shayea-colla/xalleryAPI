from .serializers import (
    DesignerSerializer,
    NormalUserSerializer,
    UserSerializer,
)

from ..models import User


class DynamicSerializerClassMixin:

    def get_serializer_class(self):
        """Dynamically return the serializer class based on the user type"""
        # get the user
        user = self.get_object()

        # return serializer based on type
        if user.type == User.Types.DESIGNER:
            return DesignerSerializer
        elif user.type == User.Types.NORMAL:
            return NormalUserSerializer

        # Return default User serializer if the user doesn't belong to either types
        return UserSerializer
