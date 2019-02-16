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

    def test_create_health4(self):
        random.seed(3)
        self.assertEqual(2, dungeonsanddragons.create_health('wizard'))

    def test_create_health4(self):
        self.assertEqual(int, type(dungeonsanddragons.create_health('bard')))

    def test_create_health5(self):
        random.seed(8)
        self.assertIn(3, range(dungeonsanddragons.create_health('fighter')))
        random.seed()





