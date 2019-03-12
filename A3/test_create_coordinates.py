from unittest import TestCase
from A3 import sud


class TestCreateCoordinates(TestCase):
    def test_create_coordinates(self):                           # Tests that return value is of type list
        self.assertEqual(list, type(sud.create_coordinates()))

    def test_create_coordinates2(self):                         # Tests that length of return list is 49
        self.assertEqual(49, len(sud.create_coordinates()))

    def test_create_coordinates3(self):                         # Tests that list items are sub-lists
        for i in sud.create_coordinates():
            self.assertEqual(list, type(i))

    def test_create_coordinates4(self):                       # Tests that first item is sub-lists are ints
        for i in sud.create_coordinates():
            self.assertEqual(int, type(i[0]))

    def test_create_coordinates5(self):                       # Tests that second item in sublist are ints
        for i in sud.create_coordinates():
            self.assertEqual(int, type(i[1]))




