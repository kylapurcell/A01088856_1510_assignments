
def how_many_ones(x):
    y = x % 10
    return y


def how_many_tens(x):
    y = x//10 % 10
    return y


def how_many_hundreds(x):
    y = x//100 % 10
    return y


def how_many_thousands(x):
    y = x//1000 % 10
    return y


def how_many_ten_thousands(x):
    y = x//10000 % 10
    return y


def roman_ones(x):
    y = how_many_ones(x)- 5
    if y < -1:
        return "I" * how_many_ones(x)
    elif y == -1:
        return "IV"
    elif 4 > y >= 0:
        return "V" + "I" * abs(y)
    elif y == 4:
        return "IX"


def roman_tens(x):
    y = how_many_tens(x) - 5
    if y < -1:
        return "X" * how_many_tens(x)
    elif y == -1:
        return "XL"
    elif 4 > y >= 0:
        return "L" + "X" * abs(y)
    elif y == 4:
        return "XC"


def roman_hundreds(x):
    y = how_many_hundreds(x) - 5
    if y < -1:
        return "C" * how_many_hundreds(x)
    elif y == -1:
        return "CD"
    elif 4 > y >= 0:
        return "D" + "C" * abs(y)
    elif y == 4:
        return "CM"


def roman_thousands(x):
    y = how_many_thousands(x) - 5
    if y < -1:
        return "M" * how_many_thousands(x)
    elif y == -1:
        return "MV"
    elif 4 > y >= 0:
        return "|V|" + "M" * abs(y)
    elif y == 4:
        return "M|X|"

def roman_ten_thousands(x):
    y = how_many_ten_thousands(x) - 5
    if y < -1:
        return "|X|" * how_many_ten_thousands(x)


def roman_numerals():
    c = int(input(" Input an integer to convert to a roman numeral: "))
    return  roman_ten_thousands(c) + roman_thousands(c) + (roman_hundreds(c)) + roman_tens(c) + roman_ones(c)


print(roman_numerals())







