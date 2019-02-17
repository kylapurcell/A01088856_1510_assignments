from unittest import TestCase
from A2 import dungeonsanddragons
import unittest.mock
import io


class TestPrintCharacter(TestCase):                              # Tests printed output
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character(self, mock_stdout):
        character = {'Name': 'Kiwo', 'Class': 'sorcerer', 'Health': 6,
                     'Strength': 6, 'Dexterity': 6, 'Constitution': 9,
                     'Intelligence': 13, 'Wisdom': 5, 'Charisma': 5, 'XP': 0, 'Inventory': []}
        expected_output = ('Name: Kiwo' + '\n' + 'Class: sorcerer' + '\n' + 'Health: 6' + '\n' +
                           'Strength: 6' + '\n' + 'Dexterity: 6' + '\n' + 'Constitution: 9' + '\n'
                           + 'Intelligence: 13' + '\n' + 'Wisdom: 5' + '\n' + 'Charisma: 5' + '\n'
                           + 'XP: 0' + '\n' 'Inventory: []' + '\n')
        dungeonsanddragons.print_character(character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

