from unittest import TestCase
from unittest.mock import patch
from A3 import character


class TestChooseClass(TestCase):
    @patch('builtins.input', return_value='Hello Kitty')
    def test_choose_class(self, mock_input):
        self.assertEqual('Hello Kitty', character.choose_class())

    @patch('builtins.input', return_value='Robotic Cat')
    def test_choose_class2(self, mock_input):
        self.assertEqual('Robotic Cat', character.choose_class())

    @patch('builtins.input', return_value='Grumpy Cat')
    def test_choose_class3(self, mock_input):
        self.assertEqual('Grumpy Cat', character.choose_class())

    @patch('builtins.input', return_value='Long Boi')
    def test_choose_class4(self, mock_input):
        self.assertEqual('Long Boi', character.choose_class())

    @patch('builtins.input', return_value='Great Gatsby')
    def test_choose_class5(self, mock_input):
        self.assertEqual('Great Gatsby', character.choose_class())

    @patch('builtins.input', return_value='Big Chonk')
    def test_choose_class6(self, mock_input):
        self.assertEqual('Big Chonk', character.choose_class())

    @patch('builtins.input', return_value='Orange Julius')
    def test_choose_class7(self, mock_input):
        self.assertEqual('Orange Julius', character.choose_class())

    @patch('builtins.input', return_value='Glowing One')
    def test_choose_class8(self, mock_input):
        self.assertEqual('Glowing One', character.choose_class())
