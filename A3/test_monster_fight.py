from unittest import TestCase
import io
from A3 import monster
from unittest.mock import patch
import random


class TestMonsterFight(TestCase):
    @patch('builtins.input', return_value='fight')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_fight(self, mock_stdout, mock_input):
        random.seed(4)
        character = {'Name': 'Mew', 'Class': 'Hello Kitty', 'Health': 1,
                     'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}
        monster_opponent = {'Name': 'Ghoul', 'Health': 5, 'Damage': 2, 'Dexterity': 7}
        expected_output = """Ghoul appeared!
Mew has a chance to attack
Mew attacked with damage of 3
Ghoul now has a health of 2
Ghoul has a chance to attack
Ghoul attacked with damage of 6
Mew now has a health of -5
Mew has died\n"""
        monster.monster_fight(character, monster_opponent)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

    @patch('builtins.input', return_value='run')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_fight2(self, mock_stdout, mock_input):
        random.seed(4)
        character = {'Name': 'Mew', 'Class': 'Hello Kitty', 'Health': 6,
                     'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}
        monster_opponent = {'Name': 'Ghoul', 'Health': 5, 'Damage': 2, 'Dexterity': 7}
        expected_output = """Ghoul appeared!\nYou escaped successfully and without a scratch too\n"""
        monster.monster_fight(character, monster_opponent)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

