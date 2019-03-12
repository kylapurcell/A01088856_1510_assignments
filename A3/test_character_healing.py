from unittest import TestCase
from unittest.mock import patch
import io
from A3 import character


class TestCharacterHealing(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_healing(self, mock_stdout):     # Tests printed output when character health < 10
        character_one = {'Name': 'Mew', 'Class': 'Hello Kitty', 'Health': 1,
                         'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}
        expected_output = 'Your health has revitalized to 2\n'
        character.character_healing(character_one)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_character_healing2(self):
        character_one = {'Name': 'Mew', 'Class': 'Hello Kitty', 'Health': 10,  # Tests that function returns None
                         'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}
        self.assertIsNone(character.character_healing(character_one))



