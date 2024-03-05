import os
from rest_flex_fields import FlexFieldsModelSerializer
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from gallery.models import Picture
from unittest.mock import patch, Mock, MagicMock

from accounts.profiles import Designer
from gallery.models import Room
from core.debug import line, debug

from ..serializers import PictureSerializer



class TestPictureSerializerClass(TestCase):

    @classmethod
    def setUpTestData(self):
        # Creating two users
        test_user1 = Designer.objects.create_user(
            username="test_user1", password="test password"
        )

        test_user2 = Designer.objects.create_user(
            username="test_user2", password="test password"
        )

        # Get the image file path
        current_dir = os.getcwd()
        path = "static/test_image/image.jpg"
        filePath = os.path.join(current_dir, path)

        # Create First Room
        test_room = Room(name="test_room", owner=test_user1, discription="room num 1 owned by test_user1")

        # Add the background field
        test_room.background = SimpleUploadedFile(
            name=f"test_room_background_1.jpg",
            content=open(filePath, "rb").read(),
            content_type="image/jpg",
        )
        test_room.save()

    def setUp(self):
        self.correct_model = Picture
        self.serializer = PictureSerializer

    def test_serializer_uses_correct_model(self):
        model = self.serializer.Meta.model
        self.assertEqual(self.correct_model, model)

    def test_serializer_fields(self):
        fields = self.serializer.Meta.fields
        expected_fields = (
            "id",
            "owner",
            "image",
            "room",
            "likes",
        )

        self.assertEqual(set(fields), set(expected_fields))

    
    def test_serializer_read_only_fields(self):
        read_only_fields = self.serializer.Meta.read_only_fields
        expected_fields = (
            "owner",
        )

        self.assertEqual(set(read_only_fields), set(expected_fields))




#    def test_serializer_validate_room_method(self):
#        test_room = Room.objects.get(name="test_room")
#        room_owner = Designer.objects.get(username="test_user1")
#        not_room_owner = Designer.objects.get(username="test_user2")
#
#        mock_self = MagicMock(spec=FlexFieldsModelSerializer,
#            context={
#                "request": Mock(user=room_owner)
#            }
#        )
#
#        line(self.serializer.validate_room(mock_self, test_room))

