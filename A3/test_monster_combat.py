from unittest import TestCase
import io
from A3 import monster
from unittest.mock import patch
import random


class TestMonsterCombat(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_combat(self,mock_stdout):
        random.seed(3)
        character = {'Name': 'Mew', 'Class': 'Hello Kitty', 'Health': 1,
                     'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}
        monster_opponent = {'Name': 'Ghoul', 'Health': 5, 'Damage': 2, 'Dexterity': 7}
        expected_output = """Mew has a chance to attack
Mew attacked with damage of 5
Ghoul now has a health of 0
Ghoul has died\n"""
        monster.monster_combat(character,monster_opponent)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_combat2(self, mock_stdout):
        random.seed(3)
        character = {'Name': 'Mew', 'Class': 'Hello Kitty', 'Health': 1,
                     'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}
        monster_opponent = {'Name': 'Ghoul', 'Health': 10, 'Damage': 2, 'Dexterity': 7}
        expected_output = """Mew has a chance to attack
Mew attacked with damage of 5
Ghoul now has a health of 5
Ghoul has a chance to attack
Ghoul attacked with damage of 2
Mew now has a health of -1
Mew has died\n"""
        monster.monster_combat(character, monster_opponent)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

