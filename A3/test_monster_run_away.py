from unittest import TestCase
from unittest.mock import patch
import io
from A3 import monster


class TestMonsterRunAway(TestCase):
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_run_away(self,mock_stdout,mock_chance):
        character = {'Name': 'Mew', 'Class': 'Hello Kitty', 'Health': 10,
                     'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}
        monster_opponent = {'Name': 'Ghoul', 'Health': 5, 'Damage': 2, 'Dexterity': 7}
        expected_output = """Ghoul attacked as you were running away with a attack of 2 your health is now 8
You survived to fight another day\n"""
        monster.monster_run_away(character,monster_opponent)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('random.randint', return_value=4)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_run_away2(self, mock_stdout, mock_chance):
        character = {'Name': 'Mew', 'Class': 'Hello Kitty', 'Health': 10,
                     'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}
        monster_opponent = {'Name': 'Ghoul', 'Health': 5, 'Damage': 2, 'Dexterity': 7}
        expected_output = "You escaped successfully and without a scratch too\n"
        monster.monster_run_away(character, monster_opponent)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_run_away3(self, mock_stdout, mock_chance):
        character = {'Name': 'Mew', 'Class': 'Hello Kitty', 'Health': 1,
                     'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}
        monster_opponent = {'Name': 'Ghoul', 'Health': 5, 'Damage': 2, 'Dexterity': 7}
        expected_output = """Ghoul attacked as you were running away with a attack of 2 your health is now -1
You died\n"""
        monster.monster_run_away(character, monster_opponent)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
