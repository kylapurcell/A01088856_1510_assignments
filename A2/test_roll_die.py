from unittest import TestCase
from A2 import dungeonsanddragons
import random


class TestRollDie(TestCase):
    def test_roll_die(self):
        self.assertLess(0, dungeonsanddragons.roll_die(3, 6))     # Tests that output is a positive int

    def test_roll_die2(self):
        self.assertGreaterEqual(18, dungeonsanddragons.roll_die(3, 6))  # Tests that output is <= num_rolls * num_sides

    def test_roll_die3(self):
        self.assertLessEqual(3, dungeonsanddragons.roll_die(3, 6))  # Tests that output is >= number of rolls

    def test_roll_die4(self):
        self.assertEqual(0, dungeonsanddragons.roll_die(0, 0))   # Tests that 0 rolls and 0 sides returns 0

    def test_roll_die5(self):
        self.assertEqual(int, type(dungeonsanddragons.roll_die(3, 7)))  # Tests that output is of type int

    def test_roll_die6(self):
        random.seed(2)
        self.assertEqual(4, dungeonsanddragons.roll_die(3, 6))  # Tests output by holding randomization in place
        random.seed()

