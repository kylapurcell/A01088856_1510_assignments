from unittest import TestCase
from A2 import dungeonsanddragons
import random


class TestChooseInventory(TestCase):
    def test_choose_inventory(self):
        self.assertEqual([], dungeonsanddragons.choose_inventory([], 0))   # Tests that 0 as selection
        # returns empty list

    def test_choose_inventory2(self):
        self.assertIsNone(dungeonsanddragons.choose_inventory([1, 2], -1))  # Tests that negative selection is None

    def test_choose_inventory3(self):
        self.assertIsNone(dungeonsanddragons.choose_inventory([1, 2, 3], 4))  # Tests that selection
        # greater than list index is None

    def test_choose_inventory4(self):
        self.assertEqual([1, 2, 3], dungeonsanddragons.choose_inventory([1, 2, 3], 3))  # Tests selection =list length,
        # output will return copy

    def test_choose_inventory5(self):
        self.assertEqual(2, len(dungeonsanddragons.choose_inventory([1, 2, 3, 4], 2)))
        # Tests that length of list = selection

    def test_choose_inventory6(self):
        self.assertEqual(list, type(dungeonsanddragons.choose_inventory([1, 2], 2)))
        # Tests that output is of type list

    def test_choose_inventory7(self):                                        # Tests random output
        random.seed(3)
        self.assertEqual(['Ring', 'Staff'], dungeonsanddragons.choose_inventory(['Ring', 'Staff', 'Scroll'], 2))
        random.seed()







