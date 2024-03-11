from django.shortcuts import render, get_object_or_404
from rest_flex_fields import FlexFieldsModelViewSet

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from gallery.models import Picture

from .serializers import PictureSerializer


# Create your views here.
class LikePictureAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk, *args, **kwargs):
        # Get the picture or raise NOT FOUND
        picture = get_object_or_404(Picture, pk=pk)

        # Get the authenticated user
        user = request.user

        # Add new like to the picture
        picture.likes.add(user)

        # serialize the data
        serializer = PictureSerializer(picture)

        # return successfull response
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)


like_picture_view = LikePictureAPIView.as_view()


class UnLikePictureAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk, *args, **kwargs):
        # Get the picture or raise NOT FOUND
        picture = get_object_or_404(Picture, pk=pk)

        # Get the authenticated user
        user = request.user

        # remove like from the picture
        picture.likes.remove(user)

        # serialize the data
        serializer = PictureSerializer(picture)

        # return successfull response
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)


unlike_picture_view = UnLikePictureAPIView.as_view()
