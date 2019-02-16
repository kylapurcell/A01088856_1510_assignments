from unittest import TestCase
from A2 import dungeonsanddragons


class TestCreateCharacter(TestCase):

    def test_create_character(self):
        self.assertIsNone(dungeonsanddragons.create_character(0))  # Tests that 0 syllables returns None

    def test_create_character2(self):
        self.assertEqual(dict, type(dungeonsanddragons.create_character(4)))  # Tests that output is of type list

    def test_create_character3(self):
        self.assertEqual(10, len(dungeonsanddragons.create_character(5)))  # Tests that length of output equals 10


