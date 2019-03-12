from unittest import TestCase
from A3 import monster


class TestMonsterDexterity(TestCase):
    def test_monster_dexterity(self):
        self.assertGreaterEqual(4, monster.monster_dexterity('Rogue Robot'))

    def test_monster_dexterity2(self):
        self.assertLessEqual(1, monster.monster_dexterity('Rogue Robot'))

    def test_monster_dexterity3(self):
        self.assertLessEqual(1, monster.monster_dexterity('Ghoul'))

    def test_monster_dexterity4(self):
        self.assertGreaterEqual(6, monster.monster_dexterity('Ghoul'))

    def test_monster_dexterity5(self):
        self.assertLessEqual(1, monster.monster_dexterity('Pax'))

    def test_monster_dexterity6(self):
        self.assertGreaterEqual(20, monster.monster_dexterity('Pax'))
