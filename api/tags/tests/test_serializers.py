from django.test import TestCase, SimpleTestCase
from accounts.api.serializers import (
    UserSerializer,
    NormalUserSerializer,
    DesignerMoreSerializer,
    DesignerSerializer,
)
from accounts.models import User, DesignerMore
from accounts.profiles import NormalUser, Designer
from api.rooms.serializers import RoomSerializer
from api.tags.models import Tag
from api.tags.serializers import TagSerializer

from core.debug import debug, line


class TestTagSerializer(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.serializer = TagSerializer
        return super().setUpTestData()

    def test_serializer_use_Tag_model(self):
        self.assertEqual(self.serializer.Meta.model, Tag)

    def test_serializer_use_correct_fields(self):
        fields = self.serializer.Meta.fields
        expected_fields = (
            "name",
            "rooms",
        )

        self.assertTupleEqual(fields, expected_fields)

    def test_serializer_read_only_fileds(self):
        read_only_fields = self.serializer.Meta.read_only_fields
        expected_read_only_fields = ("rooms",)
        self.assertTupleEqual(read_only_fields, expected_read_only_fields)

    def test_serializer_expandable_fields(self):
        expandable_fields = self.serializer.Meta.expandable_fields

        # Get the dictionary items
        field = expandable_fields.get("rooms")

        # Check if rooms exist
        self.assertFalse(field == None)
        self.assertEqual(field, (RoomSerializer, {"many": True}))
