from unittest import TestCase
from A1 import roman_numbers


class TestRomanNumerals (TestCase):
    def test_roman_numerals(self):
        self.assertEqual("I", roman_numbers.roman_numerals(1))          # Tests output on lower bound

    def test_roman_numerals2(self):
        self.assertEqual("V", roman_numbers.roman_numerals(5))          # Tests output on mid range

    def test_roman_numerals21(self):
        self.assertEqual("VI", roman_numbers.roman_numerals(6))        # Tests output on mid range

    def test_roman_numerals3(self):
        self.assertEqual("IX", roman_numbers.roman_numerals(9))       # Tests special case

    def test_roman_numerals4(self):
        self.assertEqual("X", roman_numbers.roman_numerals(10))     # Tests output on known value

    def test_roman_numerals42(self):
        self.assertEqual("XL", roman_numbers.roman_numerals(40))   # Tests special case

    def test_roman_numerals43(self):
        self.assertEqual("XLIX", roman_numbers.roman_numerals(49))  # Tests mid range

    def test_roman_numerals5(self):
        self.assertEqual("L", roman_numbers.roman_numerals(50))   # Tests output on known value

    def test_roman_numerals51(self):
        self.assertEqual("LX",roman_numbers.roman_numerals(60))   # Tests mid range

    def test_roman_numerals52(self):
        self.assertEqual("XC", roman_numbers.roman_numerals(90))  # Tests special case

    def test_roman_numerals53(self):
        self.assertEqual("XCIX", roman_numbers.roman_numerals(99))  # Tests mid range

    def test_roman_numerals6(self):
        self.assertEqual("C", roman_numbers.roman_numerals(100))  # Tests known value

    def test_roman_numerals62(self):
        self.assertEqual("CD", roman_numbers.roman_numerals(400))  # Tests special case

    def test_roman_numerals63(self):
        self.assertEqual("CDXCIX", roman_numbers.roman_numerals(499))  # Tests mid range

    def test_roman_numerals7(self):
        self.assertEqual("D", roman_numbers.roman_numerals(500))  # Tests known value

    def test_roman_numerals71(self):
        self.assertEqual("DC", roman_numbers.roman_numerals(600))  # Tests mid range

    def test_roman_numerals72(self):
        self.assertEqual("CM", roman_numbers.roman_numerals(900))   # Tests special case

    def test_roman_numerals73(self):
        self.assertEqual("CMXCIX", roman_numbers.roman_numerals(999))  # Tests mid range

    def test_roman_numerals8(self):
        self.assertEqual("M", roman_numbers.roman_numerals(1000))       # Tests known value

    def test_roman_numerals82(self):
        self.assertEqual("MMMM", roman_numbers.roman_numerals(4000))   # Tests mid range

    def test_roman_numerals83(self):
        self.assertEqual("MMMMMMMMMCMXCIX", roman_numbers.roman_numerals(9999))  # Tests mid range

    def test_roman_numerals9(self):
        self.assertEqual("MMMMMMMMMM", roman_numbers.roman_numerals(10000))    # Tests upper bounds




