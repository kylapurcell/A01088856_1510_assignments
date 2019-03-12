from unittest import TestCase
from A3 import character


class TestDetermineDexterity(TestCase):
    def test_determine_dexterity(self):
        self.assertLessEqual(1, character.determine_dexterity('Big Chonk'))
        # Tests that return value is greater than or equal to lower bounds

    def test_determine_dexterity2(self):
        self.assertGreaterEqual(12, character.determine_dexterity('Big Chonk'))
        # Tests that return value is less than or equal to upper bounds

    def test_determine_dexterity3(self):
        self.assertLessEqual(1, character.determine_dexterity('Grumpy Cat'))
        # Tests that return value is greater than or equal to lower bounds

    def test_determine_dexterity4(self):
        self.assertGreaterEqual(8, character.determine_dexterity('Grumpy Cat'))
        # Tests that return value is less than or equal to upper bounds

    def test_determine_dexterity5(self):
        self.assertLessEqual(1, character.determine_dexterity('Great Gatsby'))
        # Tests that return value is greater than or equal to lower bounds

    def test_determine_dexterity6(self):
        self.assertGreaterEqual(10, character.determine_dexterity('Great Gatsby'))
        # Tests that return value is less than or equal to upper bounds

    def test_determine_dexterity7(self):
        self.assertLessEqual(1, character.determine_dexterity('Hello Kitty'))
        # Tests that return value is greater than or equal to lower bounds

    def test_determine_dexterity8(self):
        self.assertGreaterEqual(6, character.determine_dexterity('Hello Kitty'))
        # Tests that return value is less than or equal to upper bounds
