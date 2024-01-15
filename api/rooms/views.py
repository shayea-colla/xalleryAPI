from django.shortcuts import render

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    DjangoModelPermissionsOrAnonReadOnly,
)

from gallery.models import Room
from .serializers import RoomSerializer
from .permissions import IsRoomOwnerOrReadOnly

# Create your views here.


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsRoomOwnerOrReadOnly, DjangoModelPermissionsOrAnonReadOnly]

    def create(self, request):
        """
        Create new room and assign the room owner to the current user
        """

        # Get the serializer class 
        serializer_class = self.get_serializer_class()

        # serialize the data
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            # Set the owner to the current user, no matter what provided in the request data
            serializer.validated_data["owner"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            # Return Bad request response with erorrs
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
