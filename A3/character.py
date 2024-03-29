# Kyla Purcell

# A01088856

# This is the character module, it contains all functions related to character creation, healing, and classes

import random


def choose_class() -> str:
    """
    Print a message and return an inputted class.

    POST-CONDITION: prints a message about the different classes and returns the inputted class
    RETURN: A class as a string
    """
    print("""There are several classes you may choose.
    Big Chonk: A fat cat. Very strong, always hungry at 4am
    Grumpy Cat: A fierce fighter, has been unhappy since the Great War 
    Hello Kitty: A very cute,mostly android kitten. A tribute to a popular icon from the old world. 
    Robotic Cat: A prototype for the 100% technological pet, eats binary kibble.
    Great Gatsby: A stealthy, fancy tuxedo cat. It is said this is the favorite class of the developer of this world.
    Long Boi: A skinny, depraved cat. 
    Glowing One: A black cat with glowing yellow eyes. Radiation from the war has integrated into its technical parts
    Orange Julius: A ginger colored cat with a robotic eye. """)
    class1 = input("Choose your class: ").title().strip()
    if class1 == 'Big Chonk' or class1 == 'Grumpy Cat' or class1 == 'Hello Kitty':
        return class1
    elif class1 == 'Robotic Cat' or class1 == 'Great Gatsby' or class1 == 'Long Boi':
        return class1
    elif class1 == 'Glowing One' or class1 == 'Orange Julius':
        return class1
    else:
        print('You must choose one of the given classes')
        return choose_class()


def determine_dexterity(character_class: str) -> int:
    """
     Create dexterity points for a Character.

     Creates dexterity points for a character based on a random integer determined by the character's class
     PARAM: character_class, a string
     PRE-CONDITION: character_class must be a title case string
     POST-CONDITION: returns a positive integer whose range is dependant on character_class
     RETURN: Dexterity points as a integer

     >>> random.seed(2)
     >>> determine_dexterity('Orange Julius')
     1
     >>> random.seed()
     """
    if character_class == 'Big Chonk':
        return random.randint(1, 12)
    elif character_class == 'Grumpy Cat' or character_class == 'Robotic Cat' or character_class == 'Glowing One':
        return random.randint(1, 8)
    elif character_class == 'Great Gatsby' or character_class == 'Orange Julius':
        return random.randint(1, 10)
    elif character_class == 'Hello Kitty' or character_class == 'Long Boi':
        return random.randint(1, 6)


def create_character() -> dict:
    """
    Create a character.

    POST-CONDITION: Asks the users input and calls helper functions to return a character as a dictionary
    RETURN: A character, as a dictionary
    """
    character = {'Name': input('What is your name? '), 'Class': choose_class(), 'Health': 10,
                 'Dexterity': 0, 'Location': [2, 2], 'Inventory': [], 'Cursed': False}
    character['Dexterity'] = determine_dexterity(character['Class'])  # All characters start at location [2,2] and
    # have an initial health of 10 with nothing in their inventory
    return character


def character_healing(character: dict) -> None:
    """
    Heal a character.

    PARAM: character, a dictionary
    PRE-CONDITION: character, must be a full character dictionary
    POST-CONDITION: Adds one to character's health if their health is < 10 and prints output
    RETURN: None
    >>> character_healing({'Name': 'Mew', 'Class': 'Hello Kitty', 'Health': 1,\
                     'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False})
    Your health has revitalized to 2
    >>> character_healing({'Name': 'Mew', 'Class': 'Hello Kitty', 'Health': 7,\
                     'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False})
    Your health has revitalized to 8
    """
    if 10 > character['Health'] > 0:     # Only heals character until health = 10 and only if character is not dead
        character['Health'] = character['Health'] + 1
        print('Your health has revitalized to', str(character['Health']))





