from django.test import TestCase
from django.contrib.auth.models import Group
from accounts.models import User, DesignerMore
from accounts.profiles import Designer, NormalUser
from core.debug import debug


class TestDesignerManager(TestCase):
    """Test the desinger manager"""

    @classmethod
    def setUpTestData(self):
        """Create a bunch of designers and normal users"""
        # create the designers groups first
        Group.objects.create(name="designers")

        num_designers = 20
        num_normal = 10
        for i in range(num_designers):
            Designer.objects.create_user(username=f"test_designer {i}")

        for i in range(num_normal):
            NormalUser.objects.create_user(username=f"test_normal_user {i}")

    def test_get_queryset_returns_only_designers(self):
        # get queryset
        queryset = Designer.objects.all()
        # assert ther is only 20 designers
        self.assertEqual(len(queryset), 20)


class TestNormalUserManager(TestCase):
    """Test the desinger manager"""

    @classmethod
    def setUpTestData(self):
        """Create a bunch of designers and normal users"""
        # create the designers groups first
        Group.objects.create(name="designers")

        num_designers = 20
        num_normal = 10
        for i in range(num_designers):
            Designer.objects.create_user(username=f"test_designer {i}")

        for i in range(num_normal):
            NormalUser.objects.create_user(username=f"test_normal_user {i}")

    def test_get_queryset_returns_only_designers(self):
        # get queryset
        queryset = NormalUser.objects.all()
        # assert ther is only 20 designers
        self.assertEqual(len(queryset), 10)
