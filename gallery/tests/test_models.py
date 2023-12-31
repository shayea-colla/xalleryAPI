import os
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models import PROTECT

from gallery.models import Picture, Room
from accounts.models import User


class TestPictureModel(TestCase):
    """
    Testing the Picture model
    """

    @classmethod
    def setUpTestData(self):
        """Creating rooms first"""
        # Creating two users
        test_user = User.objects.create_user(
            username="test_user", password="no way home"
        )

        # Get the image file path
        current_dir = os.getcwd()
        path = "static/test_image/image.jpg"
        filePath = os.path.join(current_dir, path)

        # Create First Room
        test_room = Room(name="test_room", owner=test_user, discription="room num 1")

        # Add the background field
        test_room.background = SimpleUploadedFile(
            name=f"test_room_background_1.jpg",
            content=open(filePath, "rb").read(),
            content_type="image/jpg",
        )

        test_room.save()

        """Create picture"""
        test_pic = Picture()
        test_pic.image = SimpleUploadedFile(
            name="test_image.jpg",
            content=open(filePath, "rb").read(),
            content_type="image/jpg",
        )
        test_pic.room = test_room
        test_pic.save()

    def test_str_function(self):
        # Get one picture
        test_picture = Picture.objects.all()[0]

        # you need to put the 'test_picture' inside the str() build-in function to test the return value of __str__
        self.assertEqual(str(test_picture), str(test_picture.id))

    def test_image_field_name(self):
        test_pictures = Picture.objects.all()

        self.assertEqual(len(test_pictures), 1)

        # get the first picture from the list of pictures
        test_picture = test_pictures[0]

        self.assertTrue(test_picture.image.name.startswith("pictures/"))

    def test_image_url(self):
        test_picture = Picture.objects.all()[0]

        self.assertTrue(test_picture.image.url.startswith("/media/pictures/"))

    def test_room_is_test_room(self):
        """test picture room is the intended room(test_room)"""

        test_room = Room.objects.get(name="test_room")
        test_pictures = Picture.objects.all()

        # There is only one picture in db
        self.assertEqual(len(test_pictures), 1)

        # Get the first one (the only one)
        test_picture = test_pictures[0]

        # Check that test_picture belone to test_room (have the foreignkey as test_room)
        self.assertEqual(test_picture.room, test_room)

    def test_delete_all_pictures_from_filesystem(self):
        for picture in Picture.objects.all():
            picture.image.delete()

        for room in Room.objects.all():
            room.background.delete()


class TestRoomModel(TestCase):
    """
    Testing the Room model

    The symbol '*' endicate the not tested area

    #Testing area:
        _name:
            - field_label
            - max_length
            - help_text
            - unique
            - error_messages *

        _owner: *
            - related_name
            - on_delete=PROTECT

        _background:
            - upload_to file
            - null = False

        _discription:
            - blanck = False

        _created_at:
            - auto_now_add = True
    """

    @classmethod
    def setUpTestData(self):
        # Create two users
        user_1 = User.objects.create_user(username="user_1", password="no way home")

        user_2 = User.objects.create_user(username="user_2", password="no way home")

        # Get the location of the test image
        # used to test uploading images
        current_dir = os.getcwd()
        path = "static/test_image/image.jpg"
        filePath = os.path.join(current_dir, path)

        # Create two rooms
        room_1 = Room.objects.create(
            name="room_1",
            owner=user_1,
            background=SimpleUploadedFile(
                name="test_room_background_1.jpg",
                content=open(filePath, "rb").read(),
                content_type="image/jpg",
            ),
            discription="",
        )
        room_2 = Room.objects.create(
            name="room_2",
            owner=user_1,
            background=SimpleUploadedFile(
                name="test_room_background_2.jpg",
                content=open(filePath, "rb").read(),
                content_type="image/jpg",
            ),
            discription="no way home",
        )

        # Upload a few pictures.
        num_pictures = 20
        for i in range(num_pictures):
            Picture.objects.create(
                image=SimpleUploadedFile(
                    name=f"test_image_{1}.jpg",
                    content=open(filePath, "rb").read(),
                    content_type="image/jpg",
                ),
                room=room_1 if i % 2 else room_2,
            )

    """ 
    Testing Room function: 
        _str:
            return: room name 
        _get_absolute_url:
            return : /room/<room_pk>/

    """

    def test_str_function(self):
        room = Room.objects.get(name="room_1")
        # you need to put the room inside the str() build-in function to test the return value of __str__
        self.assertEqual(str(room), room.name)

    def test_get_absolute_url(self):
        room = Room.objects.get(name="room_1")
        self.assertEqual(room.get_absolute_url(), f"/gallery/room/{room.id}")

    """ 
    Testing name field 
        _name:
            - max_length
            - help_text
            - unique
            - error_messages *
    """

    def test_name_field_label(self):
        room = Room.objects.get(name="room_1")
        field_label = room._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length_is_150(self):
        room = Room.objects.get(name="room_1")
        max_length = room._meta.get_field("name").max_length
        self.assertEqual(max_length, 150)

    def test_name_is_unique(self):
        room = Room.objects.get(name="room_1")
        unique_field = room._meta.get_field("name").unique
        self.assertTrue(unique_field)

    """
    Testing owner field 
        _owner:
            - related_name
            - on_delete=PROTECT
    """
    #    def test_owner_related_name(self):
    #        room = Room.objects.get(name='room_1')
    #        related_name = room._meta.get_field('owner').related_name
    #        self.assertEqual(related_name, 'rooms')
    #
    #    def test_owner_on_delete(self):
    #        room = Room.objects.get(name='room_1')
    #        on_delete = room._meta.get_field('owner').on_delete
    #        self.assertEqual(on_delete, PROTECT)

    """
    Testing background field 
        _background:
            - upload_to file
            - null = False
    """

    def test_background_upload_to(self):
        room = Room.objects.get(name="room_1")
        upload_to = room._meta.get_field("background").upload_to
        self.assertEqual(upload_to, "rooms_background/")

    def test_background_null(self):
        room = Room.objects.get(name="room_1")
        null = room._meta.get_field("background").null
        self.assertFalse(null)

    """ 
    Testing discription field
        _discription:
            - blanck = False
        
        _created_at:
            - auto_now_add = True
    """

    def test_discription_is_required(self):
        room = Room.objects.get(name="room_1")
        blank = room._meta.get_field("discription").blank
        self.assertFalse(blank)

    """ 
    Testing create_at field
        _created_at:
            - auto_now_add = True
    """

    def test_created_at_auto_now_add(self):
        room = Room.objects.get(name="room_1")
        auto_now_add = room._meta.get_field("created_at").auto_now_add
        self.assertTrue(auto_now_add)

        # Remove all background_test_images from filesystem
        for room in Room.objects.all():
            room.background.delete()

    def test_delete_all_pictures_from_filesystem(self):
        # Remove all Pictures from filesystem
        for picture in Picture.objects.all():
            picture.image.delete()

        # Remove all rooms backgrounds from filesystem
        for room in Room.objects.all():
            room.background.delete()
