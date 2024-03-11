from django.test import TestCase
from django.contrib.auth.models import Group
from accounts.models import User, DesignerMore
from accounts.profiles import Designer

from django.core.files.uploadedfile import SimpleUploadedFile

from core.debug import debug, line

from ..models import Tag


class TestTagModel(TestCase):
    """Testing Tag model"""

    def setUp(self):
        # Create a test_user object
        num_tags = 20
        for i in range(num_tags):
            Tag.objects.create(name=f"tag_{i}")

        self.model = Tag

    def test_str_function(self):
        tag_name = "tag_1"
        tag = self.model.objects.get(name=tag_name)
        self.assertEqual(str(tag), tag_name)

    def test_name_filed_primary_key_is_true(self):
        primary_key = self.model._meta.get_field("name").primary_key
        self.assertTrue(primary_key)

    def test_name_filed_max_length(self):
        max_length = self.model._meta.get_field("name").max_length
        self.assertEqual(max_length, 150)

    def test_name_filed_unique_is_tru(self):
        unique = self.model._meta.get_field("name").unique
        self.assertTrue(unique)
