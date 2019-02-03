# Kyla Purcell

# A01088856

# February 3rd 2019

# A program that generates a ordered 6 unique digit lottery number with each digit in the range of 1 to 49


import random


def number_generator():
    """
    Generate a unique 6 number list of integers in order from smallest to largest

    POST-CONDITION: List must contain unique integers in the inclusive range of [1,49]
    RETURN: a ordered unique list of 6 integers
    """
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
             30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]  # list in range [1,49]
    return sorted(random.sample(list1, 6))  # Generates a random list of length 6 ordered from smallest to largest


def main():
    """
    Drive the program
    """
    print(number_generator())


if __name__ == '__main__':
    main()


