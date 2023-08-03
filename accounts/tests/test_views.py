from django import test
from django.urls import reverse
from accounts.models import User
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

        res = self.client.get(f"/accounts/{testUser.username}/")
        self.assertEqual(res.status_code, 200)

    def test_view_accessible_by_name(self):
        # Get testUser
        testUser = User.objects.get(username="test_user_1")

        res = self.client.get(reverse("profile", args=[testUser.username]))
        self.assertEqual(res.status_code, 200)

    def test_view_uses_the_correct_template(self):
        testUser = User.objects.get(username="test_user_1")
        res = self.client.get(reverse("profile", args=[testUser.username]))

        # Assertions
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "registration/profile.html")

    def test_view_display_the_correct_user(self):
        testUser = User.objects.get(username="test_user_1")
        res = self.client.get(reverse("profile", args=[testUser.username]))

        # Assertions
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context["user"], testUser)


class TestCreateNewAccountView(test.TestCase):
    pass
