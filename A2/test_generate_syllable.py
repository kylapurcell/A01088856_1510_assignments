from unittest import TestCase
from A2 import dungeonsanddragons
import random


class TestGenerateSyllable(TestCase):
    def test_generate_syllable(self):
        self.assertEqual(str, type(dungeonsanddragons.generate_syllable()))

    def test_generate_syllable1(self):
        self.assertEqual(2, len(dungeonsanddragons.generate_syllable()))

    def test_generate_syllable2(self):
        random.seed(5)
        self.assertEqual('YI', dungeonsanddragons.generate_syllable())
        random.seed()
