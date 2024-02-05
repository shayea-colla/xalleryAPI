from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend

from core.permissions import IsAccountOwnerOrReadOnly

from ..models import User
from ..profiles import Designer, NormalUser
from .serializers import DesignerSerializer, NormalUserSerializer, UserSerializer
from .filters import AccountTagsFilter


class ListCreateAccountsAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    filter_backends = [AccountTagsFilter]

    def get_serializer_class(self, *args, **kwargs):
        """Return different serializers class based on the query params 'type'"""
        # Get the type url params
        type = self.request.query_params.get("type")

        # Check if provided
        if type is not None and type == "normal":
            # Return Normal User Serializer
            return NormalUserSerializer

        # Return DesignerSerializers by default
        return DesignerSerializer

    def get_queryset(self):
        """return differenct querysets based on the `?type` url parameter.

        if `?tyep=normal` included, return all Normal Users,
        otherwise return all Designers

        Returns:
            QuerySet: Django reqular QuerySet object
        """
        # Default value of the queyset
        queryset = Designer.objects.all()

        # Get the type url params
        type = self.request.query_params.get("type")

        # Check if type has value
        if type is not None and type == "normal":
            # Return normal users
            queryset = NormalUser.objects.all()

        # Return and filter queryset
        return self.filter_queryset(queryset)

list_create_accounts_view = ListCreateAccountsAPIView.as_view()

class RetrieveUpdateDestroyAccountAPIView(RetrieveUpdateDestroyAPIView):
    # queryset is all users except system users,
    # you can retrieve normal and designers from this queryset
    queryset = User.objects.exclude(type=User.Types.SYSTEM)
    permission_classes = [IsAccountOwnerOrReadOnly]

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

retrieve_update_destroy_account_view = RetrieveUpdateDestroyAccountAPIView.as_view()

class FollowUserAPIView(APIView):
    """API View enable any type of user to follow any type of user"""

    permission_classes = [IsAuthenticated]

    def patch(self, request, pk, *args, **kwargs):
        """add  the requesting user to the followers list of the target user"""
        # Get the Targe user
        user = get_object_or_404(User, pk=pk)

        # Get the requesting user
        follower = request.user

        # if user is trying to follow themselves
        if user == follower: 
            # return Forbidden response
            return Response(data={"detail":"you can not follow your self"}, status=status.HTTP_403_FORBIDDEN)

        # Else add the follower to the user followers
        user.followers.add(follower)

        # Serialize the user
        serializer = UserSerializer(user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


follow_user_view = FollowUserAPIView.as_view()


class UnFollowUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk, *args, **kwargs):
        """remove  the requesting user from the followers list of the target user"""
        # Get the Targe user
        user = get_object_or_404(User, pk=pk)

        # Get the requesting user
        follower = request.user

        # if user is trying to follow themselves
        if user == follower: 
            # return Forbidden response
            return Response(data={"detail":"you can not unfollow your self"}, status=status.HTTP_403_FORBIDDEN)

        # Else remove the follower from the user followers
        user.followers.remove(follower)

        # Serialize the user
        serializer = UserSerializer(user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


unfollow_user_view = UnFollowUserAPIView.as_view()
