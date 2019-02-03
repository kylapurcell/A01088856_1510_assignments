from unittest import TestCase
from A1 import time_calculator


class TestTimeCalculator(TestCase):

    def test_time_calculator(self):
        self.assertEqual([0, 0, 0, 0], time_calculator.time_calculator(0))    # Tests output on lower bounds

    def test_time_calculator2(self):
        self.assertEqual([0, 0, 0, 4], time_calculator.time_calculator(4.5))    # Tests expected output if given a float

    def test_time_calculator3(self):
        self.assertEqual([1, 24, 1440, 86400], time_calculator.time_calculator(86400))  # Tests output on higher bounds

    def test_time_calculator4(self):
        self.assertEqual(int, type(sum(time_calculator.time_calculator(80000))))    # Tests if result is an integer

    def test_time_calculator5(self):
        self.assertEqual(4, len(time_calculator.time_calculator(900)))           # Tests if length of list is 4
