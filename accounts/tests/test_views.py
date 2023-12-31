from django import test
from django.urls import reverse
from django.contrib.auth.models import Group

from accounts.models import User
from accounts.forms import CreateUserForm
from gallery.models import Room


class TestProfileView(test.TestCase):
    @classmethod
    def setUpTestData(self):
        # Create a test user
        user1 = User.objects.create_user(username="test_user_1", password="no way home")
        user2 = User.objects.create_user(username="test_user_2", password="no way home")

        # Create a tow rooms owned by 'test_user_1'
        Room.objects.create(
            name="test_room1",
            owner=user1,
        )
        Room.objects.create(
            name="test_room2",
            owner=user2,
        )

    def test_view_url_exists_at_desired_location(self):
        # Get testUser
        testUser = User.objects.get(username="test_user_1")

        res = self.client.get(f"/accounts/{testUser.pk}/")
        self.assertEqual(res.status_code, 200)

    def test_view_accessible_by_name(self):
        # Get testUser
        testUser = User.objects.get(username="test_user_1")

        res = self.client.get(reverse("profile", args=[testUser.pk]))
        self.assertEqual(res.status_code, 200)

    def test_view_uses_the_correct_template(self):
        testUser = User.objects.get(username="test_user_1")
        res = self.client.get(reverse("profile", args=[testUser.pk]))

        # Assertions
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "registration/profile.html")

    def test_view_display_the_correct_user(self):
        testUser = User.objects.get(username="test_user_1")
        res = self.client.get(reverse("profile", args=[testUser.pk]))

        # Assertions
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context["user"], testUser)


class TestEditProfileView(test.TestCase):
    pass


class TestCreateUserView(test.TestCase):
    """
    Testing  the function-based view named 'add_user'

    #Testing_paths:
        @ initial_display:
            #Testing_area:
               __url_test:
                    location: '/accounts/add/'
                    name: 'create_user'

               __template_name:
                    'registration/create_user_form.html'

               __form_class:
                   CreateUserForm()

               __context_variable_passed:
                    'form' (only one variable passed)



        @after_submition:

            case 'valid_data':
                __add_new_user_with_the_same_data_submitted
                __assign_new_user_to_designers_group
                __login_new_user
                __redirect_to_user_profile_page

            case 'invalid_data':
                __rerender_the_same_template_with_error_messages

    *Note:
        You will need setUpTestData to only create the designers group
    """

    @classmethod
    def setUpTestData(self):
        # Create the designers group
        designersGroup = Group.objects.create(name="designers")
        designersGroup.save()

    # Initial Display
    def test_view_exist_at_desired_location(self):
        res = self.client.get("/accounts/add/")

        self.assertEqual(res.status_code, 200)

    def test_veiw_accessible_by_name(self):
        res = self.client.get(reverse("create-user"))

        self.assertEqual(res.status_code, 200)

    def test_correct_template_used(self):
        res = self.client.get(reverse("create-user"))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "registration/create_user_form.html")

    def test_correct_form_class_used(self):
        res = self.client.get(reverse("create-user"))
        correct_form = CreateUserForm()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(str(res.context["form"]), str(correct_form))

    """ After submition """

    # Valid Data
    def test_creating_user_when_submitting_valid_data(self):
        # Generate a valid testing data
        data = {
            "first_name": "test",
            "last_name": "user",
            "username": "test_user",
            "email": "testuser@shayea.com",
            "discription": "short bio",
            "password": "no way home",
        }

        # submit the form
        res = self.client.post("/accounts/add/", data)

        # Assert Creating a user
        try:
            test_user = User.objects.get(username="test_user")
        except:
            test_user = False
        self.assertTrue(bool(test_user))

    def test_assigning_user_to_designers_group_when_submitting_valid_data(self):
        data = {
            "first_name": "test",
            "last_name": "user",
            "username": "test_user",
            "email": "testuser@shayea.com",
            "discription": "short bio",
            "password": "no way home",
        }

        # submit the form
        res = self.client.post("/accounts/add/", data)

        try:
            test_user = User.objects.get(username="test_user")
        except:
            test_user = False

        # Assert assigning the user to only designers group
        self.assertEqual(len(test_user.groups.all()), 1)
        self.assertTrue(bool(test_user.groups.get(name="designers")))

    def test_authenticating_user_after_submitting_valid_data(self):
        data = {
            "first_name": "test",
            "last_name": "user",
            "username": "test_user",
            "email": "testuser@shayea.com",
            "discription": "short bio",
            "password": "no way home",
        }

        # submit the form
        res = self.client.post("/accounts/add/", data)

        try:
            test_user = User.objects.get(username="test_user")
        except:
            test_user = False

        self.assertTrue(bool(test_user))

        self.assertTrue(test_user.is_authenticated)

    def test_redirection_when_submitting_valid_data(self):
        data = {
            "first_name": "test",
            "last_name": "user",
            "username": "test_user",
            "email": "testuser@shayea.com",
            "discription": "short bio",
            "password": "no way home",
        }

        # submit the form
        res = self.client.post("/accounts/add/", data)

        try:
            test_user = User.objects.get(username="test_user")
        except:
            test_user = False
        self.assertTrue(bool(test_user))

        # Assert redirection
        self.assertEqual(res.status_code, 302)

    # Invalid Data
    def test_submitting_invalid_usernamea(self):
        data = {"username": "", "password": "nowayhome"}

        # submit the form
        res = self.client.post("/accounts/add/", data)
        self.assertFormError(res, "form", "username", "This field is required.")

    def test_submitting_invalid_password(self):
        data = {"username": "test_username:", "password": ""}

        # submit the form
        res = self.client.post("/accounts/add/", data)
        self.assertFormError(res, "form", "password", "This field is required.")
