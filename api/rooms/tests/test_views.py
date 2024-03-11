import os
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from accounts.profiles import NormalUser, Designer
from api.pictures.views import LikePictureAPIView, UnLikePictureAPIView
from api.rooms.views import LikeRoomAPIView

from gallery.models import Picture, Room


class TestLikeRoomAPIView(TestCase):

    def setUp(self):
        """Create a few designers and nromal users"""

        self.designer = Designer.objects.create_user(
            username="test_designer",
            password="no way home",
            discription="test designer",
        )

        self.normal = NormalUser.objects.create_user(
            username="test_normal",
            password="no way home",
            discription="test normal",
        )

        self.test_room = Room.objects.create(
            name="test_room", discription="test discription", owner=self.designer
        )

        current_dir = os.getcwd()
        image_path = "static/test_image/image.jpg"
        path = os.path.join(current_dir, image_path)

        # Add the background field
        self.test_image = SimpleUploadedFile(
            name=f"test_room_background_1.jpg",
            content=open(path, "rb").read(),
            content_type="image/jpg",
        )
        self.test_room.background = self.test_image
        self.test_room.save()

        self.factory = APIRequestFactory()
        self.view = LikeRoomAPIView()
        self.client = APIClient()

    def test_permission_classes(self):
        """Test permission classess is AllowAny"""
        self.assertEqual(len(self.view.permission_classes), 1)
        permission_class = self.view.permission_classes[0]
        self.assertEqual(permission_class, IsAuthenticated)

    def test_view_reject_unauthorized_users(self):
        response = self.client.patch(reverse("like-picture", args=[self.test_room.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_view_does_not_accept_get_request(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.get(reverse("rooms:like", args=[self.test_room.id]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_post_request(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.post(reverse("rooms:like", args=[self.test_room.id]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_put_request(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.put(reverse("rooms:like", args=[self.test_room.id]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_delete_request(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.delete(reverse("rooms:like", args=[self.test_room.id]))
        self.assertTrue(response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_add_like_to_room(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.patch(reverse("rooms:like", args=[self.test_room.id]))
        self.assertEqual(self.test_room.likes.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)


class TestUnLikePictureAPIView(TestCase):

    def setUp(self):
        """Create a few designers and nromal users"""

        self.designer = Designer.objects.create_user(
            username="test_designer",
            password="no way home",
            discription="test designer",
        )

        self.normal = NormalUser.objects.create_user(
            username="test_normal",
            password="no way home",
            discription="test normal",
        )

        self.test_room = Room.objects.create(
            name="test_room", discription="test discription", owner=self.designer
        )

        current_dir = os.getcwd()
        image_path = "static/test_image/image.jpg"
        path = os.path.join(current_dir, image_path)

        # Add the background field
        self.test_image = SimpleUploadedFile(
            name=f"test_room_background_1.jpg",
            content=open(path, "rb").read(),
            content_type="image/jpg",
        )
        self.test_room.background = self.test_image
        self.test_room.save()

        self.factory = APIRequestFactory()
        self.view = UnLikePictureAPIView()
        self.client = APIClient()

    def test_permission_classes(self):
        """Test permission classess is AllowAny"""
        self.assertEqual(len(self.view.permission_classes), 1)
        permission_class = self.view.permission_classes[0]
        self.assertEqual(permission_class, IsAuthenticated)

    def test_view_reject_unauthorized_users(self):
        response = self.client.get(reverse("rooms:unlike", args=[self.test_room.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_view_does_not_accept_get_request(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.get(reverse("rooms:unlike", args=[self.test_room.id]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_post_request(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.post(reverse("rooms:unlike", args=[self.test_room.id]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_put_request(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.put(reverse("rooms:unlike", args=[self.test_room.id]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_delete_request(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.delete(reverse("rooms:unlike", args=[self.test_room.id]))
        self.assertTrue(response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_like_than_unlike_picture(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.patch(reverse("rooms:like", args=[self.test_room.id]))


        self.assertEqual(self.test_room.likes.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

        response = self.client.patch(reverse("rooms:unlike", args=[self.test_room.id]))

        self.assertEqual(self.test_room.likes.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
