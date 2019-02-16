from unittest import TestCase
import lab_04


class TestCreateCharacter(TestCase):

    def test_create_character(self):
        self.assertIsNone(lab_04.create_character(0))  # Tests that 0 name length returns None

    def test_create_character2(self):
        self.assertEqual(list, type(lab_04.create_character(4)))  # Tests that output is of type list

    def test_create_character3(self):
        self.assertEqual(7, len(lab_04.create_character(5)))  # Tests that length of output equals 7


