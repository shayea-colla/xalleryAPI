from django.test import SimpleTestCase 

from ..debug import debug

class TestDebugFunction(SimpleTestCase):


    def test_debug_function(self):
        debug("solo")
        
