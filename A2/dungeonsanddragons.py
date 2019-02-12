
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


def generate_consonant():
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P',
                  'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    return random.choice(consonants)


def generate_syllable():
    return generate_consonant() + generate_vowel()


def generate_name(syllables):
    name = ""
    name_list = []
    while len(name_list) < syllables:
        name_list.append(generate_syllable())
    return name.join(name_list).title()


def choose_class():
    print("""There are several classes you may choose for your character.
    Barbarian: A fierce warrior of primitive background
    Bard : An inspiring magician 
    Cleric : A priestly champion 
    Druid: A priest of old faith
    Fighter: A master of martial arts combat
    Monk: A master of the mind and body
    Paladin: A holy warrior bound to a sacred oath
    Ranger: A warrior who combats threats on the edges of civilization
    Rogue: A scoundrel who uses stealth and trickery
    Sorcerer: A spell caster with inherited magic
    Warlock: A wielder of magic given from a bargain
    Wizard: A scholarly magic-user
    Blood Hunter: A fanatical slayer, similar to Dark Souls Bloodborne""")
    class1 = input("Choose your class: ").lower()
    if class1 == 'barbarian' or class1 == 'bard' or class1 == 'cleric' or class1 == 'druid' or class1 == 'fighter':
        return class1
    elif class1 == 'monk' or class1 == 'paladin' or class1 == 'ranger' or class1 == 'rogue' or class1 == 'sorcerer':
        return class1
    elif class1 == 'warlock' or class1 == 'wizard' or class1 == 'blood hunter':
        return class1
    else:
        print('You must choose one of the given classes')
        return None


def create_health(character_class):
    if character_class == 'barbarian':
        return roll_die(1, 12)
    elif character_class == 'bard' or character_class == 'cleric' or character_class == 'druid':
        return roll_die(1, 8)
    elif character_class == 'monk' or character_class == 'warlock' or character_class == 'rogue':
        return roll_die(1, 8)
    elif character_class == 'fighter' or character_class == 'paladin' or character_class == 'ranger':
        return roll_die(1, 10)
    elif character_class == 'blood hunter':
        return roll_die(1, 10)
    elif character_class == 'wizard' or character_class == 'sorcerer':
        return roll_die(1, 6)
    else:
        return None


def create_character(name_length):
    """
    Create a Dungeons and Dragons character.

    Creates a character with a randomly generated name and attribute totals generated from random dice roll
    PARAM: name_length, an integer
    PRE-CONDITION: name_length must be a positive integer
    POST-CONDITION: returns a random list containing character name, and lists of attributes
    RETURN: a random list containing character name as a string and attributes as two item lists
    """
    my_character = {'Name': generate_name(name_length), 'Class': choose_class(), 'Health': 0,
                    'Strength': roll_die(3, 6), 'Dexterity': roll_die(3, 6), 'Constitution': roll_die(3, 6),
                    'Intelligence': roll_die(3, 6), 'Wisdom': roll_die(3, 6),
                    'Charisma': roll_die(3, 6), 'XP': 0, 'Inventory': []}
    class2 = my_character['Class']
    my_character['Health'] = create_health(class2)
    if name_length > 0:
        return my_character
    else:
        print("Name length must be greater than zero")
        return None


def who_rolls_first():
    opponent_one = roll_die(1, 20)
    opponent_two = roll_die(1, 20)
    if opponent_one > opponent_two:
        print('Opponent one rolled a ' + str(opponent_one) + ' and opponent two rolled a ' + str(opponent_two))
        print('Opponent one rolls first')
        return True
    elif opponent_two > opponent_one:
        print('Opponent one rolled a ' + str(opponent_one) + ' and opponent two rolled a ' + str(opponent_two))
        print('Opponent two rolls first')
        return False
    else:
        print('Opponent one rolled a ' + str(opponent_one) + ' and opponent two rolled a ' + str(opponent_two))
        print('Roll again')
        return who_rolls_first()




#def combat_round(opponent_one,opponent_two):


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

