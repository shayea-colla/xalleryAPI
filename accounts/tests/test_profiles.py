from django.test import TestCase
from django.contrib.auth.models import Group
from django.core.files.uploadedfile import SimpleUploadedFile

from ..models import User, DesignerMore
from ..profiles import Designer, NormalUser
from ..managers import DesignerManager, NormalUserManager

from core.debug import debug


class TestDesignerProfile(TestCase):
    def test_Designer_profile_base_type(self):
        base_type = Designer.base_type
        self.assertEqual(base_type, User.Types.DESIGNER)

    def test_Designer_profile_Meta_attribute_proxy(self):
        proxy = Designer._meta.proxy
        self.assertTrue(proxy)

    def test_Designer_profile_objects_manager(self):
        # Get the objects manager int he designer
        objects = Designer.objects
        # Get the expected manager
        manager = DesignerManager()
        # Assert both are equal
        self.assertEqual(objects, manager)


class TestNormalUserProfile(TestCase):
    def test_NormalUser_profile_base_type(self):
        base_type = NormalUser.base_type
        self.assertEqual(base_type, User.Types.NORMAL)

    def test_NormalUser_profile_Meta_attribute_proxy(self):
        proxy = NormalUser._meta.proxy
        self.assertTrue(proxy)

    def test_NormalUser_profile_objects_manager(self):
        # Get the objects manager
        objects = NormalUser.objects
        # Get the expected manager
        manager = NormalUserManager()
        # Assert both are equal
        self.assertEqual(objects, manager)
