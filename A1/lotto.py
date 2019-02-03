import random


def number_generator():
    """
    Generate a unique 6 number list of integers in order from smallest to largest

    RETURN: a ordered unique list of 6 integers
    """
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
             30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
    return sorted(random.sample(list1, 6))


def main():
    """
    Drive the program
    """
    print(number_generator())


if __name__ == '__main__':
    main()


