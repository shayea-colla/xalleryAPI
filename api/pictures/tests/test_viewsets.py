import os
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from core.permissions import IsDesignerOrReadOnly, IsObjectOwnerOrReadOnly
from gallery.models import Picture
from django_filters.rest_framework import DjangoFilterBackend

from accounts.profiles import Designer, NormalUser
from gallery.models import Room
from core.debug import line, debug

from ..serializers import PictureSerializer

from ..viewsets import PictureViewSet


class TestPictureViewSet(TestCase):

    @classmethod
    def setUpTestData(self):
        """Creating rooms first"""
        # Creating two users
        self.test_designer = Designer.objects.create_user(
            username="test_designer", password="no way home"
        )

        self.test_normal = NormalUser.objects.create_user(
            username="test_normal", password="no way home"
        )

        # Get the image file path
        current_dir = os.getcwd()
        path = "static/test_image/image.jpg"
        self.filePath = os.path.join(current_dir, path)

        # Create First Room
        self.test_room = Room(
            name="test_room", owner=self.test_designer, discription="room num 1"
        )

        self.picture_form_data = SimpleUploadedFile(
            name=f"test_room_background_1.jpg",
            content=open(self.filePath, "rb").read(),
            content_type="image/jpg",
        )

        # Add the background field
        self.test_room.background = self.picture_form_data
        self.test_room.save()

        """Create picture"""
        self.test_pic = Picture()
        self.test_pic.image = self.picture_form_data
        self.test_pic.room = self.test_room
        self.test_pic.owner = self.test_designer
        self.test_pic.save()

        self.client = APIClient()

    def setUp(self):
        self.viewset = PictureViewSet()

    def test_viewset_queryset(self):
        self.assertQuerySetEqual(self.viewset.get_queryset(), Picture.objects.all())

    def test_viewset_serializer_class(self):
        self.assertEqual(self.viewset.serializer_class, PictureSerializer)

    def test_viewset_permission_classes(self):
        self.assertEqual(
            self.viewset.permission_classes,
            [IsDesignerOrReadOnly, IsObjectOwnerOrReadOnly],
        )

    def test_viewset_filter_backends(self):
        self.assertEqual(self.viewset.filter_backends, [DjangoFilterBackend])

    def test_viewset_filterset_fields(self):
        self.assertEqual(self.viewset.filterset_fields, ["room", "owner"])

    """Integerational Test TODO"""
    # def test_creating_pictures_by_designer(self):
    #     self.client.login(username="test_designer", password="no way home")

    #     line(open(self.filePath, "rb").read())

    #     result = self.client.post(
    #         reverse("picture-list"),
    #         {
    #             "room": self.test_room.id,
    #             "image": {
    #                 "name": "test_image.jpg",
    #                 "content": open(self.filePath, mode="rb").read(),
    #                 "content_type": "image/jpg",
    #             },
    #         },
    #     )

    #     debug(result.data)
