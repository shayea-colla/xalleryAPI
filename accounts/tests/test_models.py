from django.test import TestCase
from django.contrib.auth.models import Group
from accounts.models import User, DesignerMore
from accounts.profiles import Designer

from django.core.files.uploadedfile import SimpleUploadedFile

from core.debug import debug


class TestUserModel(TestCase):
    """
    Testing my custom fields
    in the User object

    Testing area:
        _discription:
            - max_length = 1000
            - help_text = 'Write a short bio about yourself ( optional )

        _ picture
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

    def test_discription_blank_is_false(self):
        user = User.objects.get(username="test_user")
        blank = user._meta.get_field("discription").blank
        self.assertFalse(blank)

    """
        Testing profile_picture:

            _ profile_picture
                - upload_to = 'profile/'
                - null = True
    """

    def test_picture_field_label(self):
        user = User.objects.get(username="test_user")
        field_label = user._meta.get_field("picture").verbose_name
        self.assertEqual(field_label, "Profile picture")

    def test_picture_uplaod_to(self):
        user = User.objects.get(username="test_user")
        upload_to = user._meta.get_field("picture").upload_to
        self.assertEqual(upload_to, "profiles/")

    def test_profile_picture_null(self):
        user = User.objects.get(username="test_user")
        null = user._meta.get_field("picture").null
        self.assertTrue(null)

    def test_profile_picture_blank_is_True(self):
        user = User.objects.get(username="test_user")
        blank = user._meta.get_field("picture").blank
        self.assertTrue(blank)

    def test_type_field_max_length(self):
        user = User.objects.get(username="test_user")
        max_length = user._meta.get_field("type").max_length
        self.assertEqual(max_length, 50)

    def test_type_field_choices(self):
        user = User.objects.get(username="test_user")
        choices = user._meta.get_field("type").choices
        self.assertEqual(choices, User.Types.choices)

    def test_type_field_choices_default_value(self):
        user = User.objects.get(username="test_user")
        default = user._meta.get_field("type").default
        self.assertEqual(default, User.Types.NORMAL)

    def test_birth_date_field_auto_now_is_false(self):
        user = User.objects.get(username="test_user")
        auto_now = user._meta.get_field("birth_date").auto_now
        self.assertFalse(auto_now)

    def test_birth_date_field_auto_now_add_is_false(self):
        user = User.objects.get(username="test_user")
        auto_now_add = user._meta.get_field("birth_date").auto_now_add
        self.assertFalse(auto_now_add)

    def test_birth_date_field_null_attribute_is_True(self):
        user = User.objects.get(username="test_user")
        null = user._meta.get_field("birth_date").null
        self.assertTrue(null)

    def test_base_type_attribute_is_system(self):
        user = User.objects.get(username="test_user")
        base_type = user.base_type
        self.assertEqual(base_type, User.Types.SYSTEM)

    def test_save_method_assign_base_type_to_types_field_when_saving(self):
        """
        Testing that save method is assigning the types field based on
        the base_type field defined in the model direcly regarding the defualt value
        """
        user = User.objects.create_user(username="solo", password="no way home ")
        self.assertEqual(user.type, User.Types.SYSTEM)

    def test_system_user_does_not_have_designermore_object(self):
        user = User.objects.get(username="test_user")
        self.assertFalse(user in DesignerMore.objects.all())


class TestDesignerMore(TestCase):
    """Testing DesignerMore model"""

    @classmethod
    def setUpTestData(self):
        """Create desingers group"""
        Group.objects.create(name="designers")

    def setUp(self):
        """
        Create a few designermore instances
        by creating a designer you are implicitly creating a desingermore instance via signals
        """

        # Create Designer and designermore will be automatically assigned to it
        designer = Designer.objects.create_user(
            username="test_designer", password="no way home "
        )
        DesignerMore.objects.create(user=designer, favorate_application="Vim")

    def test_designermore_favorate_application_max_length_attribute(self):
        designermore = DesignerMore.objects.get(
            user=Designer.objects.get(username="test_designer")
        )
        max_length = designermore._meta.get_field("favorate_application").max_length
        self.assertEqual(max_length, 100)

    def test_designermore_favorate_application_null_attribute_is_false(self):
        designermore = DesignerMore.objects.get(
            user=Designer.objects.get(username="test_designer")
        )
        null = designermore._meta.get_field("favorate_application").null
        self.assertFalse(null)

    def test_designermore_favorate_application_blank_attribute_is_false(self):
        designermore = DesignerMore.objects.get(
            user=Designer.objects.get(username="test_designer")
        )
        blank = designermore._meta.get_field("favorate_application").blank
        self.assertFalse(blank)

    def test_designermore_tags_field_verbose_name(self):
        designermore = DesignerMore.objects.get(
            user=Designer.objects.get(username="test_designer")
        )
        verbose_name = designermore._meta.get_field("tags").verbose_name
        self.assertEqual(verbose_name, "Tags")

    def test_designermore_tags_field_related_name(self):
        designermore = DesignerMore.objects.get(
            user=Designer.objects.get(username="test_designer")
        )

        related_name = designermore._meta.get_field("tags").related_query_name()
        self.assertEqual(related_name, "designers")

    def test_designermore_str_method(self):
        designermore = DesignerMore.objects.get(
            user=Designer.objects.get(username="test_designer")
        )
        self.assertEqual(
            str(designermore), f"designermore: {designermore.user.username}"
        )
