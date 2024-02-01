import uuid
import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from gallery.utils import debug

from gallery.models import Room, Picture
from gallery.forms import CreateRoomForm
from accounts.models import User


class TestDeleteRoomView(TestCase):
    """NOTCOMP"""

    def setUp(self):
        user_1 = User.objects.create_user(username="user_1", password="no way home")

        user_2 = User.objects.create_user(username="user_2", password="no way home")

        # Get the location of the test image
        # used to test uploading images
        current_dir = os.getcwd()
        path = "static/test_image/image.jpg"
        filePath = os.path.join(current_dir, path)

        # Create two rooms
        room_1 = Room.objects.create(
            name="room_1",
            owner=user_1,
            background=SimpleUploadedFile(
                name="test_room_background_1.jpg",
                content=open(filePath, "rb").read(),
                content_type="image/jpg",
            ),
            discription="",
        )
        room_2 = Room.objects.create(
            name="room_2",
            owner=user_1,
            background=SimpleUploadedFile(
                name="test_room_background_2.jpg",
                content=open(filePath, "rb").read(),
                content_type="image/jpg",
            ),
            discription="no way home",
        )

        # Upload a few pictures.
        num_pictures = 20
        for i in range(num_pictures):
            Picture.objects.create(
                image=SimpleUploadedFile(
                    name=f"test_image_{1}.jpg",
                    content=open(filePath, "rb").read(),
                    content_type="image/jpg",
                ),
                room=room_1 if i % 2 else room_2,
            )

    def test_pass_test_func(self):
        room = Room.objects.get(name="room_1")
        self.client.login(username="user_1", password="no way home")

        res = self.client.post(f"/gallery/room/{room.id}/delete", follow=True)

        self.assertEqual(res.status_code, 201)


# class TestDeletePictureView(TestCase):
#    TODO
#    ...
