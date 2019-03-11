from unittest import TestCase
import io
from unittest.mock import patch
from A3 import sud


class TestGameMap(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_map(self,mock_stdout):
        character = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 10,
                     'Dexterity': 0, 'Location': [2, 2], 'Inventory': [], 'Cursed': False}

        expected_output = """\n
*****    *****    *****    *****    *****    *****    *****    

*****    *****    *****    *****    *****    *****    *****    

*****    *****    =^..^=   *****    *****    *****    *****    

*****    *****    *****    *****    *****    *****    *****    

*****    *****    *****    *****    *****    *****    *****    

*****    *****    *****    *****    *****    *****    *****    

*****    *****    *****    *****    *****    *****    *****    
\n"""
        sud.game_map(character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)



    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_map2(self,mock_stdout):
        character = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 10,
                     'Dexterity': 0, 'Location': [0, 0], 'Inventory': [], 'Cursed': False}

        expected_output = """\n
=^..^=   *****    *****    *****    *****    *****    *****    

*****    *****    *****    *****    *****    *****    *****    

*****    *****    *****    *****    *****    *****    *****    

*****    *****    *****    *****    *****    *****    *****    

*****    *****    *****    *****    *****    *****    *****    

*****    *****    *****    *****    *****    *****    *****    

*****    *****    *****    *****    *****    *****    *****    
\n"""
        sud.game_map(character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

