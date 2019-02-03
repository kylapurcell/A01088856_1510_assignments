def time_calculator(seconds):
    """
    Convert seconds to days, hours, and minutes

    PARAM: seconds, a positive integer
    PRE-CONDITION: seconds must be a positive integer
    POST-CONDITION: gives a list with the corresponding amount of days, hours, minutes and seconds
    RETURN: a list of integers with the amount of days, hours, minutes, and seconds in that order
    """
    minutes = int(seconds/60)
    hours = int(seconds/3600)
    days = int(seconds/86400)
    return [days, hours, minutes, seconds]


def main():
    """
    Drive the program
    """
    print(time_calculator(68000))

    
if __name__ == '__main__':
    main()



