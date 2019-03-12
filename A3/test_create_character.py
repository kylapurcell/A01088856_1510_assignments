from unittest import TestCase
from unittest.mock import patch
from A3 import character


class TestCreateCharacter(TestCase):
    # Tests 1-7 Test different returned characters for different class choice and dexterity
    @patch('builtins.input', return_value='Kyla')
    @patch('A3.character.choose_class', return_value='Hello Kitty')
    @patch('A3.character.determine_dexterity', return_value=3)
    def test_create_character(self, mock_name, mock_class, mock_dexterity):
        self.assertEqual({'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 10, 'Dexterity': 3,
                          'Location': [2, 2], 'Inventory': [], 'Cursed': False}, character.create_character())

    @patch('builtins.input', return_value='Kyla')
    @patch('A3.character.choose_class', return_value='Glowing One')
    @patch('A3.character.determine_dexterity', return_value=5)
    def test_create_character2(self, mock_name, mock_class, mock_dexterity):
        self.assertEqual({'Name': 'Kyla', 'Class': 'Glowing One', 'Health': 10, 'Dexterity': 5,
                          'Location': [2, 2], 'Inventory': [], 'Cursed': False}, character.create_character())

    @patch('builtins.input', return_value='Kyla')
    @patch('A3.character.choose_class', return_value='Great Gatsby')
    @patch('A3.character.determine_dexterity', return_value=2)
    def test_create_character3(self, mock_name, mock_class, mock_dexterity):
        self.assertEqual({'Name': 'Kyla', 'Class': 'Great Gatsby', 'Health': 10, 'Dexterity': 2,
                          'Location': [2, 2], 'Inventory': [], 'Cursed': False}, character.create_character())

    @patch('builtins.input', return_value='Kyla')
    @patch('A3.character.choose_class', return_value='Grumpy Cat')
    @patch('A3.character.determine_dexterity', return_value=6)
    def test_create_character4(self, mock_name, mock_class, mock_dexterity):
        self.assertEqual({'Name': 'Kyla', 'Class': 'Grumpy Cat', 'Health': 10, 'Dexterity': 6,
                          'Location': [2, 2], 'Inventory': [], 'Cursed': False}, character.create_character())

    @patch('builtins.input', return_value='Kyla')
    @patch('A3.character.choose_class', return_value='Big Chonk')
    @patch('A3.character.determine_dexterity', return_value=10)
    def test_create_character5(self, mock_name, mock_class, mock_dexterity):
        self.assertEqual({'Name': 'Kyla', 'Class': 'Big Chonk', 'Health': 10, 'Dexterity': 10,
                          'Location': [2, 2], 'Inventory': [], 'Cursed': False}, character.create_character())

    @patch('builtins.input', return_value='Kyla')
    @patch('A3.character.choose_class', return_value='Long Boi')
    @patch('A3.character.determine_dexterity', return_value=3)
    def test_create_character6(self, mock_name, mock_class, mock_dexterity):
        self.assertEqual({'Name': 'Kyla', 'Class': 'Long Boi', 'Health': 10, 'Dexterity': 3,
                          'Location': [2, 2], 'Inventory': [], 'Cursed': False}, character.create_character())

    @patch('builtins.input', return_value='Kyla')
    @patch('A3.character.choose_class', return_value='Orange Julius')
    @patch('A3.character.determine_dexterity', return_value=6)
    def test_create_character7(self, mock_name, mock_class, mock_dexterity):
        self.assertEqual({'Name': 'Kyla', 'Class': 'Orange Julius', 'Health': 10, 'Dexterity': 6,
                          'Location': [2, 2], 'Inventory': [], 'Cursed': False}, character.create_character())

    @patch('builtins.input', return_value='Kyla')
    @patch('A3.character.choose_class', return_value='Orange Julius')      # Tests that return value is dictionary
    @patch('A3.character.determine_dexterity', return_value=6)
    def test_create_character8(self, mock_name, mock_class, mock_dexterity):
        self.assertEqual(dict, type(character.create_character()))
