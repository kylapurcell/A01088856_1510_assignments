from unittest import TestCase
from A1 import lotto


class TestNumberGenerator(TestCase):
    def test_number_generator(self):                        # tests if list is of length 6
        self.assertEqual(6, len(lotto.number_generator()))

    def test_number_generator2(self):
        self.assertEqual(list, type(lotto.number_generator()))   # tests if out put is of type list

    def test_number_generator3(self):                           # tests if contents of the list are integer
        self.assertTrue(int, type(sum(lotto.number_generator())))

    def test_number_generator4(self):
        list2 = lotto.number_generator()
        self.assertNotEqual(list2[0], list2[1])                 # tests if list consists of unique objects
        self.assertNotEqual(list2[0], list2[2])
        self.assertNotEqual(list2[0], list2[3])
        self.assertNotEqual(list2[0], list2[4])
        self.assertNotEqual(list2[0], list2[5])
        self.assertNotEqual(list2[1], list2[2])
        self.assertNotEqual(list2[1], list2[3])
        self.assertNotEqual(list2[1], list2[4])
        self.assertNotEqual(list2[1], list2[5])
        self.assertNotEqual(list2[2], list2[3])
        self.assertNotEqual(list2[2], list2[4])
        self.assertNotEqual(list2[2], list2[5])
        self.assertNotEqual(list2[3], list2[4])
        self.assertNotEqual(list2[3], list2[5])
        self.assertNotEqual(list2[4], list2[5])











