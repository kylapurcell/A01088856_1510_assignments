from unittest import TestCase
from A2 import dungeonsanddragons
import random


class TestGenerateSyllable(TestCase):
    def test_generate_syllable(self):
        self.assertEqual(str, type(dungeonsanddragons.generate_syllable()))   # Tests that output is of type string

    def test_generate_syllable1(self):
        self.assertEqual(2, len(dungeonsanddragons.generate_syllable()))  # Tests that the length of output is 2

    def test_generate_syllable2(self):
        random.seed(5)
        self.assertEqual('YI', dungeonsanddragons.generate_syllable())  # Tests fixed random output
        random.seed()
