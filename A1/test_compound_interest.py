from unittest import TestCase
from A1 import compound_interest


class TestCompoundInterest(TestCase):

    def test_compound_interest(self):
        self.assertEqual(0.0, compound_interest.compound_interest(0.0, 0.0, 1, 0))

    def test_compound_interest2(self):
        self.assertEqual(float, type(compound_interest.compound_interest(7.5, 1.2, 3, 5)))

    def test_compound_interest3(self):
        self.assertEqual(, compound_interest)

