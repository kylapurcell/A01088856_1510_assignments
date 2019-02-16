from unittest import TestCase
from A2 import dungeonsanddragons
import random


class TestCreateHealth(TestCase):
    def test_create_health(self):
        random.seed(3)
        self.assertEqual(4, dungeonsanddragons.create_health('rogue'))

    def test_create_health1(self):
        random.seed(2)
        self.assertEqual(1, dungeonsanddragons.create_health('fighter'))

    def test_create_health2(self):
        random.seed(4)
        self.assertEqual(4, dungeonsanddragons.create_health('barbarian'))

    def test_create_health3(self):
        random.seed(3)
        self.assertEqual(2, dungeonsanddragons.create_health('wizard'))

    def test_create_health4(self):
        self.assertEqual(int, type(dungeonsanddragons.create_health('bard')))

    def test_create_health42(self):
        random.seed(8)
        self.assertIn(3, range(dungeonsanddragons.create_health('fighter')))
        random.seed()

    def test_create_health5(self):
        self.assertLessEqual(1, dungeonsanddragons.create_health('barbarian'))

    def test_create_health6(self):
        self.assertGreaterEqual(12, dungeonsanddragons.create_health('barbarian'))

    def test_create_health7(self):
        self.assertLessEqual(1, dungeonsanddragons.create_health('cleric'))

    def test_create_health8(self):
        self.assertGreaterEqual(8, dungeonsanddragons.create_health('cleric'))

    def test_create_health9(self):
        self.assertLessEqual(1, dungeonsanddragons.create_health('blood hunter'))

    def test_create_health10(self):
        self.assertGreaterEqual(10, dungeonsanddragons.create_health('blood hunter'))

    def test_create_health11(self):
        self.assertLessEqual(1, dungeonsanddragons.create_health('sorcerer'))

    def test_create_health12(self):
        self.assertGreaterEqual(6, dungeonsanddragons.create_health('sorcerer'))







