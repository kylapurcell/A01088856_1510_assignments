from unittest import TestCase
from A2 import dungeonsanddragons
import random


class TestCreateHealth(TestCase):
    def test_create_health(self):
        random.seed(3)
        self.assertEqual(4, dungeonsanddragons.create_health('rogue'))    # Tests random output for case 1

    def test_create_health1(self):
        random.seed(2)
        self.assertEqual(1, dungeonsanddragons.create_health('fighter'))  # Tests random output for case 2

    def test_create_health2(self):
        random.seed(4)
        self.assertEqual(4, dungeonsanddragons.create_health('barbarian'))  # Tests random output for case 3

    def test_create_health3(self):
        random.seed(3)
        self.assertEqual(2, dungeonsanddragons.create_health('wizard'))  # Tests random output for case 4
        random.seed()

    def test_create_health4(self):
        self.assertEqual(int, type(dungeonsanddragons.create_health('bard')))  # Tests output is of type integer

    def test_create_health5(self):
        self.assertLessEqual(1, dungeonsanddragons.create_health('barbarian'))  # Tests output is in specified range
        # for case 1

    def test_create_health6(self):
        self.assertGreaterEqual(12, dungeonsanddragons.create_health('barbarian'))  # Tests output is in specified range
        # for case 1

    def test_create_health7(self):
        self.assertLessEqual(1, dungeonsanddragons.create_health('cleric'))   # Tests output is in specified range
        # for case 2

    def test_create_health8(self):
        self.assertGreaterEqual(8, dungeonsanddragons.create_health('cleric'))  # Tests output is in specified range
        # for case 2

    def test_create_health9(self):
        self.assertLessEqual(1, dungeonsanddragons.create_health('blood hunter'))  # Tests output is in specified range
        # for case 3

    def test_create_health10(self):
        self.assertGreaterEqual(10, dungeonsanddragons.create_health('blood hunter'))
        # Tests output is in specified range for case 3

    def test_create_health11(self):
        self.assertLessEqual(1, dungeonsanddragons.create_health('sorcerer'))  # Tests output is in specified range
        # for case 4

    def test_create_health12(self):
        self.assertGreaterEqual(6, dungeonsanddragons.create_health('sorcerer'))  # Tests output is in specified range
        # for case 4







