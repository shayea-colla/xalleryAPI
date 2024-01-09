from gallery.utils import debug

from django.test import SimpleTestCase


class TestUtils(SimpleTestCase):
    def test_debug(self):
        debug("no way home")
