from unittest import TestCase
from A2 import dungeonsanddragons
import random


class TestGenerateVowel(TestCase):
    def test_generate_vowel(self):
        self.assertEqual(str, type(dungeonsanddragons.generate_vowel()))   # Tests that output is of type string

    def test_generate_vowel2(self):
        self.assertEqual(1, len(dungeonsanddragons.generate_vowel()))   # Tests that the length of output is 2

    def test_generate_vowel3(self):
        random.seed(2)
        self.assertEqual('A', dungeonsanddragons.generate_vowel())  # Tests fixed random output
        random.seed()
