# Kyla Purcell

# A01088856

# February 3rd 2019

# A program that converts time in seconds to various different units


def time_calculator(seconds):
    """
    Convert seconds to days, hours, and minutes

    PARAM: seconds, a positive integer
    PRE-CONDITION: seconds must be a positive integer
    POST-CONDITION: gives a list with the corresponding amount of days, hours, minutes and seconds
    RETURN: a list of integers with the amount of days, hours, minutes, and seconds in that order

    >>> time_calculator(0)
    [0, 0, 0, 0]

    >>> time_calculator(1)
    [0, 0, 0, 1]

    >>> time_calculator(31536000)
    [365, 8760, 525600, 31536000]
    """
    seconds1 = int(seconds)
    minutes = int(seconds1/60)
    hours = int(seconds1/3600)
    days = int(seconds1/86400)
    return [days, hours, minutes, seconds1]


def main():
    """
    Drive the program
    """
    import doctest
    doctest.testmod()
    print(time_calculator(68000))

    
if __name__ == '__main__':
    main()



