from django.test import SimpleTestCase
from ..utils import clean_tags, remove_duplicate_tags


class TestCleanTags(SimpleTestCase):

    def test_cleaning_white_spaces(self):
        cleaned_tags = clean_tags([" solo", "dany  ", "    many    "])
        expected_tags = {"solo", "dany", "many"}
        self.assertEqual(cleaned_tags, expected_tags)

    def test_removing_empty_values(self):
        cleaned_tags = clean_tags([" solo", "dany  ", "    many    ", "", "    "])
        self.assertEqual(len(cleaned_tags), 3)

class TestRemoveDuplicate_Tags(SimpleTestCase):

    def test_removing_duplicate_tags(self):
        tags = ["solo", "solo", "solo", "dany", "many", "many"]
        cleaned_tags = remove_duplicate_tags(tags)
        expected_tags = {"solo", "dany", "many"}
        self.assertEqual(cleaned_tags, expected_tags)

