from django.shortcuts import get_object_or_404
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from gallery.models import Room
from core.debug import debug

from .serializers import RoomSerializer


class LikeRoom(APIView):
    """View that enable the current authenticated user to like the requesed room"""

    permission_classes = [IsAuthenticated]

    def patch(self, request, pk, *args, **kwargs):
        # Get the room ro raise NOT FOUND
        room = get_object_or_404(Room, pk=pk)

        # Get the authenticated user
        user = request.user

        # add user to likes
        room.likes.add(user)
        # add serialized room data to the data
        serializer = RoomSerializer(room)

        # return successfull message indicate updating
        return Response(data=serializer.data, status=status.HTTP_200_OK)


like_room_view = LikeRoom.as_view()


class UnLikeRoom(APIView):
    """View that enable the current authenticated user to unlike the requesed room"""

    permission_classes = [IsAuthenticated]

    def patch(self, request, pk, *args, **kwargs):
        # Get the room ro raise NOT FOUND
        room = get_object_or_404(Room, pk=pk)

        # Get the authenticated user
        user = request.user

        # remove user from likes
        room.likes.remove(user)

        # serialize the room
        serializer = RoomSerializer(room)

        # return successfull message indicate updating
        return Response(data=serializer.data, status=status.HTTP_200_OK)


unlike_room_view = UnLikeRoom.as_view()
