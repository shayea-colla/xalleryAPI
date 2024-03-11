from unittest.mock import Mock
from django.test import SimpleTestCase
from core.mixins import SetOwnerTheCurrentUserMixin


# class TestMock(SetOwnerTheCurrentUserMixin):

#     def create(self, **kwargs):
#         line("super")
#         return super().create({})


# class TestSetOwnerTheCurrentUserMixin(SimpleTestCase):

#     def setUp(self):
#         self.mixin = SetOwnerTheCurrentUserMixin

#     def test_create_method(self):
#         context = Mock({"request": Mock()})
#         context.get("request").user = "user"
#         self.context = context
#         value = self.mixin.create(self, {})
#         self.assertEqual(value.get("owner"), "user")


class TestSetOwnerTheCurrentUserMixin(SimpleTestCase):

    def setUp(self):
        self.validated_data = {"name": "Test Object", "description": "For testing"}
        self.mock_user = Mock(id=123)  # Simulate a user with an ID

    def test_create_sets_owner(self):
        mixin = SetOwnerTheCurrentUserMixin()

        mock_request = Mock()  # Create a mock request object
        mock_request.user = self.mock_user
        mixin.context = {"request": mock_request}

        result = mixin.create(self.validated_data)

        self.assertEqual(result["owner"], self.mock_user)
