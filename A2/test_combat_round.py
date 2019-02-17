from unittest import TestCase
from A2 import dungeonsanddragons
from unittest.mock import patch
import unittest.mock
import io


class TestCombatRound(TestCase):
    @patch('A2.dungeonsanddragons.who_rolls_first', return_value=True)
    @patch('A2.dungeonsanddragons.roll_die', side_effect=[11, 3])
    @patch('A2.dungeonsanddragons.create_health', side_effect=[2, 3])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round(self, mock_stdout, mock_first, mock_roll, mock_damage):
        attacker_loser = {'Name': 'Legoxo', 'Class': 'blood hunter', 'Health': 1, 'Strength': 4, 'Dexterity': 2,
                          'Constitution': 9, 'Intelligence': 13, 'Wisdom': 11, 'Charisma': 10,
                          'XP': 0, 'Inventory': []}

        opponent_winner = {'Name': 'Pikachu', 'Class': 'blood hunter', 'Health': 5, 'Strength': 4, 'Dexterity': 20,
                           'Constitution': 9, 'Intelligence': 13, 'Wisdom': 11, 'Charisma': 10,
                           'XP': 0, 'Inventory': []}
        expected_output = 'Legoxo rolled a 11 , Pikachu has a dexterity of 20' + '\n' \
                          + 'Attack did not strike and now Pikachu gets a chance to attack' + '\n' \
                          + 'Pikachu rolled a 3 , Legoxo has a dexterity of 2' + '\n' \
                          + 'Attack of 3 was successfully struck' + '\n' + 'Legoxo has died' + '\n'

        dungeonsanddragons.combat_round(attacker_loser, opponent_winner)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('A2.dungeonsanddragons.who_rolls_first', return_value=True)
    @patch('A2.dungeonsanddragons.roll_die', side_effect=[13, 3])
    @patch('A2.dungeonsanddragons.create_health', side_effect=[4, 3])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round2(self, mock_stdout, mock_first, mock_roll, mock_damage):
        attacker_winner = {'Name': 'Legoxo', 'Class': 'blood hunter', 'Health': 1, 'Strength': 4, 'Dexterity': 2,
                           'Constitution': 9, 'Intelligence': 13, 'Wisdom': 11, 'Charisma': 10,
                           'XP': 0, 'Inventory': []}

        opponent_loser = {'Name': 'Pikachu', 'Class': 'blood hunter', 'Health': 2, 'Strength': 4, 'Dexterity': 2,
                          'Constitution': 9, 'Intelligence': 13, 'Wisdom': 11, 'Charisma': 10,
                          'XP': 0, 'Inventory': []}
        expected_output = 'Legoxo rolled a 13 , Pikachu has a dexterity of 2' + '\n' \
                          + 'Attack of 4 was successfully struck' + '\n' + 'Pikachu has died' + '\n'

        dungeonsanddragons.combat_round(attacker_winner, opponent_loser)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('A2.dungeonsanddragons.who_rolls_first', return_value=False)
    @patch('A2.dungeonsanddragons.roll_die', side_effect=[13, 3])
    @patch('A2.dungeonsanddragons.create_health', side_effect=[4, 3])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round3(self, mock_stdout, mock_first, mock_roll, mock_damage):
        attacker_loser = {'Name': 'Legoxo', 'Class': 'blood hunter', 'Health': 1, 'Strength': 4, 'Dexterity': 2,
                          'Constitution': 9, 'Intelligence': 13, 'Wisdom': 11, 'Charisma': 10,
                          'XP': 0, 'Inventory': []}

        opponent_winner = {'Name': 'Pikachu', 'Class': 'blood hunter', 'Health': 2, 'Strength': 4, 'Dexterity': 2,
                           'Constitution': 9, 'Intelligence': 13, 'Wisdom': 11, 'Charisma': 10,
                           'XP': 0, 'Inventory': []}
        expected_output = 'Pikachu rolled a 13 , Legoxo has a dexterity of 2' + '\n' \
                          + 'Attack of 4 was successfully struck' + '\n' + 'Legoxo has died' + '\n'

        dungeonsanddragons.combat_round(attacker_loser, opponent_winner)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('A2.dungeonsanddragons.who_rolls_first', return_value=False)
    @patch('A2.dungeonsanddragons.roll_die', side_effect=[3, 3])
    @patch('A2.dungeonsanddragons.create_health', side_effect=[4, 3])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round4(self, mock_stdout, mock_first, mock_roll, mock_damage):
        attacker_winner = {'Name': 'Legoxo', 'Class': 'blood hunter', 'Health': 1, 'Strength': 4, 'Dexterity': 20,
                           'Constitution': 9, 'Intelligence': 13, 'Wisdom': 11, 'Charisma': 10,
                           'XP': 0, 'Inventory': []}

        opponent_loser = {'Name': 'Pikachu', 'Class': 'blood hunter', 'Health': 2, 'Strength': 4, 'Dexterity': 2,
                          'Constitution': 9, 'Intelligence': 13, 'Wisdom': 11, 'Charisma': 10,
                          'XP': 0, 'Inventory': []}
        expected_output = 'Pikachu rolled a 3 , Legoxo has a dexterity of 20' + '\n'\
                          + 'Attack did not strike and now Legoxo gets a chance to attack' + '\n' \
                          + 'Legoxo rolled a 3 , Pikachu has a dexterity of 2' + '\n'\
                          + 'Attack of 3 was successfully struck' + '\n' + 'Pikachu has died' + '\n'

        dungeonsanddragons.combat_round(attacker_winner, opponent_loser)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('A2.dungeonsanddragons.who_rolls_first', return_value=False)
    @patch('A2.dungeonsanddragons.roll_die', side_effect=[3, 3])
    @patch('A2.dungeonsanddragons.create_health', side_effect=[4, 3])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round5(self, mock_stdout, mock_first, mock_roll, mock_damage):
        attacker_survive = {'Name': 'Legoxo', 'Class': 'blood hunter', 'Health': 10, 'Strength': 4, 'Dexterity': 20,
                            'Constitution': 9, 'Intelligence': 13, 'Wisdom': 11, 'Charisma': 10,
                            'XP': 0, 'Inventory': []}

        opponent_survive = {'Name': 'Pikachu', 'Class': 'blood hunter', 'Health': 20, 'Strength': 4, 'Dexterity': 2,
                            'Constitution': 9, 'Intelligence': 13, 'Wisdom': 11, 'Charisma': 10,
                            'XP': 0, 'Inventory': []}
        expected_output = 'Pikachu rolled a 3 , Legoxo has a dexterity of 20' + '\n' \
                          + 'Attack did not strike and now Legoxo gets a chance to attack' + '\n' \
                          + 'Legoxo rolled a 3 , Pikachu has a dexterity of 2' + '\n' \
                          + 'Attack of 3 was successfully struck' + '\n' + \
                          'Both combatants survived the fight. Legoxo now' +\
                          ' has a health of 10 and Pikachu now has a health of  17' + '\n'
        dungeonsanddragons.combat_round(attacker_survive, opponent_survive)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_combat_round6(self):
        with self.assertRaises(TypeError):
            dungeonsanddragons.combat_round('', '')

    def test_combat_round7(self):
        with self.assertRaises(TypeError):
            dungeonsanddragons.combat_round(1, 2)

    def test_combat_round8(self):
        with self.assertRaises(TypeError):
            dungeonsanddragons.combat_round(2.5, 6.7)
