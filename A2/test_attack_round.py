from unittest import TestCase
from A2 import dungeonsanddragons
import random
import unittest.mock
import io


class TestAttackRound(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_round(self, mock_stdout):
        random.seed(3)
        attacker_winner = {'Name': 'Legoxo', 'Class': 'blood hunter', 'Health': 10, 'Strength': 4, 'Dexterity': 20,
                           'Constitution': 9, 'Intelligence': 13,  'Wisdom': 11, 'Charisma': 10,
                           'XP': 0, 'Inventory': []}

        opponent_loser = {'Name': 'Pikachu', 'Class': 'blood hunter', 'Health': 2, 'Strength': 4, 'Dexterity': 2,
                          'Constitution': 9, 'Intelligence': 13,  'Wisdom': 11, 'Charisma': 10,
                          'XP': 0, 'Inventory': []}
        expected_output = 'Legoxo rolled a 8 , Pikachu has a dexterity of 2' + '\n' \
                          + 'Attack of 9 was successfully struck' + '\n'
        dungeonsanddragons.attack_round(attacker_winner, opponent_loser)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_round2(self, mock_stdout):
        random.seed(5)
        attacker_loser = {'Name': 'Legoxo', 'Class': 'blood hunter', 'Health': 10, 'Strength': 4, 'Dexterity': 2,
                          'Constitution': 9, 'Intelligence': 13, 'Wisdom': 11, 'Charisma': 10,
                          'XP': 0, 'Inventory': []}

        opponent_winner = {'Name': 'Pikachu', 'Class': 'blood hunter', 'Health': 2, 'Strength': 4, 'Dexterity': 20,
                           'Constitution': 9, 'Intelligence': 13, 'Wisdom': 11, 'Charisma': 10,
                           'XP': 0, 'Inventory': []}
        expected_output = 'Legoxo rolled a 20 , Pikachu has a dexterity of 20' + '\n' \
                          + 'Attack did not strike and now Pikachu gets a chance to attack' + '\n' \
                          + 'Pikachu rolled a 9 , Legoxo has a dexterity of 2' \
                          + '\n' + 'Attack of 9 was successfully struck' + '\n'
        dungeonsanddragons.attack_round(attacker_loser, opponent_winner)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        random.seed()





