import uuid
import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from gallery.models import Room, Picture
from gallery.forms import CreateRoomForm
from accounts.models import User


class TestAddRoomView(TestCase):
    """
    Testing the add_room function-based view

    .Testing_area:
        -url: /room/add/
        -require_http_methods: GET, POST
        -login_required
        -permission_required: 'gallery.add_room"
        -template_name: "gallery/room_create_form.html"
        -form_class: "CreateRoomForm"

        if valid_form submitted:
            -create_new_room
            -redirect_to_room_absolute_url
        else :
           -rerender the form with error messages


    """

    def setUp(self):
        # Create two users , one with correct permission
        test_user1 = User.objects.create_user(
            username="test_user1", password="no way home "
        )
        test_user2 = User.objects.create_user(
            username="test_user2", password="no way home "
        )

        # Add permission requried to the second user
        add_room_perm = Permission.objects.get(codename="add_room")
        test_user2.user_permissions.add(add_room_perm)

        test_user2.save()

        # Get the image filePath
        current_dir = os.getcwd()
        path = "static/test_image/image.jpg"
        self.filePath = os.path.join(current_dir, path)

#    def test_require_http_method(self):
#        # Login the user first, or you will always get a 302 (redirect) status code
#        self.client.login(username="test_user2", password="no way home ")
#
#        res = self.client.delete(reverse("add-room"))
#        self.assertEqual(res.status_code, 405)
#
#        res = self.client.put(reverse("add-room"))
#        self.assertEqual(res.status_code, 405)
#
#        res = self.client.patch(reverse("add-room"))
#        self.assertEqual(res.status_code, 405)

    def test_view_accessible_via_get_for_logged_in_users_with_correct_permission(self):
        self.client.login(username="test_user2", password="no way home ")
        res = self.client.get("/room/add/")

        self.assertEqual(res.status_code, 200)

    def test_permission_denied_if_logged_in_without_correct_permission(self):
        self.client.login(username="test_user1", password="no way home ")
        res = self.client.get("/room/add/")

        # Assert raising permissionDeniedError
        self.assertEqual(res.status_code, 403)

    def test_redirection_if_not_logged_in(self):
        res = self.client.get("/room/add/")

        self.assertRedirects(res, reverse("login") + "?next=/room/add/")

    def test_view_accessible_by_name(self):
        self.client.login(username="test_user2", password="no way home ")
        res = self.client.get(reverse("add-room"))

        self.assertEqual(res.status_code, 200)

    def test_view_use_correct_tmeplate(self):
        self.client.login(username="test_user2", password="no way home ")
        res = self.client.get("/room/add/")

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "gallery/room_create_form.html")

    def test_view_use_correct_form_class(self):
        self.client.login(username="test_user2", password="no way home ")
        res = self.client.get("/room/add/")

        correct_form = CreateRoomForm()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(str(res.context["form"]), str(correct_form))

    def test_submitting_valid_data(self):
        self.client.login(username="test_user2", password="no way home ")
        data = {
            "name": "test room",
            "background": SimpleUploadedFile(
                name="test_background.jpg",
                content=open(self.filePath, "rb").read(),
                content_type="image/jpg",
            ),
            "discription": "test discription",
        }
        res = self.client.post(reverse("add-room"), data)

        test_room = Room.objects.get(name="test room")

        self.assertTrue(bool(test_room))
        self.assertTrue(res.url.startswith("/room/"))

    def test_submitting_invalid_data(self):
        self.client.login(username="test_user2", password="no way home ")
        # Omit the name so you can test invalid submition
        data = {
            "background": SimpleUploadedFile(
                name="test_background.jpg",
                content=open(self.filePath, "rb").read(),
                content_type="image/jpg",
            ),
            "discription": "test discription",
        }
        res = self.client.post(reverse("add-room"), data)

        # Assert no room created.
        all_rooms = Room.objects.all()
        self.assertEqual(len(all_rooms), 0)

