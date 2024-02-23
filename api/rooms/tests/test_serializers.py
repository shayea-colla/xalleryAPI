from django.test import SimpleTestCase
from ..serializers import RoomSerializer
from gallery.models import Room
from accounts.api.serializers import DesignerSerializer

from core.debug import debug


class TestRoomSerializer(SimpleTestCase):

    def test_serializer_use_Room_model(self):
        serializer = RoomSerializer()
        self.assertEqual(serializer.Meta.model, Room)

    def test_serializer_use_correct_fields(self):
        serializer = RoomSerializer()
        fields = serializer.Meta.fields
        expected_fields = (
            "id",
            "name",
            "owner",
            "background",
            "discription",
            "created_at",
            "pictures",
            "tags",
            "likes",
        )
        # convert the fields into a set to ignore the order
        self.assertEqual(set(fields), set(expected_fields))

    def test_serializer_read_only_fileds(self):
        serializer = RoomSerializer()
        read_only_fields = serializer.Meta.read_only_fields
        expected_read_only_fields = (
            "owner",
            "pictures",
            "created_at",
        )

        # convert the fields into a set to ignore the order
        self.assertEqual(set(read_only_fields), set(expected_read_only_fields))

    def test_serializer_expandable_fileds(self):
        serializer = RoomSerializer()
        expandable_fields = serializer.Meta.expandable_fields

        # Get the dictionary items
        field = expandable_fields.get("owner")

        # Check if owner exist
        self.assertFalse(field == None)

        self.assertEqual(field, DesignerSerializer)


