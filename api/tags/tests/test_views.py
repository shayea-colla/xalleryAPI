import os
import stat
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from accounts.profiles import NormalUser, Designer
from api.pictures.views import UnLikePictureAPIView
from api.tags.models import Tag
from api.tags.serializers import TagSerializer
from api.tags.views import CreateTagsAPIView, ListTagsAPIView
from core import debug
from core.permissions import IsDesigner

from gallery.models import Picture, Room


class TestListTagsAPIView(TestCase):

    def setUp(self):

        num_tags = 20
        self.tags = []
        for i in range(num_tags):
            self.tags.append(Tag.objects.create(name=f"tag_{i}"))

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

        self.view = ListTagsAPIView()
        self.client = APIClient()
        self.model = Tag

    def test_permission_classes(self):
        """Test permission classess is AllowAny"""

        self.assertEqual(len(self.view.permission_classes), 1)
        permission_class = self.view.permission_classes[0]
        self.assertEqual(permission_class, AllowAny)

    def test_permit_list_expands(self):
        """Test permit_list_expands belong to FlexFieldsSerializer and expandable fields"""
        permit_list = self.view.permit_list_expands
        self.assertEqual(permit_list, ["rooms"])

    def test_serializer_class(self):
        serializer_class = self.view.serializer_class
        self.assertEqual(serializer_class, TagSerializer)

    # Fixme
    # def test_queryset(self):
    #     queryset = self.view.get_queryset()
    #     self.assertEquals(queryset, Tag.objects.all())

    def test_view_accept_get_request(self):
        response = self.client.get(reverse("tags:list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_does_not_accept_post_request(self):
        response = self.client.post(reverse("tags:list"))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_put_request(self):
        response = self.client.put(reverse("tags:list"))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_delete_request(self):
        response = self.client.delete(reverse("tags:list"))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_returns_all_tags(self):
        response = self.client.get(reverse("tags:list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), len(self.tags))


class TestCreateTagsAPIView(TestCase):

    def setUp(self):

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

        self.view = CreateTagsAPIView()
        self.client = APIClient()
        self.model = Tag

    def test_permission_classes(self):
        """Test permission classess is AllowAny"""

        self.assertEqual(len(self.view.permission_classes), 1)
        permission_class = self.view.permission_classes[0]
        self.assertEqual(permission_class, IsDesigner)

    def test_serializer_class(self):
        serializer_class = self.view.serializer_class
        self.assertEqual(serializer_class, TagSerializer)

    # Fixme
    # def test_queryset(self):
    #     queryset = self.view.get_queryset()
    #     self.assertEquals(queryset, Tag.objects.all())

    def test_view_reject_unauthorized_users(self):
        response = self.client.post(reverse("tags:create"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_view_reject_normal_users(self):
        self.client.login(username="test_normal", password="no way home")
        response = self.client.post(reverse("tags:create"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_view_deos_not_accept_get_request(self):
        self.client.login(username="test_designer", password="no way home")
        response = self.client.get(reverse("tags:create"))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_put_request(self):
        self.client.login(username="test_designer", password="no way home")
        response = self.client.put(reverse("tags:create"))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_view_does_not_accept_delete_request(self):
        self.client.login(username="test_designer", password="no way home")
        response = self.client.delete(reverse("tags:create"))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_create_tag_by_designer(self):
        self.client.login(username="test_designer", password="no way home")
        response = self.client.post(reverse("tags:create"), {"name": "test_tag"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Tag.objects.all().count(), 1)
