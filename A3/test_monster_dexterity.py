from unittest import TestCase
from A3 import monster


class TestMonsterDexterity(TestCase):
    def test_monster_dexterity(self):
        # Tests that return value is less than or equal to upper bounds
        self.assertGreaterEqual(4, monster.monster_dexterity('Rogue Robot'))

    def test_monster_dexterity2(self):
        # Tests that return value is greater than or equal to lower bounds
        self.assertLessEqual(1, monster.monster_dexterity('Rogue Robot'))

    def test_monster_dexterity3(self):
        # Tests that return value is greater than or equal to lower bounds
        self.assertLessEqual(1, monster.monster_dexterity('Ghoul'))

    def test_monster_dexterity4(self):
        # Tests that return value is less than or equal to upper bounds
        self.assertGreaterEqual(6, monster.monster_dexterity('Ghoul'))

    def test_monster_dexterity5(self):
        # Tests that return value is greater than or equal to lower bounds
        self.assertLessEqual(1, monster.monster_dexterity('Pax'))

    def test_monster_dexterity6(self):
        # Tests that return value is less than or equal to upper bounds
        self.assertGreaterEqual(20, monster.monster_dexterity('Pax'))

    def test_monster_dexterity7(self):
        # Tests that return value is of type integer
        self.assertEqual(int, type(monster.monster_dexterity('Ghoul')))
