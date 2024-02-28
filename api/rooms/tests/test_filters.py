import os
import unittest
from unittest.mock import patch, Mock
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.filters import BaseFilterBackend
from rest_framework.test import APIRequestFactory
from django.db.models import Q  # Ensure compatibility with both Django versions
from django.test import TestCase
from api.rooms.utils import clean_tags
from core.debug import debug  # Assuming this is used for debugging, uncomment if needed

from gallery.models import Room  # Replace with your actual model name
from accounts.models import User
from api.tags.models import Tag

from ..filters import RoomTagsFilter
from ..viewsets import  RoomViewSet


class TestRoomTagsFilter(TestCase):

    def setUp(self):
        # Create test user
        user = User.objects.create_user(username="test_user", password="no way home")

        # Get the location of the test image used to test uploading images
        current_dir = os.getcwd()
        path = "static/test_image/image.jpg"
        filePath = os.path.join(current_dir, path)

        # Set the filter to be tested
        self.filter = RoomTagsFilter()

        # Set the rooms list
        self.rooms = []
        for i in range(3):
            self.rooms.append(
                Room.objects.create(
                    name=f"room_{i}",
                    owner=user,
                    background=SimpleUploadedFile(
                        name="test_room_background_1.jpg",
                        content=open(filePath, "rb").read(),
                        content_type="image/jpg",
                    ),
                    discription="test description",
                )
            )

        # Set the tags list
        tag1 = Tag.objects.create(name="tag1")
        tag2 = Tag.objects.create(name="tag2")
        tag3 = Tag.objects.create(name="tag3")

        # Add tags to rooms
        self.rooms[0].tags.add(tag1)
        self.rooms[1].tags.add(tag1, tag2)
        self.rooms[2].tags.add(tag1, tag2, tag3)

        self.factory = APIRequestFactory()
        # Intentially left like this, we don't want to create instance of the class we want the class itself
        self.view = RoomViewSet
        self.base_url = "/api/rooms/"
        self.queryset = Room.objects.all()


    def test_filter_queryset_empty_tags(self):
        request = Mock(query_params={"tags": ""})
        filtered_rooms = self.filter.filter_queryset(
            request, self.queryset , Mock()
        )

        self.assertEqual(filtered_rooms.count(), len(self.rooms))

    def test_filter_queryset_tag1(self):
        request = Mock(query_params={"tags": "tag1"})
        filtered_rooms = self.filter.filter_queryset(
            request, self.queryset , Mock()
        )

        self.assertEqual(filtered_rooms.count(), len(self.rooms))

    def test_filter_queryset_single_tag(self):
        request = Mock(query_params={"tags": "tag2"})
        filtered_rooms = self.filter.filter_queryset(
            request, Room.objects.all(), Mock()
        )
        self.assertEqual(filtered_rooms.count(), 2)  # Rooms with "tag1"
        self.assertQuerysetEqual(
            filtered_rooms, Room.objects.filter(Q(tags="tag2"))
        )
 
    def test_filter_queryset_multiple_tags(self):
        request = Mock(query_params={"tags": "tag2,tag3"})
        filtered_rooms = self.filter.filter_queryset(
            request, Room.objects.all(), Mock()
        )
        self.assertEqual(filtered_rooms.count(), 1)  # Room with "tag2" and "tag3"
        self.assertQuerysetEqual(filtered_rooms, Room.objects.filter(tags="tag2").filter(tags="tag3"))

    def test_filter_queryset_invalid_tags(self):
        request = Mock(query_params={"tags": "invalid_tag"})
        filtered_rooms = self.filter.filter_queryset(
            request, Room.objects.all(), Mock()
        )
        self.assertEqual(filtered_rooms.count(), 0)  # No tags match
