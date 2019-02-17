from unittest import TestCase
from A2 import dungeonsanddragons
from unittest.mock import patch
import random


class TestCreateCharacter(TestCase):

    @patch('A2.dungeonsanddragons.choose_class', return_value='blood hunter')
    def test_create_character(self, mock_class):
        self.assertIsNone(dungeonsanddragons.create_character(0))  # Tests that 0 syllables returns None

    @patch('A2.dungeonsanddragons.choose_class', return_value='barbarian')
    def test_create_character2(self, mock_class):
        self.assertEqual(dict, type(dungeonsanddragons.create_character(4)))  # Tests that output is of type list

    @patch('A2.dungeonsanddragons.choose_class', return_value='wizard')
    def test_create_character3(self, mock_class):
        self.assertEqual(11, len(dungeonsanddragons.create_character(5)))  # Tests that length of output equals 10

    @patch('A2.dungeonsanddragons.choose_class', return_value='blood hunter')
    def test_create_character4(self, mock_class):
        random.seed(2)
        self.assertEqual({'Name': 'Cadi', 'Class': 'blood hunter', 'Health': 7,'Strength': 8, 'Dexterity': 12,
                          'Constitution': 11, 'Intelligence': 9, 'Wisdom': 4, 'Charisma': 8, 'XP': 0, 'Inventory': []}
                         , dungeonsanddragons.create_character(2))
        random.seed()





