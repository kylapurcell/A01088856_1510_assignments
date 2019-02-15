
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
    """
    Generate a single random vowel from a list of vowels.

    POST-CONDITION: returns a random vowel from a list of vowels
    RETURN: a vowel as a string
    """
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    return random.choice(vowels)


def generate_consonant():
    """
    Generate a single random consonant from a list of consonants.

    POST-CONDITION: returns a random consonant from a list of consonants
    RETURN: a consonant as a string
    """
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P',
                  'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    return random.choice(consonants)


def generate_syllable():
    """
    Generate a random syllable made up of a vowel and a consonant.

    POST-CONDITION: concatenates a vowel and a consonant and returns a syllable
    RETURN: a syllable as a string
    """
    return generate_consonant() + generate_vowel()


def generate_name(syllables):
    """
    Generate a random name from a specified amount of syllables.

    Uses helper functions to generate a specified number of syllables into and list then concatenates them together
    PARAM: syllables, a positive integer
    PRE-CONDITION: syllables must be a positive integer
    POST-CONDITION: returns a name made up of a specified number of syllables
    RETURN: a name as a string
    """
    name = ""
    name_list = []
    while len(name_list) < syllables:
        name_list.append(generate_syllable())
    return name.join(name_list).title()


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
    """
    Create health points for a Dungeons and Dragons Character.

    Creates health points for a character by randomly rolling a die based on the character's class
    PARAM: character_class, a string
    PRE-CONDITION: character_class must be a lowercase string
    POST-CONDITION: returns a positive integer from a random die roll whose range is dependant on character_class
    RETURN: Health points as a integer
    """
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


def create_character(number_of_syllables):
    """
    Create a Dungeons and Dragons character.

    Creates a character with a randomly generated name, inputted class , health that is
    dependant on class, attribute totals generated from random dice roll, inventory and experience points.
    PARAM: number_of_syllables, an integer
    PRE-CONDITION: number_of_syllables must be a positive integer
    POST-CONDITION: returns a random dictionary containing character name, class, health , attributes, inventory, and XP
    RETURN: a randomly generated dictionary
    """
    my_character = {'Name': generate_name(number_of_syllables), 'Class': choose_class(), 'Health': 0,
                    'Strength': roll_die(3, 6), 'Dexterity': roll_die(3, 6), 'Constitution': roll_die(3, 6),
                    'Intelligence': roll_die(3, 6), 'Wisdom': roll_die(3, 6),
                    'Charisma': roll_die(3, 6), 'XP': 0, 'Inventory': []}
    class2 = my_character['Class']
    my_character['Health'] = create_health(class2)
    if number_of_syllables > 0:
        return my_character
    else:
        print("Number of syllables must be greater than zero")
        return None


def who_rolls_first():
    """
    Decide who will roll an attack first.

    Rolls a 1D20 dice for each opponent and whoever rolls higher will attack first
    POST-CONDITION: returns true or false based on which random die roll is higher
    RETURN: true or false as a boolean
    """
    opponent_one = roll_die(1, 20)
    opponent_two = roll_die(1, 20)
    if opponent_one > opponent_two:
        print('Opponent one rolled a ' + str(opponent_one) + ' and opponent two rolled a ' + str(opponent_two))
        print('Opponent one attacks first')
        return True
    elif opponent_two > opponent_one:
        print('Opponent one rolled a ' + str(opponent_one) + ' and opponent two rolled a ' + str(opponent_two))
        print('Opponent two attacks first')
        return False
    else:
        print('Opponent one rolled a ' + str(opponent_one) + ' and opponent two rolled a ' + str(opponent_two))
        print('Roll again')
        return who_rolls_first()


def attack_round(attacker, opponent):
    """
    Decide if an attack will be successful and reduce damage.

    Rolls an attack based on attacker's class and if > opponent's dexterity, will reduce opponent's
    health by that amount, if they miss or opponent is still alive, opponent gets a chance to attack.
    PARAM: attacker, a dictionary
    PARAM: opponent, a dictionary
    PRE-CONDITION: attacker must be a complete character's dictionary
    PRE-CONDITION: opponent must be a complete character's dictionary
    POST-CONDITION: Prints information about the fight and reduces health of opponent or attacker if applicable
    RETURN: None
    """
    attack_one = roll_die(1, 20)
    attack_two = roll_die(1, 20)
    damage_one = create_health(attacker['Class'])
    damage_two = create_health(opponent['Class'])
    if attack_one > opponent['Dexterity']:
        opponent['Health'] = opponent['Health'] - damage_one
        print(str(attacker['Name']) + ' rolled a ' + str(attack_one) + ' , ' + str(opponent['Name'])
              + ' has a dexterity of ' + str(opponent['Dexterity']))
        print('Attack of ' + str(damage_one) + ' was successfully struck')
        if opponent['Health'] > 0:
            print(opponent['Name'] + ' survived and gets a chance to attack')
            if attack_two > attacker['Dexterity']:
                attacker['Health'] = attacker['Health'] - damage_two
                print(str(opponent['Name']) + ' rolled a ' + str(attack_two) + ' , ' + str(attacker['Name'])
                      + ' has a dexterity of ' + str(attacker['Dexterity']))
                print('Attack of ' + str(damage_two) + ' was successfully struck')
            else:
                print(str(opponent['Name']) + ' rolled a ' + str(attack_two) + ' , ' + str(attacker['Name'])
                      + ' has a dexterity of ' + str(attacker['Dexterity']))
                print('Attack did not strike')

    else:
        print(str(attacker['Name']) + ' rolled a ' + str(attack_one) + ' , ' + str(opponent['Name'])
              + ' has a dexterity of ' + str(opponent['Dexterity']))
        print('Attack did not strike and now ' + opponent['Name'] + ' gets a chance to attack')
        if attack_two > attacker['Dexterity']:
            attacker['Health'] = attacker['Health'] - damage_two
            print(str(opponent['Name']) + ' rolled a ' + str(attack_two) + ' , ' + str(attacker['Name'])
                  + ' has a dexterity of ' + str(attacker['Dexterity']))
            print('Attack of ' + str(damage_two) + ' was successfully struck')
        else:
            print(str(opponent['Name']) + ' rolled a ' + str(attack_two) + ' , ' + str(attacker['Name'])
                  + ' has a dexterity of ' + str(attacker['Dexterity']))
            print('Attack did not strike')


def combat_round(opponent_one, opponent_two):
    """
    Engage in a single round of combat.

    Uses helper functions to decide which opponent attacks and how much damage is dealt, and then prints
    information about the status of the opponents.
    PARAM: opponent_one, a dictionary
    PARAM: opponent_two, a dictionary
    PRE-CONDITION: opponent_one must be a complete character dictionary
    PRE-CONDITION: opponent_two must be a complete character dictionary
    POST-CONDITION: Checks the value of each characters health and prints out information about the fight
    RETURN: None
    """
    if who_rolls_first():
        attack_round(opponent_one, opponent_two)
        if opponent_two['Health'] <= 0:
            print(opponent_two['Name'] + ' has died')
        elif opponent_one['Health'] <= 0:
            print(opponent_one['Name'] + ' has died')
        else:
            print('Both combatants survived the fight. ' + opponent_one['Name'] + ' now has a health of '
                  + str(opponent_one['Health']) + ' and ' + opponent_two['Name'] + ' now has a health of '
                  + str(opponent_two['Health']))
    else:
        attack_round(opponent_two, opponent_one)
        if opponent_two['Health'] <= 0:
            print(opponent_two['Name'] + ' has died')
        elif opponent_one['Health'] <= 0:
            print(opponent_one['Name'] + ' has died')
        else:
            print('Both combatants survived the fight. ' + opponent_one['Name'] + ' now has a health of '
                  + str(opponent_one['Health']) + ' and ' + opponent_two['Name'] + ' now has a health of  '
                  + str(opponent_two['Health']))


def print_character(character):
    """
    Print a Dungeons and Dragons character.

    Prints a characters name, class, health, attributes, inventory, and XP from a given character's dictionary
    PARAM: character, a dictionary
    PRE-CONDITION: character must be a complete character's dictionary
    POST-CONDITION: prints the contents of a character dictionary
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
    """
    Drive the program.
    """
    import doctest
    doctest.testmod()
    print('Welcome to dungeons and dragons, I am ' + generate_name(2) 
          + ' I will be the Dungeon Master, your trusted guide through this journey.')
    print('Lets start by creating a unique character for you to play.')
    print('First I will need you to answer a few questions before we begin.')
    character_name = int(input('How many syllables would you like for your characters name? '))
    print('Now lets talk character class')
    character = create_character(character_name)
    print('\n')
    print('Good, your character is: ')
    print_character(character)
    print('\n')
    print('Now lets roll a dice and see if something happens')
    dice_roll = int(input('how many times do you want to roll a six-sided dice? '))
    print('You rolled ' + str(roll_die(dice_roll, 6)) + "\n")
    print('Oh no several enemies appeared, pick a class to choose who you will fight: ')
    enemy = create_character(3)
    print('\n')
    print('Oh I see the enemy is: ')
    print_character(enemy)
    print('Now lets do a round of combat')
    combat_round(character, enemy)
    print('\n')
    print('One more question: ')
    inventory_selected = int(input('If your character had 10 grocery bags how many could they carry? '))
    print('\n')
    print('You awaken anew (dead or alive) in a dark forest, '
          'in front of you is a small chest with several items inside ')
    inventory_available = ['Potion', 'Gold Sword', 'Magic Ring', 'Cursed Apple',
                           'Crown', 'Staff', 'Dragon Egg', 'Blood vile', 'Bow and Arrows', 'Snacks']
    print('You slowly open the chest and find ' + str(inventory_available) + '\n')
    inventory1 = choose_inventory(inventory_available, inventory_selected)
    print('Since you told us your character could only carry ' + str(inventory_selected)
          + " items, that's what you pick up. Your new inventory is: " + str(inventory1))
    character['Inventory'] = inventory1
    print('\n')
    print('Your stats have been updated: ')
    print_character(character)


if __name__ == '__main__':
    main()



