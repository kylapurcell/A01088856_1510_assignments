import random
import character


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


def monster_dexterity(class_type):
    if class_type == 'Radioactive Rat' or class_type == 'Rogue Robot':
        return random.randint(1, 4)
    elif class_type == 'Mutated Creature' or 'Ghoul':
        return random.randint(1, 6)
    elif class_type == 'Pax':
        return random.randint(1, 20)


def monster_about():
    """
    Print information about the monsters of this world
    :return:
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
    :return:
    """
    monster = {'Name': monster_class_choice(), 'Health': 5,
               'Damage': random.randint(1, 4), 'Dexterity': 0}
    class2 = monster['Name']
    monster['Dexterity'] = monster_dexterity(class2)
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
    attack_roll = random.randint(1, 20)
    damage = random.randint(1, 6)
    print(str(attacker['Name']), 'has a chance to attack')
    if attack_roll > opponent['Dexterity']:
        opponent['Health'] = opponent['Health'] - damage
        print(attacker['Name'] + ' attacked with damage of ' + str(damage))
    elif attack_roll <= opponent['Dexterity']:
        print('Attack missed')


def monster_run_away(my_character, monster):
    chance_damage = random.randint(1, 10)
    if chance_damage == 5:
        my_character['Health'] = my_character['Health'] - monster['Damage']
        print(str(monster['Name']), 'attacked as you were running away with a attack of', str(monster['Damage']),
              'your health is now', str(my_character['Health']))
        if my_character['Health'] < 0:
            print('You died')
        print('You survived to fight another day')
    else:
        print('You escaped successfully and without a scratch too')


def monster_encounter(random_monster, user_character):
    print(random_monster['Name'], 'appeared!')
    if random_monster['Name'] == 'Pax':
        user_character['Cursed'] = True
        print('You have encountered the demon thief of destiny')
        print('ᕙ༼ Ծ^6^Ծ ༽ᕗ')


def monster_combat(my_character, monster):
    """
    Engage in combat to the death.
    :return:
    """
    while my_character['Health'] > 0:
            attack_round(my_character, monster)
            print(monster['Name'] + ' now has a health of ' + str(monster['Health']))
            if monster['Health'] <= 0:
                print(monster['Name'] + ' has died')
                break
            elif monster['Health'] > 0:
                attack_round(monster, my_character)
                print(my_character['Name'] + ' now has a health of ' + str(my_character['Health']))
            else:
                print(my_character['Name'] + ' has died')


def monster_fight(my_character, monster):
    monster_encounter(monster, my_character)
    choice = input(' Would you like to run away or fight? (type run or fight) ').lower().strip()
    if choice == 'run':
        monster_run_away(my_character, monster)
    elif choice == 'fight':
        monster_combat(my_character,monster)
    else:
        print('You must run or fight')
        return monster_combat(my_character, monster)











