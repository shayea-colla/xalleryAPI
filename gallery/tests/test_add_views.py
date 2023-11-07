import os
    
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Permission
from django.core.files.uploadedfile import SimpleUploadedFile

from accounts.models import User

from gallery.utils  import debug
from gallery.forms  import CreateRoomForm, AddPictureForm
from gallery.models import Room




class TestCreatRoomView(TestCase):
    
    def setUp(self):
        # Create two test users
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


    def test_view_exist_at_desired_location(self):
        self.client.login(username="test_user2", password="no way home ")
        res = self.client.get("/room/add/", follow=True)

        self.assertEqual(res.status_code, 200)

    def test_view_accessible_by_name(self):
        self.client.login(username="test_user2", password="no way home ")
        res = self.client.get(reverse("add-room"))
        self.assertEqual(res.status_code, 200)

    def test_view_use_correct_template(self):
        self.client.login(username="test_user2", password="no way home ")
        res = self.client.get(reverse("add-room"))

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "gallery/room_create_form.html")

        

    def test_view_use_correct_form_class(self):
        # Login
        self.client.login(username="test_user2", password="no way home ")
        res = self.client.get("/room/add/")

        correct_form = CreateRoomForm()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(str(res.context["form"]), str(correct_form))



    def test_form_valid_method(self):
        test_user = User.objects.get(username='test_user2')
        self.client.login(username="test_user2", password="no way home ")
        data = {
            "name": "test_room",
            "background": SimpleUploadedFile(
                name="test_background.jpg",
                content=open(self.filePath, "rb").read(),
                content_type="image/jpg",
            ),
            "discription": "test discription",
        }
        res = self.client.post(reverse("add-room"), data)

        test_room = Room.objects.get(name="test_room")

        self.assertTrue(test_room.owner == test_user )
        self.assertTrue(res.url.startswith("/room/"))



class TestAddPictureView(TestCase):
    def setUp(self):
        # Create two test users
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


        for i in range(2):
            Room.objects.create(
                name=f"test_room_{i}",
                owner=test_user1 if i % 2 else test_user2,
            )
