def how_many_ones(real_number):
    """
    Calculate how many digits are present in ones column of a given number

    PARAM: real_number, a positive integer
    PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: calculates what number is in the ones column of a given number
    RETURN: the number in the ones column as an integer

    >>> how_many_ones(0)
    0
    >>> how_many_ones(13)
    3
    """
    ones = real_number % 10
    return ones


def how_many_tens(real_number):
    """
    Calculate how many digits are present in tens column of a given number

    PARAM: real_number, a positive integer
    PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: calculates what number is in the tens column of a given number
    RETURN: the number in the tens column as a positive integer

    >>> how_many_tens(0)
    0
    >>> how_many_tens(11)
    1
    """
    tens = real_number // 10 % 10
    return tens


def how_many_hundreds(real_number):
    """
    Calculate how many digits are present in hundreds column of a given number

    PARAM: real_number, a positive integer
    PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: calculates what number is in the hundreds column of a given number
    RETURN: the number in the hundreds column as an integer
    """
    hundreds = real_number // 100 % 10
    return hundreds


def how_many_thousands(real_number):
    """
    Calculate how many digits are present in thousands column of a given number

    PARAM: real_number, a positive integer
    PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: calculates what number is in the thousands column of a given number
    RETURN: the number in the thousands column as an integer
    """
    thousands = real_number // 1000 % 10
    return thousands


def how_many_ten_thousands(real_number):
    """
    Calculate how many digits are present in ten thousands column of a given number

    PARAM: real_number, a positive integer
    PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: calculates what number is in the ten thousands column of a given number
    RETURN: the number in the thousands column as an integer
    """
    ten_thousands = real_number // 10000 % 10
    return ten_thousands


def roman_ones(real_number):
    """
    Return the corresponding roman numeral for the ones column of a given real number

    PARAM: real_number, a positive integer
    PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: calculates the corresponding roman number for the ones column
    RETURN: the roman numeral of the ones column as a string
    """
    roman1 = how_many_ones(real_number) - 5
    if roman1 < -1:
        return "I" * how_many_ones(real_number)
    elif roman1 == -1:
        return "IV"
    elif 4 > roman1 >= 0:
        return "V" + "I" * roman1
    elif roman1 == 4:
        return "IX"


def roman_tens(real_number):
    """
    Return the corresponding roman numeral for the tens column of a given real number

    PARAM: real_number, a positive integer
    PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: calculates the corresponding roman number for the tens column
    RETURN: the roman numeral of the tens column as a string
    """
    roman10 = how_many_tens(real_number) - 5
    if roman10 < -1:
        return "X" * how_many_tens(real_number)
    elif roman10 == -1:
        return "XL"
    elif 4 > roman10 >= 0:
        return "L" + "X" * roman10
    elif roman10 == 4:
        return "XC"


def roman_hundreds(real_number):
    """
    Return the corresponding roman numeral for the hundreds column of a given real number

    PARAM: real_number, a positive integer
    PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: calculates the corresponding roman number for the hundreds column
    RETURN: the roman numeral of the hundreds column as a string
    """
    roman100 = how_many_hundreds(real_number) - 5
    if roman100 < -1:
        return "C" * how_many_hundreds(real_number)
    elif roman100 == -1:
        return "CD"
    elif 4 > roman100 >= 0:
        return "D" + "C" * roman100
    elif roman100 == 4:
        return "CM"


def roman_thousands(real_number):
    """
     Return the corresponding roman numeral for the thousands column of a given real number

     PARAM: real_number, a positive integer
     PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
     POST-CONDITION: calculates the corresponding roman number for the thousands column
     RETURN: the roman numeral of the thousands column as a string
     """
    return "M" * how_many_thousands(real_number)


def roman_ten_thousands(real_number):
    """
    Return the corresponding roman numeral for the ten thousands column of a given real number

    PARAM: real_number, a positive integer
    PRE-CONDITION: real number must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: calculates the corresponding roman number for the ten thousands column
    RETURN: the roman numeral of the ten thousands column as a string
    """
    return "M" * how_many_ten_thousands(real_number) * 10


def roman_numerals(positive_int):
    """
    Return the corresponding roman numeral for a given real number

    PARAM: positive_int, a positive integer
    PRE-CONDITION: positive_int must be a positive integer in the inclusive range(1,10000)
    POST-CONDITION: concatenates the corresponding roman numerals for each column
    RETURN: the corresponding roman numeral as a string
    """
    return roman_ten_thousands(positive_int) + roman_thousands(positive_int) \
           + (roman_hundreds(positive_int)) + roman_tens(positive_int) + roman_ones(positive_int)


def main():
    """
    Drive the program
    """
    print(roman_numerals(1789))


if __name__ == '__main__':
    main()





