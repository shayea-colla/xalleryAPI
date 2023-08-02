from django.test import SimpleTestCase
from gallery.forms import CreateRoomForm, AddPictureForm


class TestCreateRoomForm(SimpleTestCase):
    """
    Class for testing the CreateRoomForm

    Testing area:
        __fields:
            * you don't need to test very much here
              because you use ModelForm to generate the form fields so all testing area has being tested in the test_model.py file
              all you need to test is that the fields themselfs exists as you specified them in the fields variable in the Meta class

            _name field:
                --just test that field exist

            _discription field:
                --just test that field exist

    """

    def test_name_field_exist(self):
        form = CreateRoomForm()
        self.assertTrue(form.fields["name"])

    def test_discription_field_exist(self):
        form = CreateRoomForm()
        self.assertTrue(form.fields["discription"])


class TestAddPictureForm(SimpleTestCase):
    """
    Class for testing AddPictureForm.

    Testing area:
        __fields:
            * you don't need to test very much here
              because you use ModelForm to generate the form fields so all testing area has being tested in the test_model.py file
              all you need to test is that the fields themselfs exists as you specified them in the "fields" variable in the Meta class

            _image field:
                --just test that field exist

    """

    def test_image_field_exist(self):
        form = AddPictureForm()
        self.assertTrue(form.fields["image"])
