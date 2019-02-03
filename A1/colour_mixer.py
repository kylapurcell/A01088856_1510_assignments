# Kyla Purcell

# A01088856

# February 3rd 2019

# A program that prints the color that results from mixing two given primary colors


def primary_color(color1, color2):
    """
    Return the resulting color from mixing two primary colors

    PARAM: color1, a string
    PARAM: color2, a string
    PRE-CONDITION: color1 != color2 and must be a lowercase string containing the colors red, blue, or yellow
    PRE-CONDITION: color2 != color1 and must be a lowercase string containing the colors red, blue, or yellow
    POST-CONDITION: gives the color that results from the mixture of given colors
    RETURN: the resultant color as a string in lowercase or a message to correct user input as a string

    >>> primary_color("red", "blue")
    'purple'

    >>> primary_color("red", "yellow")
    'orange'

    >>> primary_color("blue", "yellow")
    'green'

    """
    if color1 == "red" and color2 == "blue":
        return "purple"
    elif color1 == "blue" and color2 == "red":
        return "purple"
    elif color1 == "red" and color2 == "yellow":
        return "orange"
    elif color1 == "yellow" and color2 == "red":
        return "orange"
    elif color1 == "yellow" and color2 == "blue":
        return "green"
    elif color1 == "blue" and color2 == "yellow":
        return "green"
    elif color1 == color2:                                  # if two colors are the same returns a helpful message
        return "Your chosen colors must be different"
    else:
        return "Your chosen colors must be primary colors (red,blue,yellow)"  # if given colors != red, blue, yellow


def color_mixer():
    """
    Receive user input then give the resulting color from mixing two primary colors

    Uses helper function to find the resultant color from the user inputted primary colors
    RETURN: the resultant color as a string
    """
    first_color = input("input your first color: ").strip()    # takes user input and strips any whitespace
    second_color = input("input your second color: ").strip()
    return primary_color(first_color.lower(), second_color.lower())  # ensures user input is in lower case


def main():
    """
    Drive the program
    """
    import doctest
    doctest.testmod()
    print(color_mixer())


if __name__ == '__main__':
    main()



