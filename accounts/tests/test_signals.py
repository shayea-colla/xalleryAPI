from django.test import TestCase
from django.contrib.auth.models import Group
from accounts.models import User, DesignerMore
from accounts.profiles import Designer, NormalUser
from core.debug import debug


class TestAssignDesignersGroupSignal(TestCase):
    """
    Testing assigning designers to the designers groups
    whenever a new `Designer` is created via the Designer proxy model
    """

    def setUp(self):
        """Create the designers groups"""
        Group.objects.create(name="designers")

    def test_designers_assigned_to_designers_group_once_they_created(self):
        designer = Designer.objects.create_user(username="designer")
        designers_group = Group.objects.get(name="designers")
        self.assertTrue(designers_group in designer.groups.all())

    def test_normal_users_do_not_assigned_to_designers_group_once_they_created(self):
        normal_user = NormalUser.objects.create_user(username="normal_user")
        designers_group = Group.objects.get(name="designers")
        self.assertFalse(designers_group in normal_user.groups.all())
