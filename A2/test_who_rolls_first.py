from unittest import TestCase
from A2 import dungeonsanddragons
from unittest.mock import patch


class TestWhoRollsFirst(TestCase):
    @patch('A2.dungeonsanddragons.roll_die', side_effect=[8, 3])      # Mock die roll
    def test_who_rolls_first(self, mock_roll_die):
        self.assertEqual(True, dungeonsanddragons.who_rolls_first())  # Tests True case

    @patch('A2.dungeonsanddragons.roll_die', side_effect=[9, 13])  # Mock die roll
    def test_who_rolls_first1(self, mock_roll_die):
        self.assertEqual(False, dungeonsanddragons.who_rolls_first())  # Tests False case

    def test_who_rolls_first(self):
        self.assertEqual(bool, type(dungeonsanddragons.who_rolls_first()))  # Tests output is Boolean



