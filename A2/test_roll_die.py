from unittest import TestCase
import lab_04


class TestRollDie(TestCase):
    def test_roll_die(self):
        self.assertLess(0, lab_04.roll_die(3, 6))     # Tests that output is a positive int

    def test_roll_die2(self):
        self.assertGreaterEqual(18, lab_04.roll_die(3, 6))  # Tests that output is <= num_rolls * num_sides

    def test_roll_die3(self):
        self.assertLessEqual(3, lab_04.roll_die(3, 6))  # Tests that output is >= number of rolls

    def test_roll_die4(self):
        self.assertEqual(0, lab_04.roll_die(0, 0))   # Tests that 0 rolls and 0 sides returns 0

    def test_roll_die5(self):
        self.assertEqual(int, type(lab_04.roll_die(3, 7)))  # Tests that output is of type int
