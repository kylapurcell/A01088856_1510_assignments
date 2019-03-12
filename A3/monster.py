import random
import character


def monster_class_choice():
    """
    Determine what type of monster will appear.

    What kind of monster that appears is dependant on a random number between 1 and 4,
    an extra rare monster may appear if a number between 1 and 60 is chosen
    POST-CONDITION: Based on two random integers determines which monster class will be returned
    RETURN: Monster's name as a string
    >>> random.seed(4)
    >>> monster_class_choice()
    'Radioactive Rat'
    >>> random.seed(2)
    >>> monster_class_choice()
    'Ghoul'
    >>> random.seed()
    """
    normal_chance = random.randint(1, 4)   # Determines which monster will appear
    rare_chance = random.randint(1, 60)   # One in 60 chance of Pax appearing if monster encounter occurs
    if rare_chance == 50:
        return 'Pax'
    elif normal_chance == 1:
        return 'Ghoul'
    elif normal_chance == 2:
        return 'Radioactive Rat'
    elif normal_chance == 3:
        return 'Rogue Robot'
    elif normal_chance == 4:
        return 'Mutated Creature'


def monster_dexterity(class_type):
    """
    Calculate monster dexterity based on class.

    PARAM: class_type, a string
    PRE-CONDITION: class_type must be a string
    POST-CONDITION: Based on two random integers determines which monster class will be returned
    RETURN: Monster's dexterity as an integer
    >>> random.seed(5)
    >>> monster_dexterity('Ghoul')
    5
    >>> monster_dexterity('Pax')
    3
    >>> random.seed()
    """
    if class_type == 'Radioactive Rat' or class_type == 'Rogue Robot':
        return random.randint(1, 4)
    elif class_type == 'Mutated Creature' or 'Ghoul':
        return random.randint(1, 6)
    elif class_type == 'Pax':
        return random.randint(1, 20)


def monster_about():
    """
    Print information about the monsters of this world.

    POST-CONDITION: Prints output containing information about the monsters of the game
    RETURN: None
    """
    print("""The Monster Encyclopedia:
      Ghoul: Radioactive, humanoid creature with green flesh. Rumored to be whats left of humans.
      Radioactive Rat : An over sized rat. Sometimes a tasty snack for certain cat species.
      Rogue Robot: A robot with glitched programming. 
      Mutated Creature: Mutated beyond belief. Hard to tell what this creature is. 
      Pax: The demon thief of destiny. Feared by all and said to curse those unlucky enough to meet him.""")


def generate_monster():
    """
    Generate a monster.

    POST-CONDITION: Creates a monster based on random type choice and dexterity helper functions
    RETURN:  a monster, as a dictionary
    >>> random.seed(3)
    >>> generate_monster()
    {'Name': 'Radioactive Rat', 'Health': 5, 'Damage': 2, 'Dexterity': 3}
    >>> random.seed()
    """
    monster = {'Name': monster_class_choice(), 'Health': 5,
               'Damage': random.randint(1, 4), 'Dexterity': 0}  # All monsters have 5 health,
    # dexterity dependant on name and damage of (1 to 4) if user runs away.
    # Note monsters will do (1 to 6) damage in a fight
    class2 = monster['Name']
    monster['Dexterity'] = monster_dexterity(class2)
    return monster


def attack_round(attacker, opponent):
    """
    Decide if an attack will be successful.

    Rolls an attack and if it is > opponent's dexterity, will return the attack value
    PARAM: attacker, a dictionary
    PARAM: opponent, a dictionary
    PRE-CONDITION: attacker must be a dictionary
    PRE-CONDITION: opponent must be a dictionary
    POST-CONDITION: Prints output and modifies the health of the opponent if attack successful
    RETURN: None
    >>> random.seed(2)
    >>> attack_round({'Name': 'Pikachu', 'Class': 'Hello Kitty', 'Health': 10,\
                     'Dexterity': 4, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}, \
                     {'Name': 'Ghoul', 'Health': 5,\
               'Damage': 3, 'Dexterity': 3})
    Pikachu has a chance to attack
    Attack missed
    >>> random.seed()
    """
    attack_roll = random.randint(1, 20)   # For attack to strike this number must be greater then opponent dexterity
    damage = random.randint(1, 6)  # Monsters and characters both do damage from (1 to 6) if they strike
    print(str(attacker['Name']), 'has a chance to attack')
    if attack_roll > opponent['Dexterity']:
        opponent['Health'] = opponent['Health'] - damage
        print(attacker['Name'] + ' attacked with damage of ' + str(damage))
    elif attack_roll <= opponent['Dexterity']:
        print('Attack missed')


def monster_run_away(my_character, monster):
    """
    Decide if damage occurs while fleeing.


    PARAM: attacker, a dictionary
    PARAM: opponent, a dictionary
    PRE-CONDITION: attacker must be a dictionary
    PRE-CONDITION: opponent must be a dictionary
    POST-CONDITION: Prints output and has 1 in 10 chance of subtracting damage from character's health
    RETURN: None
    >>> random.seed(3)
    >>> monster_run_away({'Name': 'Charmander', 'Class': 'Hello Kitty', 'Health': 10,\
                              'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False},\
                              {'Name': 'Ghoul', 'Health': 5, 'Damage': 0, 'Dexterity': 7})
    You escaped successfully and without a scratch too
    >>> random.seed()
    """
    chance_damage = random.randint(1, 10)   # Monsters have 10% chance of damaging a player as they run
    if chance_damage == 5:
        my_character['Health'] = my_character['Health'] - monster['Damage']
        print(str(monster['Name']), 'attacked as you were running away with a attack of', str(monster['Damage']),
              'your health is now', str(my_character['Health']))
        if my_character['Health'] < 0:
            print('You died')
        else:
            print('You survived to fight another day')
    else:
        print('You escaped successfully and without a scratch too')


def monster_encounter(random_monster, user_character):
    """
    Encounter a monster.


    PARAM: random_monster, a dictionary
    PARAM: user_character, a dictionary
    PRE-CONDITION: random_monster must be a dictionary
    PRE-CONDITION: user_character must be a dictionary
    POST-CONDITION: Prints output and modifies the character's cursed value if a rare monster appears
    RETURN: None
    >>> monster_encounter({'Name': 'Pax', 'Health': 5, 'Damage': 0, 'Dexterity': 7},{'Name': 'Charmander', \
    'Class': 'Hello Kitty', 'Health': 10,'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False})
    Pax appeared!
    You have encountered the demon thief of destiny
    ^( Ծ^6^Ծ )^
    """
    print(random_monster['Name'], 'appeared!')
    if random_monster['Name'] == 'Pax':
        user_character['Cursed'] = True  # If pax appears it curses the character and a unique message appears
        print('You have encountered the demon thief of destiny')
        print('^( Ծ^6^Ծ )^')


def monster_combat(my_character, monster):
    """
    Engage in combat to the death.

    PARAM: my_character, a dictionary
    PARAM: monster, a dictionary
    PRE-CONDITION: monster must be a dictionary
    PRE-CONDITION: my_character must be a dictionary
    POST-CONDITION: Prints output and reduces character/monster health until one reaches 0
    RETURN: None
    >>> random.seed(4)
    >>> monster_combat({'Name': 'Charmander', 'Class': 'Hello Kitty', 'Health': 10,\
                              'Dexterity': 3, 'Location': [0, 2], 'Inventory': [], 'Cursed': False},\
                              {'Name': 'Ghoul', 'Health': 5, 'Damage': 2, 'Dexterity': 2})
    Charmander has a chance to attack
    Charmander attacked with damage of 3
    Ghoul now has a health of 2
    Ghoul has a chance to attack
    Ghoul attacked with damage of 6
    Charmander now has a health of 4
    Charmander has a chance to attack
    Charmander attacked with damage of 4
    Ghoul now has a health of -2
    Ghoul has died
    >>> random.seed()
    """
    while my_character['Health'] > 0:
            attack_round(my_character, monster)
            print(monster['Name'] + ' now has a health of ' + str(monster['Health']))
            if monster['Health'] <= 0:
                print(monster['Name'] + ' has died')
                break                                # If the monster dies the combat ends
            elif monster['Health'] > 0:
                attack_round(monster, my_character)
                print(my_character['Name'] + ' now has a health of ' + str(my_character['Health']))
    else:
        print(my_character['Name'] + ' has died')  # If the player dies the combat ends


def monster_fight(my_character, monster):
    """
     Decide the outcome of a monster encounter.

    PARAM: my_character, a dictionary
    PARAM: monster, a dictionary
    PRE-CONDITION: monster must be a dictionary
    PRE-CONDITION: my_character must be a dictionary
    POST-CONDITION: Takes user input and calls functions based on user choice
    RETURN: None
    """
    monster_encounter(monster, my_character)
    choice = input(' Would you like to run away or fight? (type run or fight) ').lower().strip()
    if choice == 'run':
        monster_run_away(my_character, monster)   # Calls run function
    elif choice == 'fight':
        monster_combat(my_character, monster)  # Calls fight function
    else:
        print('You must run or fight')
        return monster_fight(my_character, monster)
        # Recursion: Player must pick run or fight if they encounter a monster











