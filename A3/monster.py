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


def generate_monster():
    """
    Generate a monster.
    :return:
    """
    monster = {'Class': monster_class_choice(), 'Health': 5,
               'Damage': roll_die(1, 4), 'Dexterity': roll_die(3, 6), 'Special': 0}
    class2 = monster['Class']
    monster['Dexterity'] = monster_dexterity(class2)
    monster['Special'] = monster_class_perk(class2)
    return monster


