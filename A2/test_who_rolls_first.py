from unittest import TestCase
from A2 import dungeonsanddragons
from unittest.mock import patch
import random
import unittest.mock
import io


class TestWhoRollsFirst(TestCase):
    @patch('random.randint', side_effect=[8, 3])
    def test_who_rolls_first(self, mock_roll_die):
        self.assertEqual(True, dungeonsanddragons.who_rolls_first())

    @patch('random.randint', side_effect=[9, 13])
    def test_who_rolls_first1(self, mock_roll_die):
        self.assertEqual(False, dungeonsanddragons.who_rolls_first())

    
