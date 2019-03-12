from unittest import TestCase
from unittest.mock import patch
import io
from A3 import sud


class TestIsCharacterDead(TestCase):
    @patch('builtins.input', return_value='yes')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_character_dead(self, mock_stdout, mock_input):
        character = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 0,
                     'Dexterity': 0, 'Location': [2, 2], 'Inventory': [], 'Cursed': False}
        expected_output = 'You awaken at the center of this world, where you started your journey\n'
        sud.is_character_dead(character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', return_value='yes')
    def test_is_character_dead2(self, mock_input):
        self.assertFalse(sud.is_character_dead({'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 0,
                                                'Dexterity': 0, 'Location': [2, 2], 'Inventory': [], 'Cursed': False}))

    @patch('builtins.input', return_value='no')
    def test_is_character_dead3(self, mock_input):
        self.assertTrue(sud.is_character_dead({'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 0,
                                               'Dexterity': 0, 'Location': [2, 2], 'Inventory': [], 'Cursed': False}))

    def test_is_character_dead4(self):
        character = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 5,
                     'Dexterity': 0, 'Location': [2, 2], 'Inventory': [], 'Cursed': False}
        self.assertFalse(sud.is_character_dead(character))

