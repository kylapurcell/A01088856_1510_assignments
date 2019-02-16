from unittest import TestCase
from A2 import dungeonsanddragons
import random


class TestGenerateConsonant(TestCase):
    def test_generate_consonant(self):
        self.assertEqual(str, type(dungeonsanddragons.generate_consonant()))

    def test_generate_consonant1(self):
        self.assertEqual(1, len(dungeonsanddragons.generate_consonant()))

    def test_generate_consonant2(self):
        random.seed(4)
        self.assertEqual('K', dungeonsanddragons.generate_consonant())
