import os
import unittest
from unittest.mock import patch, Mock

from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.filters import BaseFilterBackend
from django.db.models import Q  # Ensure compatibility with both Django versions
from django.test import TestCase
from api.rooms.utils import clean_tags
from core.debug import debug  # Assuming this is used for debugging, uncomment if needed

from gallery.models import Room  # Replace with your actual model name
from accounts.models import User
from api.tags.models import Tag

from ..filters import RoomTagsFilter


class RoomTagsFilterTest(TestCase):

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
        self.tags = []
        for i in range(3):
            self.tags.append(
                Tag.objects.create(
                    name=f"tag{i}",
                )
            )

        # Add tags to rooms
        self.rooms[0].tags.add(self.tags[0])
        self.rooms[0].tags.add(self.tags[0], self.tags[1])
        self.rooms[0].tags.add(self.tags[0], self.tags[1], self.tags[2])


#    def test_filter_queryset_empty_tags(self):
#        request = Mock(query_params={})
#        filtered_rooms = self.filter.filter_queryset(
#            request, Room.objects.all(), Mock()
#        )
#        self.assertEqual(filtered_rooms.count(), len(self.rooms))
#
#    def test_filter_queryset_single_tag(self):
#        request = Mock(query_params={"tags": "tag1"})
#        filtered_rooms = self.filter.filter_queryset(
#            request, Room.objects.all(), Mock()
#        )
#        self.assertEqual(filtered_rooms.count(), 2)  # Rooms with "tag1"
#        self.assertQuerysetEqual(
#            filtered_rooms, Room.objects.filter(Q(tags="tag1") | Q(tags="tag1,tag4"))
#        )
#
#    def test_filter_queryset_multiple_tags(self):
#        request = Mock(query_params={"tags": "tag2,tag3"})
#        filtered_rooms = self.filter.filter_queryset(
#            request, Room.objects.all(), Mock()
#        )
#        self.assertEqual(filtered_rooms.count(), 1)  # Room with "tag2"
#        self.assertQuerysetEqual(filtered_rooms, Room.objects.filter(tags="tag2"))
#
#    def test_filter_queryset_invalid_tags(self):
#        request = Mock(query_params={"tags": "invalid_tag"})
#        filtered_rooms = self.filter.filter_queryset(
#            request, Room.objects.all(), Mock()
#        )
#        self.assertEqual(filtered_rooms.count(), 0)  # No tags match
#
#    @patch("api.rooms.utils.clean_tags")
#    def test_filter_queryset_clean_tags(self, mock_clean_tags):
#        mock_clean_tags.return_value = ["cleaned_tag1"]
#        request = Mock(query_params={"tags": "tag1,   extra_spaces"})
#        filtered_rooms = self.filter.filter_queryset(
#            request, Room.objects.all(), Mock()
#        )
#        mock_clean_tags.assert_called_once_with(["tag1", ",  extra_spaces"])
#        self.assertEqual(filtered_rooms.count(), 2)  # Rooms with "cleaned_tag1"
#        self.assertQuerysetEqual(
#            filtered_rooms,
#            Room.objects.filter(Q(tags="cleaned_tag1") | Q(tags="cleaned_tag1,tag4")),
#        )
#
#
# if __name__ == "__main__":
#    unittest.main()
