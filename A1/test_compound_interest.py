from unittest import TestCase
from A1 import compound_interest


class TestCompoundInterest(TestCase):

    def test_compound_interest(self):
        self.assertEqual(0.0, compound_interest.compound_interest(0.0, 0.0, 1, 0))   # Tests lower bounds

    def test_compound_interest2(self):
        self.assertEqual(float, type(compound_interest.compound_interest(7.5, 1.2, 3, 5)))  # Tests if output is a float

    def test_compound_interest3(self):
        self.assertEqual(368.0462271001469, compound_interest.compound_interest(4.5, 0.7, 3, 7))  # Tests higher bounds

    def test_compound_interest4(self):
        self.assertEqual(2126.048271773767, compound_interest.compound_interest(7.8, 1.36, 3, 5))  # Tests higher bounds

