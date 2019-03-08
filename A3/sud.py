import random
import monster
import character
import json
import os


def create_coordinates():
    list1 = []
    list2 = []
    list3 = []
    for i in range(0, 7):
        for j in range(0, 7):
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
        if i % 7 == 0:
            print('\n')
        if character['Location'] == coord[i]:
            print('=^..^=','  ', end='')
            continue
        print('*****' + '    ', end='')
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
    elif character['Location'][0] == 6 and command == 'South':
        print(" You've reached the end of this world please turn back or head east or west")
    elif character['Location'][1] == 6 and command == 'East':
        print(" You've reached the end of this world please turn back or head north or south")
    else:
        movement(character, command)


def location_special(character):
    if character['Location'] == [1, 3]:
        print('龴ↀ◡ↀ龴')
        test = input('what would you like to do?')
        if test == 'test':
            print('works')
    elif character['Location'] == [1, 2]:
        print('not working')


def location_normal(character):
    pass


def monster_encounter_chance():
    chance = random.randint(1, 10)
    if chance == 4:
        print('You have encountered a monster yikes')
        return True
    else:
        print('You feel a calm wind blow in the air, At this moment you are truly alone in the wasteland')


def monster_encounter(monster):
        print(monster['Name'],' appeared')


def save_game(character):
    filename = str(character['Name']) + 'savefile.json'
    if os.path.isfile(filename):
        over_write = input('There is already a save file with your character name '
                           'press 1 to overwrite and 2 to create a new file? ')
        if over_write == '1':
            print('Okay your character file will be overwritten')
        elif over_write == '2':
            new_filename = input('What would you like your new character file to be called? ') + 'savefile.json'
            with open(new_filename, 'w') as file_object: json.dump(character, file_object)
    with open(filename, 'w') as file_object: json.dump(character, file_object)
    print('Your game has been saved, Thank you for playing =^..^=')


def load_game():
    choice = input('Do you want to start a new game or load? (new,load) ')
    if choice == 'load':
        try:
            name = input("input your character's name ").title().strip()
            filename = name + 'savefile.json'
            with open(filename) as file_object: my_character = json.load(file_object)
            return my_character
        except FileNotFoundError:
            print('We could not find that character in our system please create a new one')
            return character.create_character()
    return character.create_character()


def game_loop():
    my_character = load_game()
    game_map(my_character)
    while True:
        command = input('Input a direction or quit: ').title().strip()
        if command == 'Quit':
            break
        movement_conditions(my_character, command)
        game_map(my_character)
        if monster_encounter_chance():
            my_monster = monster.generate_monster()
            monster_encounter(my_monster)
            monster.monster_combat(my_character, my_monster)
        location_special(my_character)
        location_normal(my_character)
    return save_game(my_character)

print('龴ↀ◡ↀ龴')
print('ᕙ༼ ,,ԾܫԾ,, ༽ᕗ')



game_loop()









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


