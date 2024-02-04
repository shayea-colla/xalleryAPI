from django.test import TestCase, SimpleTestCase
from ..serializers import (
    UserSerializer,
    NormalUserSerializer,
    DesignerMoreSerializer,
    DesignerSerializer,
)
from accounts.models import User, DesignerMore
from accounts.profiles import NormalUser, Designer

from core.debug import debug


class TestUserSerializer(TestCase):
    def test_user_serializer_use_User_model(self):
        serializer = UserSerializer()
        self.assertEqual(serializer.Meta.model, User)

    def test_user_serializer_use_correct_fields(self):
        serializer = UserSerializer()
        fields = serializer.Meta.fields
        debug(fields)
        expected_fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "password",
            "email",
            "type",
            "discription",
            "date_joined",
            "liked_pictures",
            "liked_rooms",
        )
        self.assertEqual(fields, expected_fields)

    def test_user_serializer_read_only_fileds(self):
        serializer = UserSerializer()
        read_only_fields = serializer.Meta.read_only_fields
        expected_read_only_fields = (
            "id",
            "type",
            "date_joined",
            "liked_pictures",
            "liked_rooms",
        )
        self.assertEqual(read_only_fields, expected_read_only_fields)

    def test_user_serialzier_password_field_is_wirte_only(self):
        serializer = UserSerializer()
        write_only = serializer.fields.get("password").write_only
        self.assertTrue(write_only)

    def test_user_serializer_create_method_hashes_the_password_before_saving(self):
        # Data for test user
        test_user = {
            "username": "test_user",
            "password": "no way home",
            "discription": "test_user discription",
        }
        serializer = UserSerializer(data=test_user)

        # Assert serializer is valid
        self.assertTrue(serializer.is_valid())

        # Save the instance
        created_user = serializer.save()

        # Assert that serializer doesn't store UNHASHED passwords
        self.assertNotEqual(created_user.password, test_user["password"])


class TestNormalUserSerializer(TestCase):
    """Test Normal User Serializer and check if it is inheriting from the UserSerializer"""

    def test_normal_user_serializer_use_NormalUser_model(self):
        serializer = NormalUserSerializer()
        self.assertEqual(serializer.Meta.model, NormalUser)

    def test_user_serializer_use_correct_fields(self):
        serializer = UserSerializer()
        fields = serializer.Meta.fields
        expected_fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "password",
            "email",
            "type",
            "discription",
            "date_joined",
        )
        self.assertEqual(fields, expected_fields)

    def test_normal_user_serializer_read_only_fileds(self):
        serializer = UserSerializer()
        read_only_fields = serializer.Meta.read_only_fields
        expected_read_only_fields = (
            "id",
            "type",
            "date_joined",
        )
        self.assertEqual(read_only_fields, expected_read_only_fields)

    def test_normal_user_serialzier_password_field_is_wirte_only(self):
        serializer = UserSerializer()
        write_only = serializer.fields.get("password").write_only
        self.assertTrue(write_only)

    def test_normal_user_serializer_create_method_hashes_the_password_before_saving(
        self,
    ):
        # Data for test user
        test_user = {
            "username": "test_user",
            "password": "no way home",
            "discription": "test_user discription",
        }
        serializer = UserSerializer(data=test_user)

        # Assert serializer is valid
        self.assertTrue(serializer.is_valid())

        # Save the instance
        created_user = serializer.save()

        # Assert that serializer doesn't store UNHASHED passwords
        self.assertNotEqual(created_user.password, test_user["password"])


class TestDesignerMoreSerializer(SimpleTestCase):
    """Test DesignerMoreSerializer serializer class"""

    def test_designermore_serializer_use_DesignerMore_model(self):
        serializer = DesignerMoreSerializer()
        self.assertEqual(serializer.Meta.model, DesignerMore)

    def test_designermore_serializer_use_correct_fields(self):
        serializer = DesignerMoreSerializer()
        fields = serializer.Meta.fields
        expected_fields = (
            "favorate_application",
            "tags",
        )

        self.assertEqual(fields, expected_fields)

    #    def test_desigermore_serializer_favorate_application_field_type_is_CharField(self):
    #        serializer = DesignerMoreSerializer()
    #        favorate_application_field = serializer.get_fields().get("favorate_application")
    #        debug(dir(favorate_application_field))
    #        self.assertEqual(favorate_application_field, "char")

    def test_desigermore_serializer_favorate_application_field_max_length(self):
        serializer = DesignerMoreSerializer()
        favorate_application_field = serializer.get_fields().get("favorate_application")
        max_length = favorate_application_field.max_length
        self.assertEqual(max_length, 100)

    def test_desigermore_serializer_favorate_application_field_required_is_True(self):
        serializer = DesignerMoreSerializer()
        favorate_application_field = serializer.get_fields().get("favorate_application")
        required = favorate_application_field.required
        self.assertTrue(required)


class TestDesignerSerializer(TestCase):
    """Test DesignerSerializer serialzier class"""

    def test_designer_serializer_use_Designer_model(self):
        serializer = DesignerSerializer()
        self.assertEqual(serializer.Meta.model, Designer)

    def test_user_serializer_use_correct_fields(self):
        serializer = DesignerSerializer()
        fields = serializer.Meta.fields
        expected_fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "password",
            "email",
            "type",
            "discription",
            "date_joined",
            "designermore",
        )
        self.assertEqual(fields, expected_fields)
