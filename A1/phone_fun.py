def number_converter(number):
    """
    Convert letters of the alphabet into the corresponding or return the given number

    If number is a letter, will convert to a number in the form of a string, else will return a string version of given
    number
    PARAM: number, a string or an integer
    PRE-CONDITION: number must be a string or an integer
    POST-CONDITION: converts letters into a number or returns given number
    RETURN: the corresponding number as a string or the given number as a string
    """
    if number == "A" or number == "B" or number == "C":
        return str(2)
    elif number == "D" or number == "E" or number == "F":
        return str(3)
    elif number == "G" or number == "H" or number == "I":
        return str(4)
    elif number == "J" or number == "K" or number == "L":
        return str(5)
    elif number == "M" or number == "N" or number == "O":
        return str(6)
    elif number == "P" or number == "Q" or number == "R" or number == "S":
        return str(7)
    elif number == "T" or number == "U" or number == "V":
        return str(8)
    elif number == "W" or number == "X" or number == "Y" or number == "Z":
        return str(9)
    else:
        return str(number)


def number_translator():
    """
     Translate a given phone number that includes letters into the numeric version

    PRE-CONDITION: phone_number must be 10 digits and in the format XXX-XXX-XXX
    POST-CONDITION: converts each relevant index into a numeric version then concatenates them together
    RETURN: the numeric version of given phone number as a string in XXX-XXX-XXX format
    """

    phone_number = input("Input a 10 digit phone number in format XXX-XXX-XXXX: ").strip().upper()
    digit1= number_converter(phone_number[0])
    digit2= number_converter(phone_number[1])
    digit3= number_converter(phone_number[2])
    digit4= number_converter(phone_number[4])
    digit5 = number_converter(phone_number[5])
    digit6 = number_converter(phone_number[6])
    digit7 = number_converter(phone_number[8])
    digit8 = number_converter(phone_number[9])
    digit9 = number_converter(phone_number[10])
    digit10 = number_converter(phone_number[11])
    return digit1 + digit2 + digit3 + "-" + digit4 + digit5 + digit6 + "-" + digit7 + digit8 + digit9 + digit10


def main():
    """
    Drive the program
    """
    print(number_translator())


if __name__ == '__main__':
    main()



