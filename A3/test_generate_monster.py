from unittest import TestCase
from unittest.mock import patch
from A3 import monster
import random


class TestGenerateMonster(TestCase):
    @patch('A3.monster.monster_class_choice', return_value='Ghoul')
    @patch('A3.monster.monster_dexterity', return_value=3)
    @patch('random.randint', return_value=2)
    def test_generate_monster(self,mock_class,mock_dexterity,mock_damage):
        self.assertEqual({'Name': 'Ghoul', 'Health': 5, 'Damage': 2,
                          'Dexterity': 3}, monster.generate_monster())

    @patch('A3.monster.monster_class_choice', return_value='Rogue Robot')
    @patch('A3.monster.monster_dexterity', return_value=3)
    @patch('random.randint', return_value=2)
    def test_generate_monster2(self, mock_class, mock_dexterity, mock_damage):
        self.assertEqual({'Name': 'Rogue Robot', 'Health': 5, 'Damage': 2,
                          'Dexterity': 3}, monster.generate_monster())

    @patch('A3.monster.monster_class_choice', return_value='Radioactive Rat')
    @patch('A3.monster.monster_dexterity', return_value=3)
    @patch('random.randint', return_value=2)
    def test_generate_monster3(self, mock_class, mock_dexterity, mock_damage):
        self.assertEqual({'Name': 'Radioactive Rat', 'Health': 5, 'Damage': 2,
                          'Dexterity': 3}, monster.generate_monster())

    @patch('A3.monster.monster_class_choice', return_value='Mutated Creature')
    @patch('A3.monster.monster_dexterity', return_value=3)
    @patch('random.randint', return_value=2)
    def test_generate_monster(self, mock_class, mock_dexterity, mock_damage):
        self.assertEqual({'Name': 'Mutated Creature', 'Health': 5, 'Damage': 2,
                          'Dexterity': 3}, monster.generate_monster())

    @patch('A3.monster.monster_class_choice', return_value='Pax')
    @patch('A3.monster.monster_dexterity', return_value=3)
    @patch('random.randint', return_value=2)
    def test_generate_monster(self, mock_class, mock_dexterity, mock_damage):
        self.assertEqual({'Name': 'Pax', 'Health': 5, 'Damage': 2,
                          'Dexterity': 3}, monster.generate_monster())
        
    def test_generate_monster5(self):
        self.assertEqual(dict, type(monster.generate_monster()))




