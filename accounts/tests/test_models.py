from django.test import TestCase
from accounts.models import User

from django.core.files.uploadedfile import SimpleUploadedFile


class TestUserModel(TestCase):
    """
    Testing my custom fields
    in the User object

    Testing area:
        _discription:
            - max_length = 1000
            - help_text = 'Write a short bio about yourself ( optional )

        _ profile_picture
            - upload_to = 'profile/'
            - null = True
    """

    def setUp(self):
        # Create a test_user object
        User.objects.create_user(
            username="test_user",
            password="no way home",
        )

    """
        Testing description field:
            - max_length = 1000
            - help_text = 'Write a short bio about yourself ( optional )
    """

    def test_get_absolute_url_function(self):
        user = User.objects.get(username="test_user")
        self.assertEqual(user.get_absolute_url(), f"/accounts/{user.pk}/")

    def test_description_field_label(self):
        user = User.objects.get(username="test_user")
        field_label = user._meta.get_field("discription").verbose_name
        self.assertEqual(field_label, "discription")

    def test_description_max_length(self):
        user = User.objects.get(username="test_user")
        max_length = user._meta.get_field("discription").max_length
        self.assertEqual(max_length, 1000)

    def test_description_help_text(self):
        user = User.objects.get(username="test_user")
        help_text = user._meta.get_field("discription").help_text
        self.assertEqual(help_text, "Write a short bio about yourself ( required )")

    """
        Testing profile_picture:

            _ profile_picture
                - upload_to = 'profile/'
                - null = True
    """

    def test_profile_picture_field_label(self):
        user = User.objects.get(username="test_user")
        field_label = user._meta.get_field("profile_picture").verbose_name
        self.assertEqual(field_label, "profile picture")

    def test_profile_picture_uplaod_to(self):
        user = User.objects.get(username="test_user")
        upload_to = user._meta.get_field("profile_picture").upload_to
        self.assertEqual(upload_to, "profiles/")

    def test_profile_picture_null(self):
        user = User.objects.get(username="test_user")
        null = user._meta.get_field("profile_picture").upload_to
        self.assertTrue(null)
