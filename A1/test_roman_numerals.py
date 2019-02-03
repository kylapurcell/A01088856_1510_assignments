from unittest import TestCase
from A1 import roman_numbers


class TestRomanNumerals (TestCase):
    def test_roman_numerals(self):
        self.assertEqual("I", roman_numbers.roman_numerals(1))

    def test_roman_numerals2(self):
        self.assertEqual("V", roman_numbers.roman_numerals(5))

    def test_roman_numerals21(self):
        self.assertEqual("VI", roman_numbers.roman_numerals(6))

    def test_roman_numerals3(self):
        self.assertEqual("IX", roman_numbers.roman_numerals(9))

    def test_roman_numerals4(self):
        self.assertEqual("X", roman_numbers.roman_numerals(10))

    def test_roman_numerals42(self):
        self.assertEqual("XL", roman_numbers.roman_numerals(40))

    def test_roman_numerals43(self):
        self.assertEqual("XLIX", roman_numbers.roman_numerals(49))

    def test_roman_numerals5(self):
        self.assertEqual("L", roman_numbers.roman_numerals(50))

    def test_roman_numerals51(self):
        self.assertEqual("LX",roman_numbers.roman_numerals(60))

    def test_roman_numerals52(self):
        self.assertEqual("XC", roman_numbers.roman_numerals(90))

    def test_roman_numerals53(self):
        self.assertEqual("XCIX", roman_numbers.roman_numerals(99))

    def test_roman_numerals6(self):
        self.assertEqual("C", roman_numbers.roman_numerals(100))

    def test_roman_numerals62(self):
        self.assertEqual("CD", roman_numbers.roman_numerals(400))

    def test_roman_numerals63(self):
        self.assertEqual("CDXCIX", roman_numbers.roman_numerals(499))

    def test_roman_numerals7(self):
        self.assertEqual("D", roman_numbers.roman_numerals(500))

    def test_roman_numerals71(self):
        self.assertEqual("DC", roman_numbers.roman_numerals(600))

    def test_roman_numerals72(self):
        self.assertEqual("CM", roman_numbers.roman_numerals(900))

    def test_roman_numerals73(self):
        self.assertEqual("CMXCIX", roman_numbers.roman_numerals(999))

    def test_roman_numerals8(self):
        self.assertEqual("M", roman_numbers.roman_numerals(1000))

    def test_roman_numerals82(self):
        self.assertEqual("MMMM", roman_numbers.roman_numerals(4000))

    def test_roman_numerals83(self):
        self.assertEqual("MMMMMMMMMCMXCIX", roman_numbers.roman_numerals(9999))

    def test_roman_numerals9(self):
        self.assertEqual("MMMMMMMMMM", roman_numbers.roman_numerals(10000))




