import random


def choose_class():
    """
    Print a message and return an inputted class.

    POST-CONDITION: prints a message about the different classes and returns the inputted class
    RETURN: a class as a string
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


def create_character():
    character = {'Name': input('What is your name? '), 'Class': choose_class(), 'Health': 2, 'Damage': 0,
                 'Dexterity': 0, 'Location': [2, 2], 'Inventory': ['Unknown Item'], 'Cursed': True}
    return character


def character_healing(character):
    if 10 > character['Health'] > 0:
        character['Health'] = character['Health'] + 1
        print('Your health has revitalized to', str(character['Health']))


