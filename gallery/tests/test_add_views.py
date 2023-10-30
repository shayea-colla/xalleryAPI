from django.test import TestCase




class TestCreatRoomView(TestCase):
    
    @classmethod
    def setUpTestData():
        # Create two test users
        test_user1 = User.objects.create_user(
            username="test_user1", password="no way home "
        )

        test_user2 = User.objects.create_user(
            username="test_user2", password="no way home "
        )
        

    def test_login_required(self):
        res = self.client.get("room/add/")
        self.assertEqual(res.status_code, 302)

    def test_view_exist_at_desired_location(self):
        self.client.login(username="test_user1", password="no way home ")
        res = self.client.get("room/add/")
        self.assertEqual(res.status_code, 200)

    def test_view_accessible_by_name(self):
        self.client.login(username="test_user1", password="no way home ")
        res = self.client.get(reverse("add-room"))
        self.assertEqual(res.status_code, 200)

    def test_view_use_correct_template(self):
        self.client.login(username="test_user1", password="no way home ")
        res = self.client.get(reverse("add-room"))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "gallery/room_create_form.html")

        


class TestAddPictureView(TestCase):
    TODO
    ...
