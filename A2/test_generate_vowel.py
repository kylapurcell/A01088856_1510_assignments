from unittest import TestCase
from A2 import dungeonsanddragons
import random


class TestGenerateVowel(TestCase):
    def test_generate_vowel(self):
        self.assertEqual(str, type(dungeonsanddragons.generate_vowel()))

    def test_generate_vowel2(self):
        self.assertEqual(1, len(dungeonsanddragons.generate_vowel()))

    def test_generate_vowel3(self):
        random.seed(2)
        self.assertEqual('A', dungeonsanddragons.generate_vowel())
        random.seed()
