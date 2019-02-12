
import random


def roll_die(number_of_rolls, number_of_sides):
        """
        Simulate the rolling of a die a specified number of times with a specified number of sides.

        Calculates a random total with range dependant on number_of_rolls and number_of_sides
        PARAM: number_of_rolls: a positive integer
        PARAM: number_of_sides: a positive integer
        PRE-CONDITION: number_of_rolls must be an integer > 0
        PRE-CONDITION: number_of_sides must be an integer > 0
        POST-CONDITION: returns a random sum of a die rolled a specified number of times with specified number of sides
        RETURN: a random total as a positive integer
        """
        range_roll_1 = number_of_rolls        # Min total is the rolls
        range_roll_2 = number_of_sides*number_of_rolls   # Max total is sides * rolls
        if number_of_rolls > 0 and number_of_sides > 0:
            return random.randint(range_roll_1, range_roll_2)   # Generates random total with in (min,max) range
        else:
            return 0     # Returns zero if rolls and sides = zero


def choose_inventory(inventory, selection):
    """
    Create an inventory list based on a given list and number of items to be selected.

    Creates a list of inventory items from a given list of a length of a given integer
    PARAM: inventory, a list
    PARAM: selection, an integer
    PRE-CONDITION: selection must be =< the length of inventory
    PRE-CONDITION: selection must be > 0
    POST-CONDITION: returns a sorted list of inventory items with length of selection
    RETURN: a sorted list with length of selection or a copy of the given list
    """
    if inventory == [] and selection == 0:        # an empty list and selection of zero returns empty list
        return []
    elif selection < 0:
        print(" you cannot have a selection less than zero")
        return None
    elif selection > len(inventory):
        print(" Your selection cannot be greater than the inventory length")
        return None
    elif selection == len(inventory):        # Selection is equal to list length a copy of inventory will be returned
        return inventory[:]
    else:
        return sorted(list(random.choices(inventory, k=selection)))


def generate_vowel():
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    return random.choice(vowels)


def create_character(name_length):
    """
    Create a Dungeons and Dragons character.

    Creates a character with a randomly generated name and attribute totals generated from random dice roll
    PARAM: name_length, an integer
    PRE-CONDITION: name_length must be a positive integer
    POST-CONDITION: returns a random list containing character name, and lists of attributes
    RETURN: a random list containing character name as a string and attributes as two item lists
    """
    list1 = ["Strength", roll_die(3, 6)]        # Determines attributes based on 3 rolls of a six sided die
    list2 = ["Dexterity", roll_die(3, 6)]
    list3 = ["Constitution", roll_die(3, 6)]   # Attributes are selected this way from D&D 3d6 rule
    list4 = ["Intelligence", roll_die(3, 6)]
    list5 = ["Wisdom", roll_die(3, 6)]
    list6 = ["Charisma", roll_die(3, 6)]
    list_final = [create_name(name_length), list1, list2, list3, list4, list5, list6]
    if name_length > 0:
        return list_final
    else:
        print("Name length must be greater than zero")
        return None


def print_character(character):
    """
    Print a Dungeons and Dragons character.

    Prints a characters name, attributes and possible inventory from a given character's list
    PARAM: character, a list
    PRE-CONDITION: character must be of length 7 or 8
    POST-CONDITION: prints the contents of a character list with attributes and an inventory if available
    RETURN: None
    """
    name = 'Name: ' + str(character[0]) + "\n"
    strength = 'Strength: ' + str(character[1][1]) + "\n"  # Prints name and attributes on multiple lines
    dexterity = 'Dexterity: ' + str(character[2][1]) + "\n"
    constitution = 'Constitution: ' + str(character[3][1]) + "\n"
    intelligence = 'Intelligence: ' + str(character[4][1]) + "\n"
    wisdom = 'Wisdom: ' + str(character[5][1]) + "\n"
    charisma = 'Charisma: ' + str(character[6][1])
    if len(character) > 7:
        inventory = "\n" + 'Inventory : ' + str(character[7])  # If inventory is in character it will be printed too
        print(name + strength + dexterity + constitution + intelligence + wisdom + charisma + inventory)

    else:
        print(name + strength + dexterity + constitution + intelligence + wisdom + charisma)

