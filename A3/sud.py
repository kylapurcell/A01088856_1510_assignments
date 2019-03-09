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


def location_one(character):
    print('\n')
    print("Oh wait, Someone appeared. In front of you, you see a scraggly looking cat with red eyes and a robotic arm."
          " He's wearing a beanie with the phrase 'One Love' on it. ")
    print('龴ↀ◡ↀ龴')
    if character['Cursed']:
        print('龴ↀ__ↀ龴')
        print("There's something different about you... I'm too scared to accept catnip from you...head south west")
    elif 'CatNip' in character['Inventory']:
        print('Hello again man!')
        print('龴ↀ 0 ↀ龴')
        print('OMG you found it thank you!! Here take this')
        print("Its a golden medal. You're surprised someone like him has something this nice")
        character['Inventory'].remove('CatNip')
        character['Inventory'].append('I Beat Catpocalpse Medal')
        print('your inventory:', str(character['Inventory']))
    else:
        print('Hey man. I really need some CatNip. Can you bring me some?'
              ' Try the store in the city ruins, south-east of here. Please man I gotta have it')
        print('your inventory: ', str(character['Inventory']))


def location_two(character):
    print("You have entered the large ruins of a library, in the middle of the room stands a studious "
          "looking cat wearing glasses with the word 'Google' written on them.")
    print("^⨀ᴥ⨀^,Hello welcome to the library, I can use my state of art technology to "
          " help you access information about this world")
    choice = input('If if you would like to view information about the monsters of this world type 1,'
                   ' and type anything else to be left alone: ').strip()
    if character['Cursed']:
        print('^⨀__⨀^')
        print("Oh, it appears you've been visited by Pax I think you should head south from here ")
    elif choice == '1':
        monster.monster_about()
    print('Thanks for coming. If you require my service again please visit this location again')


def location_three(character):
    print('You see the ruins of a grocery store. Sitting on top of a cash register is a fat cat smoking a cigarette!')
    print('ᕙ༼ ,,ԾܫԾ,, ༽ᕗ')
    if character['Cursed']:
        print('ᕙ༼ ,,Ծ___Ծ,, ༽ᕗ uhm...we are closed. Begone!')
    elif 'Cigarettes' in character['Inventory']:
        print('Wow ya got em thanks Bub! I put the Cat Nip in your inventory ;)')
        character['Inventory'].remove('Cigarettes')
        character['Inventory'].append('CatNip')
    else:
        money = input('Hey Bub,I cant sell ya Cat Nip without money, ya got any money? (yes/no)')
        print('What?', money, '?', "Look I know you don't got any money "
                                   "but can you go to the Human Museum and get me cigarettes?")
        print('Head North West and take this and tell them I sent ya')
        character['Inventory'].append('Me0w M1x: Binary Edition!')
    print('your inventory:', str(character['Inventory']))
    print("You can't figure out how a cat would start smoking cigarettes but you head on your way")

def location_four(character):
    print("You see building with a sign that reads 'Museum', a small robotic cat sits inside")
    print('龴ↀ=ↀ龴')
    print('Welcome to the Human Museum, your source for the most accurate info about our extinct friends')
    random_fact = random.randint(0, 2)
    facts = ['Humans used to place items on tables and never get the urge to push them on the floor',
             'Humans had the most comfortable chairs *Holds up a laptop*',
             'Humans always closed the door when in the bathroom...but why?!']
    print('Did you know', facts[random_fact])
    if character['Cursed']:
        print('龴ↀ-0-ↀ龴...Please leave')
    elif 'Me0w M1x: Binary Edition!' in character['Inventory']:
        print('Oh Cigarettes? The fat cat at the grocery store again! Every week with that guy...')
        print('Fine just take them and go')
        character['Inventory'].remove('Me0w M1x: Binary Edition!')
        character['Inventory'].append('Cigarettes')
        print('your inventory:', str(character['Inventory']))
        print('He seems mad. Better be on your way')

def location_five(character):
    pass


def location_special(character):
    if character['Location'] == [2, 3]:
        location_one(character)
    elif character['Location'] == [1, 5]:
        location_two(character)
    elif character['Location'] == [5,5]:
        location_three(character)
    elif character['Location'] == [1,1]:
        location_four(character)



def location_normal(character):
    if character['Location'] != [1, 1] and character['Location'][0] < 4 and character['Location'][1] < 4:
        print("You are in the valley, a barren location that likely used to be a suburb before the war")
        print("In the distance you see the charred ruins of a large building with tall pillars")



def monster_encounter_chance():
    chance = random.randint(1, 10)
    if chance == 4:
        print('You have encountered a monster yikes')
        return True
    else:
        print('You feel a calm wind blow in the air, At this moment you are truly alone in the wasteland')


def monster_encounter(monster):
        print(monster['Name'],'appeared')


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


def is_character_dead(character):
    if character['Health'] <= 0:
        character['Health'] = 10
        character['Location'] = [2, 2]
        survival = input(' Would you like to continue the game? (yes/no) ').lower().strip()
        if survival == 'yes':
            print('You awaken at the center of this world, where you started your journey')
            return False
        elif survival == 'no':
            return True
        else:
            print('Please choose yes or no')
            return is_character_dead(character)


def game_loop():
    my_character = load_game()
    game_map(my_character)
    while True:
        command = input('Input a direction or quit: ').title().strip()
        if command == 'Quit':
            break
        movement_conditions(my_character, command)
        game_map(my_character)
        character.character_healing(my_character)
        if monster_encounter_chance():
            my_monster = monster.generate_monster()
            monster_encounter(my_monster)
            monster.monster_combat(my_character, my_monster)
        if is_character_dead(my_character):
            break
        location_special(my_character)
        location_normal(my_character)
    return save_game(my_character)

print('龴ↀ◡ↀ龴')
print('ᕙ༼ ,,ԾܫԾ,, ༽ᕗ')













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
    game_loop()



main()