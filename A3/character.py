import random

def choose_class():
    """
    Print a message and return an inputted class.

    POST-CONDITION: prints a message about the different classes and returns the inputted class
    RETURN: a class as a string
    """
    print("""There are several classes you may choose.
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
    class1 = input("Choose your class: ").lower().strip()
    if class1 == 'barbarian' or class1 == 'bard' or class1 == 'cleric' or class1 == 'druid' or class1 == 'fighter':
        return class1
    elif class1 == 'monk' or class1 == 'paladin' or class1 == 'ranger' or class1 == 'rogue' or class1 == 'sorcerer':
        return class1
    elif class1 == 'warlock' or class1 == 'wizard' or class1 == 'blood hunter':
        return class1
    else:
        print('You must choose one of the given classes')
        return choose_class()


def create_character():
    character = {'Name': input('What is your name? '), 'Class': 0, 'Health': 10, 'Damage': 0,
                 'Dexterity': 0, 'Location': [0, 0], 'Inventory': []}
    return character


