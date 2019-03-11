from unittest import TestCase
from A3 import sud

class TestCreateCoordinates(TestCase):
    def test_create_coordinates(self):
        self.assertEqual(list, type(sud.create_coordinates()))

    def test_create_coordinates2(self):
        self.assertEqual(49, len(sud.create_coordinates()))


