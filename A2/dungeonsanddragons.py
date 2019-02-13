
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
    class1 = input("Choose your class: ").lower()
    if class1 == 'barbarian' or class1 == 'bard' or class1 == 'cleric' or class1 == 'druid' or class1 == 'fighter':
        return class1
    elif class1 == 'monk' or class1 == 'paladin' or class1 == 'ranger' or class1 == 'rogue' or class1 == 'sorcerer':
        return class1
    elif class1 == 'warlock' or class1 == 'wizard' or class1 == 'blood hunter':
        return class1
    else:
        print('You must choose one of the given classes')
        return choose_class()


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


def attack_round(attacker, opponent):
    attack_roll = create_health(attacker['Class'])
    if attack_roll > opponent['Dexterity']:
        print(str(attacker['Name']) + ' attacked with a roll of ' + str(attack_roll) + ' , ' + str(opponent['Name'])
              + ' has a dexterity of ' + str(opponent['Dexterity']))
        print('Attack was successfully struck')
        return attack_roll
    elif attack_roll <= opponent['Dexterity']:
        print(str(attacker['Name']) + ' attacked with a roll of ' + str(attack_roll) + ' , ' + str(opponent['Name'])
              + ' has a dexterity of ' + str(opponent['Dexterity']))
        print('Attack did not strike')
        return 0


def combat_round(opponent_one, opponent_two):
    if who_rolls_first():
        attack1 = attack_round(opponent_one, opponent_two)
        print('Attack equals ' + str(attack1))
        opponent_two['Health'] = opponent_two['Health'] - attack1
        if opponent_two['Health'] <= 0:
            print(opponent_two['Name'] + ' has died')
        else:
            print(opponent_two['Name'] + ' survived but their health is now ' + str(opponent_two['Health']))
    else:
        attack2 = attack_round(opponent_two, opponent_one)
        print('Attack equals ' + str(attack2))
        opponent_one['Health'] = opponent_one['Health'] - attack2
        if opponent_one['Health'] <= 0:
            print(opponent_one['Name'] + ' has died')
        else:
            print(opponent_one['Name'] + ' survived but their health is now ' + str(opponent_one['Health']))


def print_character(character):
    """
    Print a Dungeons and Dragons character.

    Prints a characters name, attributes and possible inventory from a given character's list
    PARAM: character, a list
    PRE-CONDITION: character must be of length 7 or 8
    POST-CONDITION: prints the contents of a character list with attributes and an inventory if available
    RETURN: None
    """
    name = 'Name: ' + str(character['Name']) + "\n"
    character_class = 'Class: ' + str(character['Class']) + "\n"
    health = 'Health: ' + str(character['Health']) + "\n"
    strength = 'Strength: ' + str(character['Strength']) + "\n"
    dexterity = 'Dexterity: ' + str(character['Dexterity']) + "\n"
    constitution = 'Constitution: ' + str(character['Constitution']) + "\n"
    intelligence = 'Intelligence: ' + str(character['Intelligence']) + "\n"
    wisdom = 'Wisdom: ' + str(character['Wisdom']) + "\n"
    charisma = 'Charisma: ' + str(character['Charisma']) + "\n"
    xp = 'XP: ' + str(character['XP']) + "\n"
    inventory = 'Inventory: ' + str(character['Inventory'])
    print(name + character_class + health + strength + dexterity
          + constitution + intelligence + wisdom + charisma + xp + inventory)


def main():
    print('Welcome to dungeons and dragons, I am ' + generate_name(2) 
          + ' I will be the Dungeon Master, your trusted guide through this journey.')
    print('Lets start by creating a unique character for you to play.')
    print('First I will need you to answer a few questions before we begin.')
    character_name = int(input('How many syllables would you like for your characters name? '))
    print('Now lets talk character class')
    character = create_character(character_name)
    print('Good, your character is: ')
    print_character(character)
    print('\n')
    print('Now lets roll a dice and see if something happens')
    dice_roll = int(input('how many times do you want to roll a six-sided dice? '))
    print('You rolled ' + str(roll_die(dice_roll, 6)) + "\n")
    print('Oh no several enemies appeared, pick a class to choose who you will fight: ')
    enemy = create_character(3)
    print('Oh I see the enemy is: ')
    print_character(enemy)
    print('Now lets do a round of combat')
    combat_round(character, enemy)
    print('\n')
    print('One more question: ')
    inventory_selected = int(input('If your character had 10 grocery bags how many could they carry? '))
    print('\n')
    print('You awaken anew in a dark forest, in front of you is a small chest with several items inside ')
    inventory_available = ['Potion', 'Gold Sword', 'Magic Ring', 'Cursed Apple',
                           'Crown', 'Staff', 'Dragon Egg', 'Blood vile', 'Bow and Arrows', 'Snacks']
    print('You slowly open the chest and find ' + str(inventory_available) + '\n')
    inventory1 = choose_inventory(inventory_available, inventory_selected)
    print('Since you told us your character could only carry ' + str(inventory_selected)
          + " items, that's what you pick up. Your new inventory is: " + str(inventory1))
    character['Inventory'] = inventory1
    print('Your stats have been updated: ')
    print_character(character)


main()
