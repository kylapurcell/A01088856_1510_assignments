from unittest import TestCase
from A2 import dungeonsanddragons
from unittest.mock import patch


class TestChooseClass(TestCase):
    @patch('builtins.input', return_value='bard')
    def test_choose_class1(self, mock_class1):
        self.assertEqual('bard', dungeonsanddragons.choose_class())

    @patch('builtins.input', return_value='monk')
    def test_choose_class2(self, mock_class):
        self.assertEqual('monk', dungeonsanddragons.choose_class())

    @patch('builtins.input', return_value='blood hunter')
    def test_choose_class3(self, mock_class2):
        self.assertEqual('blood hunter', dungeonsanddragons.choose_class())

    @patch('builtins.input', return_value='barbarian')
    def test_choose_class4(self, mock_class3):
        self.assertEqual(str, type(dungeonsanddragons.choose_class()))
