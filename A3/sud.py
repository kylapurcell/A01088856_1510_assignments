import random
import monster
import character
import json
import os


def create_coordinates():
    """
    Create a list of coordinates for a game map.

    POST-CONDITION: Returns a list containing 7 sub-lists that contain coordinates to a game map as pairs of integers.
    RETURN: a nested list.
    """
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


def game_map(user_character):
    """
    Print a game map.

    Prints out a game map with a character icon located on the map based on the character's current location
    PARAM: user_character, a dictionary
    PRE-CONDITION: user_character must be a complete character dictionary
    POST-CONDITION: prints out a a game map with a character icon located at character's current coordinate
    RETURN: None
    """
    coord = create_coordinates()
    for i in range(0, len(coord)):
        if i % 7 == 0:
            print('\n')
        if user_character['Location'] == coord[i]:
            print('=^..^=', '  ', end='')
            continue
        print('*****' + '    ', end='')
    print('\n')


def movement(user_character, command):
    """
    Move the character across a game map.

    PARAM: user_character, a dictionary
    PARAM: command, a string
    PRE-CONDITION: user_character must be a complete character dictionary
    PRE-CONDITION: command must be a string
    POST-CONDITION: Changes the characters current location based on the command they inputted
    RETURN: None

    Not sure how to doctest or unit test this function
    """
    if command == 'West':
        user_character['Location'][1] = (user_character['Location'][1] - 1)
    elif command == 'East':
        user_character['Location'][1] = (user_character['Location'][1] + 1)
    elif command == 'South':
        user_character['Location'][0] = (user_character['Location'][0] + 1)
    elif command == 'North':
        user_character['Location'][0] = (user_character['Location'][0] - 1)


def movement_conditions(user_character, command):
    """
    Decide if movement command is valid.

    PARAM: user_character, a dictionary
    PARAM: command, a string
    PRE-CONDITION: user_character must be a complete character dictionary
    POST-CONDITION: Determine if move is valid by returning True or False and print a helpful message if it is not
    RETURN: True or False as a boolean
    >>> movement_conditions({'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 10, 'Damage': 7, \
    'Dexterity': 5, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}, 'North')
     You've reached the end of this world please turn back or head east or west
    >>> movement_conditions({'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 10, 'Damage': 7, \
    'Dexterity': 5, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}, 'West')
    True
    """
    if command != 'North' and command != 'South' and command != 'West' and command != 'East':
        print('I do not understand that command. Please type North ,West, South, East, or Quit')
    elif user_character['Location'][0] == 0 and command == 'North':
        print(" You've reached the end of this world please turn back or head east or west")
    elif user_character['Location'][1] == 0 and command == 'West':
        print(" You've reached the end of this world please turn back or head north or south")
    elif user_character['Location'][0] == 6 and command == 'South':
        print(" You've reached the end of this world please turn back or head east or west")
    elif user_character['Location'][1] == 6 and command == 'East':
        print(" You've reached the end of this world please turn back or head north or south")
    else:
        return True


def inventory_modify(item1, item2, user_character):
    """
    Change the items in a character dictionary.

    PARAM: user_character, a dictionary
    PARAM: Item1, a string
    PARAM: Item2, a string
    PRE-CONDITION: user_character must be a complete character dictionary
    POST-CONDITION: Removes an item from the character's dictionary and replaces it with another
    RETURN: None

    Not sure how to doctest or unittest this function
    """
    user_character['Inventory'].remove(item1)
    user_character['Inventory'].append(item2)


def location_one(user_character):
    """
    Initiate quest dialogue for location one.

    PARAM: user_character, a dictionary
    PRE-CONDITION: user_character must be a complete character dictionary
    POST-CONDITION: Depending on what the character has in their inventory prints different dialogue and appends/removes
     items from their inventory list.
    RETURN: None
    """
    print("\n Oh wait, Someone appeared. In front of you, you see a scraggly looking cat "
          "with red eyes and a robotic arm.\n He's wearing a beanie with the phrase 'One Love' on it.\n \n 龴ↀ◡ↀ龴 ")
    if user_character['Cursed']:
        print(" \n 龴ↀ__ↀ龴 \n... I'm too scared to accept catnip from you like this...head south west")
    elif 'CatNip' in user_character['Inventory']:
        print('Hello again man! \n 龴ↀ 0 ↀ龴 \n OMG you found it thank you!! Here take this')
        print("Its a golden medal. You're surprised someone like him has something this nice")
        inventory_modify('CatNip', 'I Beat Catpocalpse Medal', user_character)
    else:
        print('Hey man. I really need some CatNip. Can you bring me some?'
              ' Try the store in the city ruins, south-east of here. Please man I gotta have it')
    print('your inventory: ', str(user_character['Inventory']))


def location_two():
    """
    Initiate dialogue for location three.

    PARAM: user_character, a dictionary
    PRE-CONDITION: user_character must be a complete character dictionary
    POST-CONDITION: Depending on what the user types, initiates different dialogue and prints it
    RETURN: None
    """
    print("You have entered the large ruins of a library, in the middle of the room stands a studious "
          "looking cat wearing glasses with the word 'Google' written on them.")
    print("\n^⨀ᴥ⨀^\n,Hello welcome to the library, I can use my state of art technology to "
          " help you access information about this world")
    choice = input('If if you would like to view information about the monsters of this world type 1,'
                   ' and type anything else to be left alone: ').strip()
    if choice == '1':
        monster.monster_about()
    print('Thanks for coming. If you require my service again please visit this location again')


def location_three(user_character):
    """
    Initiate quest dialogue for location three.

    PARAM: user_character, a dictionary
    PRE-CONDITION: user_character must be a complete character dictionary
    POST-CONDITION: Depending on what the character has in their inventory prints different dialogue and appends/removes
     items from their inventory list.
    RETURN: None
    """
    print('You see the ruins of a grocery store. On top of a cash register is a fat cat smoking a cigarette!')
    if 'Cigarettes' in user_character['Inventory']:
        print('\n ᕙ༼ ,,Ծ O Ծ,, ༽ᕗ \n Wow ya got em thanks Bub! I put the Cat Nip in your inventory ;)')
        inventory_modify('Cigarettes', 'CatNip', user_character)
    elif 'Me0w M1x: Binary Edition!' in user_character['Inventory'] or 'CatNip' in user_character['Inventory']:
        print('\nᕙ༼ ,,Ծ__Ծ,, ༽ᕗ\n No Cigarettes no Cat Nip , sorry Bub.')
    else:
        money = input('\n ᕙ༼ ,,ԾܫԾ,, ༽ᕗ \n Hey Bub,I cant sell ya Cat Nip without money, ya got any money? (yes/no)')
        print('What?', money, '?', "Look I know you don't got any money "
                                   "but to the Human Museum and get me cigarettes? \n Head north west and take this.")
        user_character['Inventory'].append('Me0w M1x: Binary Edition!')
        print("You can't figure out how a cat would start smoking cigarettes but you head on your way")
    print('your inventory:', str(user_character['Inventory']))


def location_four(user_character):
    """
    Initiate quest dialogue for location three.

    PARAM: user_character, a dictionary
    PRE-CONDITION: user_character must be a complete character dictionary
    POST-CONDITION: Depending on what the character has in their inventory prints different dialogue and appends/removes
     items from their inventory list.
    RETURN: None
    """
    print("You see building with a sign that reads 'Museum', a small robotic cat sits inside \n \n龴ↀ=ↀ龴")
    print('Welcome to the Human Museum, your source for the most accurate info about our extinct friends')
    random_fact = random.randint(0, 2)
    facts = ['Humans used to place items on tables and never get the urge to push them on the floor',
             'Humans had the most comfortable chairs *Holds up a laptop*',
             'Humans always closed the door when in the bathroom...but why?!']
    print('Did you know', facts[random_fact])
    if 'Me0w M1x: Binary Edition!' in user_character['Inventory']:
        print('\nOh Cigarettes? The fat cat at the grocery store again! Every week with that guy...Fine just take them')
        inventory_modify('Me0w M1x: Binary Edition!', 'Cigarettes', user_character)
        print('your inventory:', str(user_character['Inventory']))
        print('He seems mad. Better be on your way')


def location_secret(user_character):
    """
    Initiate special dialogue for an easter egg/secret location.

    PARAM: user_character, a dictionary
    PRE-CONDITION: user_character must be a complete character dictionary
    POST-CONDITION: Depending on if the character is cursed or not prints different dialogue options
    and changes the character's status.
    RETURN: None
    """
    if user_character['Cursed']:
        print("""Hey you've found me. I'm the developer of this game. You are here because you are one of the lucky
              individuals to find my easter egg. I added this in my game because I love Black Mirror's Bandersnatch.
              If you have not seen it yet, you should. Anyway I'll un-curse you so you can beat the game! 
              Thanks for playing!!!""")
        user_character['Cursed'] = False
    else:
        print('You notice something strange about this area but cannot quite put your finger on it')


def location_special(user_character):
    """
    Determine if character is at a quest location.

    PARAM: user_character, a dictionary
    PRE-CONDITION: user_character must be a complete character dictionary
    POST-CONDITION: Calls a function that corresponds to characters current location.
    RETURN: None
    """
    if user_character['Location'] == [2, 3]:
        location_one(user_character)
    elif user_character['Location'] == [1, 5]:
        location_two()
    elif user_character['Location'] == [5, 5]:
        location_three(user_character)
    elif user_character['Location'] == [1, 1]:
        location_four(user_character)
    elif user_character['Location'] == [5, 1]:
        location_secret(user_character)


def location_normal(user_character):
    """
    Print descriptions dependant on characters location on the map.

    PARAM: user_character, a dictionary
    PRE-CONDITION: user_character must be a complete character dictionary
    POST-CONDITION: Prints output dependant on what region that character's location corresponds to on the map.
    RETURN: None
     """
    if user_character['Location'] != [1, 1] and user_character['Location'] != [2, 3] \
            and user_character['Location'][0] < 3 and user_character['Location'][1] < 3:
        print("You are in the valley, a barren location that likely used to be a suburb before the war")
    elif user_character['Location'] != [5, 5]\
            and user_character['Location'][0] >= 4 and user_character['Location'][1] >= 4:
        print('You are in the city ruins, a charred location filled with decaying buildings')
    elif user_character['Location'] != [5, 1] and user_character['Location'][0] > 3 > user_character['Location'][1]:
        print('You are in the lake region, green radioactive particles shimmer in the waters located in the distance ')
    elif user_character['Location'] != [1, 5] and user_character['Location'][0] < 3 < user_character['Location'][1]:
        print('You are crossing a bridge leading to the outskirts of the city ruins')


def monster_encounter_chance(user_character):
    """
    Determine if character encounters a monster or heals.

    PARAM: user_character, a dictionary
    PRE-CONDITION: user_character must be a full character dictionary
    POST-CONDITION: Prints output if monster encounter occurs and calls a helper function if it doesn't
    RETURN: True or False as a boolean
    >>> random.seed(3)
    >>> monster_encounter_chance({'Name':'Kyla', 'Class': 'Big Chonk', 'Health': 10, 'Damage': 0,\
                 'Dexterity': 0, 'Location': [2, 2], 'Inventory': [], 'Cursed': False})
    You have encountered a monster yikes
    True
    >>> random.seed()
    """
    chance = random.randint(1, 10)
    if chance == 4:
        print('You have encountered a monster yikes')
        return True
    else:
        print('You feel a calm wind blow in the air, At this moment you are truly alone in the wasteland')
        character.character_healing(user_character)


def save_game(user_character):
    """
    Save a character in a json file.

    PARAM: user_character, a dictionary
    PRE-CONDITION: user_character must be a complete character dictionary
    POST-CONDITION: Saves the character dictionary by writing it into a json file
    RETURN: None

    Not sure how to doctest or unittest this function
    """
    filename = str(user_character['Name']) + 'savefile.json'
    if os.path.isfile(filename):
        over_write = input('There is already a save file with your name, 1 to overwrite and 2 to create a new file: ')
        if over_write == '1':
            print('Okay your character file will be overwritten')
        elif over_write == '2':
            new_filename = input('What would you like your new character file to be called? ') + 'savefile.json'
            with open(new_filename, 'w') as file_object: json.dump(user_character, file_object)
        else:
            return save_game(user_character)
    with open(filename, 'w') as file_object: json.dump(user_character, file_object)
    print('Your game has been saved, Thank you for playing =^..^=')


def load_game():
    """
    Load a character save file from a json file.

    POST-CONDITION: Loads a character dictionary from a json file or calls a function to create a new character
    RETURN: A character as a dictionary

    Not sure how to doctest or unittest this function
    """
    choice = input('Do you want to start a new game or load? (new,load) ').lower().strip()
    if choice == 'load':
        try:
            name = input("Input your character's name ").title().strip()
            filename = name + 'savefile.json'
            with open(filename) as file_object: my_character = json.load(file_object)
            return my_character
        except FileNotFoundError:
            print('We could not find that character in our system')
    elif choice == 'new':
        print('Okay we will create a new game for you')
        return character.create_character()
    return load_game()


def is_character_dead(user_character):
    """
    Manage a dead character.

    PARAM: user_character, a dictionary
    PRE-CONDITION: user_character must be a complete character dictionary
    POST-CONDITION: Regenerates the character's health and location, prints output and calls a helper function if user
    decides to quit.
    RETURN: True or False as a boolean
    """
    if user_character['Health'] <= 0:
        user_character['Health'] = 10
        user_character['Location'] = [2, 2]
        survival = input(' Would you like to continue the game? (yes/no) ').lower().strip()
        if survival == 'yes':
            print('You awaken at the center of this world, where you started your journey')
            return False
        elif survival == 'no':
            return True
        else:
            print('Please choose yes or no')
            return is_character_dead(user_character)


def game_loop():
    """
    Run the game.

    Cannot unit test or doctest. However game was play tested by several people and bugs were patched accordingly.
    """
    my_character = load_game()
    game_map(my_character)
    while True:
        command = input('Input North,East,South, or West to move. Input quit to exit the game: ').title().strip()
        if command == 'Quit':
            break
        if movement_conditions(my_character, command):
            movement(my_character, command)
            game_map(my_character)
            if monster_encounter_chance(my_character):
                my_monster = monster.generate_monster()
                monster.monster_fight(my_character, my_monster)
            if is_character_dead(my_character):
                break
            location_special(my_character)
            location_normal(my_character)
    return save_game(my_character)


def main():
    """
    Drive the program
    """
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
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    main()
