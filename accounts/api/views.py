from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from core.permissions import IsAccountOwnerOrReadOnly

from ..models import User
from ..profiles import Designer, NormalUser

from .serializers import DesignerSerializer, NormalUserSerializer, UserSerializer


class ListCreateAccounts(ListCreateAPIView):
    permission_classes = [AllowAny]

    def get_serializer_class(self, *args, **kwargs):
        """Return different serializers class based on the query params 'type'"""
        if (
            "type" in self.request.query_params
            and self.request.query_params["type"] == "normal"
        ):
            # Return Normal User Serializer
            return NormalUserSerializer

        # Return DesignerSerializers
        return DesignerSerializer

    def get_queryset(self):
        """if `?tyep=normal` included, return all Normal Users,
           otherwise return all Designers

        Returns:
            QuerySet: Django reqular QuerySet object
        """
        if (
            "type" in self.request.query_params
            and self.request.query_params["type"] == "normal"
        ):
            return NormalUser.objects.all()

        # Return all Designers By default
        return Designer.objects.all()


class RetrieveUpdateDestroyAccountAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.exclude(type=User.Types.SYSTEM)
    permission_classes = [IsAccountOwnerOrReadOnly]
    lookup_field = "username"

    def get_serializer_class(self):
        """Dynamically return the serializer class based on the user type"""
        # get the user
        user = self.get_object()

        # return serializer based on type
        if user.type == User.Types.DESIGNER:
            return DesignerSerializer
        elif user.type == User.Types.NORMAL:
            return NormalUserSerializer

        # Return default User serializer if the user doesn't belone to either types
        return UserSerializer
