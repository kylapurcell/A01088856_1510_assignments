from unittest import TestCase
from unittest.mock import patch
import io
from A3 import monster


class TestMonsterEncounter(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)   # Tests printed output for regular monster encounter
    def test_monster_encounter(self, mock_stdout):
        character = {'Name': 'Mew', 'Class': 'Hello Kitty', 'Health': 1,
                     'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}
        monster_opponent = {'Name': 'Ghoul', 'Health': 5, 'Damage': 2, 'Dexterity': 7}
        expected_output = 'Ghoul appeared!\n'
        monster.monster_encounter(monster_opponent, character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)   # Tests printed output for rare monster encounter
    def test_monster_encounter2(self, mock_stdout):
        character = {'Name': 'Mew', 'Class': 'Hello Kitty', 'Health': 1,
                     'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}
        monster_opponent = {'Name': 'Pax', 'Health': 5, 'Damage': 2, 'Dexterity': 7}
        expected_output = """Pax appeared!
You have encountered the demon thief of destiny
^( Ծ^6^Ծ )^\n"""
        monster.monster_encounter(monster_opponent, character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
