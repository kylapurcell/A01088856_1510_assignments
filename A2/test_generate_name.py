from unittest import TestCase
from A2 import dungeonsanddragons
import random


class TestGenerateName(TestCase):
    def test_generate_name(self):
        self.assertEqual(str, type(dungeonsanddragons.generate_name(2)))     # Tests that output is of type string

    def test_generate_name1(self):
        self.assertEqual(4, len(dungeonsanddragons.generate_name(2)))      # Tests that length of output is four

    def test_generate_name2(self):
        with self.assertRaises(TypeError):
            dungeonsanddragons.generate_name('')               # Tests that name_length must be an integer

    def test_generate_name3(self):
        random.seed(6)
        self.assertEqual('Xaticagy', dungeonsanddragons.generate_name(4))  # Tests fixed random output
        random.seed()


