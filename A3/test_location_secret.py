from unittest import TestCase
from unittest.mock import patch
import io
from A3 import sud


class TestLocationSecret(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_secret(self,mock_stout):
        character_one = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 0,
                         'Dexterity': 0, 'Location': [5, 5], 'Inventory': [], 'Cursed': False}
        expected_output = 'You notice something strange about this area but cannot quite put your finger on it\n'
        sud.location_secret(character_one)
        self.assertEqual(mock_stout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_secret2(self, mock_stout):
        character_one = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 0,
                         'Dexterity': 0, 'Location': [5, 5], 'Inventory': [], 'Cursed': True}
        expected_output = """Hey you've found me. I'm the developer of this game. You are here because you are \
one of the lucky
              individuals to find my easter egg. I added this in my game because I love Black Mirror's Bandersnatch.
              If you have not seen it yet, you should. Anyway I'll un-curse you so you can beat the game! 
              Thanks for playing!!!\n"""
        sud.location_secret(character_one)
        self.assertEqual(mock_stout.getvalue(), expected_output)
