from unittest import TestCase
import lab_04


class TestChooseInventory(TestCase):
    def test_choose_inventory(self):
        self.assertEqual([], lab_04.choose_inventory([], 0))   # Tests that 0 as selection returns empty list

    def test_choose_inventory2(self):
        self.assertIsNone(lab_04.choose_inventory([1, 2], -1))  # Tests that negative selection is None

    def test_choose_inventory3(self):
        self.assertIsNone(lab_04.choose_inventory([1, 2, 3], 4))  # Tests that selection greater than list index is None

    def test_choose_inventory4(self):
        self.assertEqual([1, 2, 3], lab_04.choose_inventory([1, 2, 3], 3))  # Tests selection =list length, return copy

    def test_choose_inventory5(self):
        self.assertEqual(2, len(lab_04.choose_inventory([1, 2, 3, 4], 2)))  # Tests that length of list = selection

    def test_choose_inventory6(self):
        self.assertEqual(list, type(lab_04.choose_inventory([1, 2], 2)))  # Tests that output is of type list







