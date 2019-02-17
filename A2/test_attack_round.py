from unittest import TestCase
from A2 import dungeonsanddragons
from unittest.mock import patch
import unittest.mock
import io


class TestAttackRound(TestCase):
    # Tests case where attacker successfully strikes and does damage
    @patch('A2.dungeonsanddragons.roll_die', side_effect=[8, 9])        # Mock die roll
    @patch('A2.dungeonsanddragons.create_health', side_effect=[9, 4])    # Mock damage dealt
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)      # Mock printed output
    def test_attack_round(self, mock_stdout, mock_roll, mock_damage):
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

    @patch('A2.dungeonsanddragons.roll_die', side_effect=[20, 9])     # Mock die roll
    @patch('A2.dungeonsanddragons.create_health', side_effect=[2, 9])  # Mock damage dealt
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)       # Mock printed output
    def test_attack_round2(self, mock_stdout, mock_roll, mock_damage):
        # Tests case where attacker strike unsuccessful and opponent attacks and deals damage
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

    def test_attack_round3(self):
        # Tests that attacker and opponent must be of type dictionary and not string
        with self.assertRaises(TypeError):
            dungeonsanddragons.attack_round('', '')

    def test_attack_round4(self):
        # Tests that attacker and opponent must be of type dictionary and not integer
        with self.assertRaises(TypeError):
            dungeonsanddragons.attack_round(1, 2)

    def test_attack_round5(self):
        # Tests that attacker and opponent must be of type dictionary and not float
        with self.assertRaises(TypeError):
            dungeonsanddragons.attack_round(1.6, 1.7)




