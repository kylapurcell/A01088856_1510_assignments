# Kyla Purcell

# A01088856

# February 3rd 2019

# A program that converts real numbers in the range 1-10,000 into roman numerals


def how_many_ones(real_number):
    """
    Calculate how many digits are present in ones column of a given number

    PARAM: real_number, a positive integer
    PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: calculates what number is in the ones column of a given number
    RETURN: the number in the ones column as an integer

    >>> how_many_ones(1)
    1
    >>> how_many_ones(13)
    3
    >>> how_many_ones(10000)
    0
    """
    ones = real_number % 10  # Uses remainder to calculate what number in ones column
    return ones


def how_many_tens(real_number):
    """
    Calculate how many digits are present in tens column of a given number

    PARAM: real_number, a positive integer
    PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: calculates what number is in the tens column of a given number
    RETURN: the number in the tens column as a positive integer

    >>> how_many_tens(1)
    0
    >>> how_many_tens(11)
    1
    >>> how_many_tens(10000)
    0
    """
    tens = real_number // 10 % 10  # Uses remainder to calculate what number in tens column
    return tens


def how_many_hundreds(real_number):
    """
    Calculate how many digits are present in hundreds column of a given number

    PARAM: real_number, a positive integer
    PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: calculates what number is in the hundreds column of a given number
    RETURN: the number in the hundreds column as an integer
    
    >>> how_many_hundreds(1)
    0
    >>> how_many_hundreds(400)
    4
    >>> how_many_hundreds(10000)
    0
    """
    hundreds = real_number // 100 % 10  # Uses remainder to calculate what number in hundreds column
    return hundreds


def how_many_thousands(real_number):
    """
    Calculate how many digits are present in thousands column of a given number

    PARAM: real_number, a positive integer
    PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: calculates what number is in the thousands column of a given number
    RETURN: the number in the thousands column as an integer

    >>> how_many_thousands(1)
    0
    >>> how_many_thousands(6000)
    6
    >>> how_many_thousands(10000)
    0
    """
    thousands = real_number // 1000 % 10  # Uses remainder to calculate what number in thousands column
    return thousands


def how_many_ten_thousands(real_number):
    """
    Calculate how many digits are present in ten thousands column of a given number

    PARAM: real_number, a positive integer
    PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: calculates what number is in the ten thousands column of a given number
    RETURN: the number in the thousands column as an integer

    >>> how_many_ten_thousands(1)
    0
    >>> how_many_ten_thousands(3000)
    0
    >>> how_many_ten_thousands(10000)
    1
    """
    ten_thousands = real_number // 10000 % 10  # Uses remainder to calculate what number in ten thousands column
    return ten_thousands


def roman_ones(real_number):
    """
    Return the corresponding roman numeral for the ones column of a given real number

    PARAM: real_number, a positive integer
    PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: calculates the corresponding roman number for the ones column
    RETURN: the roman numeral of the ones column as a string

    >>> roman_ones(1)
    'I'
    >>> roman_ones(4)
    'IV'
    >>> roman_ones(5)
    'V'
    >>> roman_ones(6)
    'VI'
    >>> roman_ones(9)
    'IX'
    """
    roman1 = how_many_ones(real_number) - 5  # calculates the difference to determine what roman numeral
    if roman1 < -1:
        return "I" * how_many_ones(real_number)
    elif roman1 == -1:  # If difference is -1, ones number = 4 so special case
        return "IV"
    elif 4 > roman1 >= 0:
        return "V" + "I" * roman1
    elif roman1 == 4:  # If difference is 4, ones number = 9, so special case
        return "IX"


def roman_tens(real_number):
    """
    Return the corresponding roman numeral for the tens column of a given real number

    PARAM: real_number, a positive integer
    PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: calculates the corresponding roman number for the tens column
    RETURN: the roman numeral of the tens column as a string

    >>> roman_tens(10)
    'X'
    >>> roman_tens(40)
    'XL'
    >>> roman_tens(50)
    'L'
    >>> roman_tens(60)
    'LX'
    >>> roman_tens(90)
    'XC'
    """
    roman10 = how_many_tens(real_number) - 5  # calculates the difference to determine what roman numeral
    if roman10 < -1:
        return "X" * how_many_tens(real_number)
    elif roman10 == -1:  # If difference is -1, tens number = 40, so special case
        return "XL"
    elif 4 > roman10 >= 0:
        return "L" + "X" * roman10
    elif roman10 == 4:  # If difference is 4, tens number = 90, so special case
        return "XC"


def roman_hundreds(real_number):
    """
    Return the corresponding roman numeral for the hundreds column of a given real number

    PARAM: real_number, a positive integer
    PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: calculates the corresponding roman number for the hundreds column
    RETURN: the roman numeral of the hundreds column as a string

    >>> roman_hundreds(100)
    'C'
    >>> roman_hundreds(400)
    'CD'
    >>> roman_hundreds(500)
    'D'
    >>> roman_hundreds(600)
    'DC'
    >>> roman_hundreds(900)
    'CM'
    """
    roman100 = how_many_hundreds(real_number) - 5  # calculates the difference to determine what roman numeral
    if roman100 < -1:
        return "C" * how_many_hundreds(real_number)
    elif roman100 == -1:  # If difference is -1, hundreds number = 400, so special case
        return "CD"
    elif 4 > roman100 >= 0:
        return "D" + "C" * roman100
    elif roman100 == 4:  # If difference is 4, hundreds number = 900, so special case
        return "CM"


def roman_thousands(real_number):
    """
     Return the corresponding roman numeral for the thousands column of a given real number

     PARAM: real_number, a positive integer
     PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
     POST-CONDITION: calculates the corresponding roman number for the thousands column
     RETURN: the roman numeral of the thousands column as a string

     >>> roman_thousands(1)
     ''
     >>> roman_thousands(1000)
     'M'
     >>> roman_thousands(5000)
     'MMMMM'
     """
    return "M" * how_many_thousands(real_number)  # Thousands roman numerals depends only on how_many_thousands


def roman_ten_thousands(real_number):
    """
    Return the corresponding roman numeral for the ten thousands column of a given real number

    PARAM: real_number, a positive integer
    PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: calculates the corresponding roman number for the ten thousands column
    RETURN: the roman numeral of the ten thousands column as a string

    >>> roman_ten_thousands(1)
    ''
    >>> roman_ten_thousands(5000)
    ''
    >>> roman_ten_thousands(10000)
    'MMMMMMMMMM'
    """
    return "M" * how_many_ten_thousands(real_number) * 10  # Ten Thousands numeral is ten thousands number times 10


def roman_numerals(positive_int):
    """
    Return the corresponding roman numeral for a given real number

    PARAM: positive_int, a positive integer
    PRE-CONDITION: positive_int must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: concatenates the corresponding roman numerals for each column
    RETURN: the corresponding roman numeral as a string

    >>> roman_numerals(1)
    'I'
    >>> roman_numerals(25)
    'XXV'
    >>> roman_numerals(560)
    'DLX'
    >>> roman_numerals(4545)
    'MMMMDXLV'
    >>> roman_numerals(10000)
    'MMMMMMMMMM'
    """
    return roman_ten_thousands(positive_int) + roman_thousands(positive_int) \
           + (roman_hundreds(positive_int)) + roman_tens(positive_int) + roman_ones(positive_int)


def main():
    """
    Drive the program
    """
    import doctest
    doctest.testmod()
    print(roman_numerals(1789))


if __name__ == '__main__':
    main()
