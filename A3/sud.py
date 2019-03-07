import random
import monster
import character


def create_coordinates():
    list1 = []
    list2 = []
    list3 = []
    for i in range(0, 5):
        for j in range(0, 5):
            list1.append(i)
            list2.append(j)
    for i in list1:
        list3.append([i])
    for i in range(0, len(list3)):
        list3[i].insert(1, list2[i])
    return list3


def game_map(character):
    coord = create_coordinates()
    for i in range(0, len(coord)):
        if i % 5 == 0:
            print('\n')
        if character['Location'] == coord[i]:
            print('$' + '  ', end='')
            continue
        print('*' + '  ', end='')
    print('\n')


def movement(character, command):
        if command == 'West':
            character['Location'][1] = (character['Location'][1] - 1)
        elif command == 'East':
            character['Location'][1] = (character['Location'][1] + 1)
        elif command == 'South':
            character['Location'][0] = (character['Location'][0] + 1)
        elif command == 'North':
            character['Location'][0] = (character['Location'][0] - 1)
        else:
            print('I do not understand that command, type help if you want to hear the rules')


def movement_conditions(character, command):
    if character['Location'][0] == 0 and command == 'North':
        print(" You've reached the end of this world please turn back or head east or west")
    elif character['Location'][1] == 0 and command == 'West':
        print(" You've reached the end of this world please turn back or head north or south")
    elif character['Location'][0] == 4 and command == 'South':
        print(" You've reached the end of this world please turn back or head east or west")
    elif character['Location'][1] == 4 and command == 'East':
        print(" You've reached the end of this world please turn back or head north or south")
    else:
        movement(character, command)


def location_one(character):
    if character['Location'] == [1, 3]:
        print('龴ↀ◡ↀ龴')
        test = input('what would you like to do?')
        if test == 'test':
            print('works')
    elif character['Location'] == [1, 2]:
        print('not working')


def monster_encounter_chance():
    chance = random.randint(1, 10)
    if chance == 4:
        print('You have encountered a monster yikes')
        return True
    else:
        print('You feel a calm wind blow in the air, At this moment you are truly alone in the wasteland')


def monster_encounter(monster):
        print(monster['Name'],' is hereee')


def game_loop():
    command = ''
    my_character = character.create_character()
    game_map(my_character)
    while command != 'Quit':
        command = input('Input a direction or quit: ').title()
        movement_conditions(my_character, command)
        game_map(my_character)
        print(my_character['Location'])
        if monster_encounter_chance():
            my_monster = monster.generate_monster()
            monster_encounter(my_monster)
            monster.monster_combat(my_character, my_monster)
        location_one(my_character)
    return None
print('龴ↀ◡ↀ龴')
print('ᕙ༼ ,,ԾܫԾ,, ༽ᕗ')



practice()









def main():
    print("""          
   _  _      _                         _                
  / ___|__ _| |_ _ __   ___   ___ __ _| |_ __  ___  ___ 
 | |   / _` | __| '_ \ / _ \ / __/ _` | | '_ \/ __|/ _ 
 | |__| (_| | |_| |_) | (_) | (_| (_| | | |_) \__ \  __/
  \____\__,_|\__| .__/ \___/ \___\__,_|_| .__/|___/\___|
                |_|                     |_|                           """)
    print("""
    
                        _
                       | |
                       | |
                       | |
  |\                   | |                                      
 /, ~\                / /
X     `-.....-------./ /
 ~-. ~  ~              |
    \             /    |
     \  /_     ___\   /
     | /\ ~~~~~   \ |
     | | \        || |
     | |\ \       || )
    (_/ (_/      ((_/""")                   # Ascii art from https://textart.io/art/


