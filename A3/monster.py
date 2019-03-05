import random
import character


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

        >>> random.seed(1)
        >>> roll_die(1, 20)
        5
        >>> roll_die(3,6)
        5
        >>> random.seed()
        """
        range_roll_1 = number_of_rolls        # Min total is the rolls
        range_roll_2 = number_of_sides*number_of_rolls   # Max total is sides * rolls
        if number_of_rolls > 0 and number_of_sides > 0:
            return random.randint(range_roll_1, range_roll_2)   # Generates random total with in (min,max) range
        else:
            return 0     # Returns zero if rolls and sides = zero


def monster_class_choice():
    """
    What kind of monster that appears is dependant on a random number between 1 and 4,
    an extra rare monster may appear if a number between 1,100 is chosen
    :return:
    """
    normal_chance = random.randint(1, 4)
    rare_chance = random.randint(1, 100)
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


def monster_class_perk(class_type):
    """
    If a monster is a rare class a identifier will be added to the dictionary for special events to occur
    :param class_type:
    :return:
    """
    if class_type == 'Pax':
        return 1
    else:
        return 0


def monster_dexterity(class_type):
    if class_type == 'Radioactive Rat' or class_type == 'Rogue Robot':
        return roll_die(3, 4)
    elif class_type == 'Mutated Creature' or 'Ghoul':
        return roll_die(3, 6)
    elif class_type == 'Pax':
        return roll_die(3, 8)


def monster_about():
    """
    Print information about the monsters of this world
    :return:
    """


def generate_monster():
    """
    Generate a monster.
    :return:
    """
    monster = {'Name': monster_class_choice(), 'Health': 5,
               'Damage': roll_die(1, 4), 'Dexterity': roll_die(3, 6), 'Special': 0}
    class2 = monster['Class']
    monster['Dexterity'] = monster_dexterity(class2)
    monster['Special'] = monster_class_perk(class2)
    return monster


def attack_round(attacker, opponent):
    """
    Decide if an attack will be successful.

    Rolls an attack based on attacker's class and if > opponent's dexterity, will return the attack value
    PARAM: attacker, a dictionary
    PARAM: opponent, a dictionary
    PRE-CONDITION: attacker must be a complete character's dictionary
    PRE-CONDITION: opponent must be a complete character's dictionary
    POST-CONDITION: returns an attack value if attack is successful and 0 if it is not
    RETURN: an attack as an integer or 0
    """
    attack_roll = roll_die(1, 20)
    damage = roll_die(1, 4)
    if attack_roll > opponent['Dexterity']:
        opponent['Health'] = opponent['Health'] - damage
        print(str(attacker['Name']) + ' rolled a ' + str(attack_roll) + ' , ' + str(opponent['Name'])
              + ' has a dexterity of ' + str(opponent['Dexterity']))
        print('Attack was successfully struck')
        print(attacker['Name'] + ' attacked with a roll of ' + str(damage))
        return damage
    elif attack_roll <= opponent['Dexterity']:
        print(str(attacker['Name']) + ' rolled a ' + str(attack_roll) + ' , ' + str(opponent['Name'])
              + ' has a dexterity of ' + str(opponent['Dexterity']))
        print('Attack did not strike')
        return 0


def monster_run_away(my_character, monster):
    chance_damage = random.randint(1, 10)
    if chance_damage is not 5:
        print('You escaped successfully and without a scratch too')
    else:
        my_character['Health'] = my_character['Health'] - monster['Damage']
        print(str(monster['Name']), 'attacked as you were running away with a attack of', str(monster['Damage']),
              'your health is now', str(my_character['Health']))
        if my_character['Health'] < 0:
            print('You died')
        print('You survived to fight another day')


def monster_combat(my_character, monster):
    """
    Engage in combat to the death.
    :return:
    """
    choice = input(' Would you like to run away or fight? (type run or fight) ').lower().strip()
    if choice == 'run':
        monster_run_away(my_character, monster)
    elif choice == 'fight':
        while my_character['Health'] > 0:
            attack1 = attack_round(my_character, monster)
            my_character['Health'] = monster['Health'] - attack1
            if monster['Health'] <= 0:
                print(monster['Name'] + ' has died')
                break
            elif attack1 == 0 or monster['Health'] > 0:
                print(monster['Name'] + ' now has a health of ' + str(monster['Health']))
                attack3 = attack_round(monster, my_character)
                my_character['Health'] = my_character['Health'] - attack3
                print(my_character['Name'] + ' now has a health of ' + str(my_character['Health']))

        else:
            print(my_character['Name'] + ' has died')


monster_combat({'Name': 'Kyla', 'Health': 10, 'Dexterity':5, 'Damage':2},
                   {'Name': 'xxx', 'Health': 10, 'Dexterity':5, 'Damage':2})









