from django.test import TestCase
from django.contrib.auth.models import Group
from unittest.mock import Mock

from accounts.models import User
from ..utils import is_designer, is_owner

from core.debug import line, debug


class TestUtilsModule(TestCase):

    @classmethod
    def setUpTestData(self) -> None:
        # create a designer group
        designer_group = Group.objects.create(name="designers")

        # create  one user and add it to the designer group
        user_designer = User.objects.create_user(
            username="test_user_in_designer_group", password="test passwrod"
        )

        user_designer.groups.add(designer_group)
        self.user_in_designer_group = user_designer

        self.test_user1: User = User.objects.create_user(
            username="test_user1", password="test passwrod"
        )

        self.test_user2: User = User.objects.create_user(
            username="test_user2", password="test passwrod"
        )

    def test_is_designer_returns_true_for_user_in_designer_group(self):
        self.assertTrue(is_designer(self.user_in_designer_group))

    def test_is_designer_returns_false_for_users_not_in_designer_group(self):
        self.assertFalse(is_designer(self.test_user1))

    def test_is_owner_returns_true_if_owner_match_the_user_provided(self):
        obj = Mock(owner=self.test_user1)
        self.assertTrue(is_owner(self.test_user1, obj))

    def test_is_owner_returns_false_if_owner_does_not_match_the_user_provided(self):
        obj = Mock(owner=self.test_user1)
        self.assertFalse(is_owner(self.test_user2, obj))
