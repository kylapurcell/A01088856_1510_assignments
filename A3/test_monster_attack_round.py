from unittest import TestCase
from unittest.mock import patch
import io
import random
from A3 import monster


class TestAttackRound(TestCase):
    @patch('random.randint', side_effect=[10, 3])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_round(self,mock_stdout,mock_random):
        character_attacker = {'Name': 'Charmander', 'Class': 'Hello Kitty', 'Health': 10,
                              'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}
        monster_opponent = {'Name': 'Ghoul', 'Health': 5, 'Damage': 0, 'Dexterity': 7}
        expected_output = """Charmander has a chance to attack
Charmander attacked with damage of 3\n"""
        monster.attack_round(character_attacker, monster_opponent)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('random.randint', side_effect=[2, 3])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_round2(self, mock_stdout, mock_random):
        character_attacker = {'Name': 'Charmander', 'Class': 'Hello Kitty', 'Health': 10,
                              'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}
        monster_opponent = {'Name': 'Ghoul', 'Health': 5, 'Damage': 0, 'Dexterity': 7}
        expected_output = """Charmander has a chance to attack
Attack missed\n"""
        monster.attack_round(character_attacker, monster_opponent)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('random.randint', side_effect=[2, 3])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_round2(self, mock_stdout, mock_random):
        monster_attacker = {'Name': 'Ghoul', 'Health': 5, 'Damage': 0, 'Dexterity': 7}
        character_opponent = {'Name': 'Charmander', 'Class': 'Hello Kitty', 'Health': 10,
                              'Dexterity': 7, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}

        expected_output = """Ghoul has a chance to attack\nAttack missed\n"""
        monster.attack_round(monster_attacker, character_opponent)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('random.randint', side_effect=[10, 3])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_round3(self, mock_stdout, mock_random):
        monster_attacker = {'Name': 'Ghoul', 'Health': 5, 'Damage': 0, 'Dexterity': 7}
        character_opponent = {'Name': 'Charmander', 'Class': 'Hello Kitty', 'Health': 10,
                              'Dexterity': 7, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}

        expected_output = """Ghoul has a chance to attack
Ghoul attacked with damage of 3\n"""
        monster.attack_round(monster_attacker, character_opponent)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
