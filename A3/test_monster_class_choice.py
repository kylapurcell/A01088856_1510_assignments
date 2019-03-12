from unittest import TestCase
from unittest.mock import patch
import random
from A3 import monster


class TestMonsterClassChoice(TestCase):
    @patch('random.randint', side_effect=[1, 20])      # Tests case where Ghoul is returned
    def test_monster_class_choice(self, mock_random):
        self.assertEqual('Ghoul', monster.monster_class_choice())

    @patch('random.randint', side_effect=[2, 20])    # Tests case where Radioactive Rat is returned
    def test_monster_class_choice2(self, mock_random):
        self.assertEqual('Radioactive Rat', monster.monster_class_choice())

    @patch('random.randint', side_effect=[3, 20])   # Tests case where Rogue Robot is returned
    def test_monster_class_choice3(self, mock_random):
        self.assertEqual('Rogue Robot', monster.monster_class_choice())

    @patch('random.randint', side_effect=[4, 20])  # Tests case where Mutated Creature is returned
    def test_monster_class_choice4(self, mock_random):
        self.assertEqual('Mutated Creature', monster.monster_class_choice())

    @patch('random.randint', side_effect=[1, 50])  # Tests case where Pax is returned
    def test_monster_class_choice5(self, mock_random):
        self.assertEqual('Pax', monster.monster_class_choice())

    @patch('random.randint', side_effect=[4, 20])  # Tests that return value is of type string
    def test_monster_class_choice6(self, mock_random):
        self.assertEqual(str, type(monster.monster_class_choice()))
