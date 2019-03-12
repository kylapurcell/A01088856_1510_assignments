# Kyla Purcell

# A01088856

# I hope you enjoy this short SUD. There is a small quest you can go on and also a hidden side quest
# you can also happen upon. I took a functional programming approach when creating this game and so modules contain no
# global variables and instead functions grouped together that relate to each purpose. Hope you like it!


import random
import monster
import character
import json
import os


def create_coordinates():
    """
    Create a list of coordinates for a game map.

    Uses nested for loops to create a nested list of coordinates from (0,0) to (6,6) to represent points on a game map
    POST-CONDITION: Returns a list containing 7 sub-lists that contain coordinates to a game map as pairs of integers.
    RETURN: a nested list.
    >>> create_coordinates()
    [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], \
[2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], \
[4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], \
[6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6]]
    """
    list1 = []
    list2 = []
    list3 = []
    for i in range(0, 7):
        for j in range(0, 7):     # Creates two lists from nested for loop
            list1.append(i)
            list2.append(j)
    for i in list1:
        list3.append([i])   # Appends items of list1 to the 0 index of sub-lists in list3
    for i in range(0, len(list3)):
        list3[i].insert(1, list2[i])  # Inserts items of list2 in the 1 index of the sub-lists in list3
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
            print('\n')                           # Adds a space to make board 7 by 7
        if user_character['Location'] == coord[i]:
            print('=^..^=', '  ', end='')           # User's current position is represented by this cat icon
            continue
        print('*****' + '    ', end='')     # Spaces on the game map are represented by *****
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
        user_character['Location'][1] = (user_character['Location'][1] - 1)   # Accounts for python row dominance
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
    print("\nOh wait, Someone appeared. In front of you, you see a scraggly looking cat "
          "with red eyes and a robotic arm.")
    print("He's wearing a beanie with the phrase 'One Love' on it.")
    print("\n龴ↀ◡ↀ龴 ")
    if user_character['Cursed']:     # If character is cursed unique dialogue option to lead user to easter egg
        print(" \n龴ↀ__ↀ龴 ")
        print("... I'm too scared to accept catnip from you like this...head south west")
    elif 'CatNip' in user_character['Inventory']:
        print('\nHello again man!')
        print('龴ↀ 0 ↀ龴')
        print('OMG you found it thank you!! Here take this')
        print("Its a golden medal. You're surprised someone like him has something this nice")
        inventory_modify('CatNip', 'I Beat Catpocalpse Medal', user_character)  # User 'wins' the game
    else:
        print('Hey man. I really need some CatNip. Can you bring me some?'  # Dialogue option if no CatNip
              ' Try the store in the city ruins, south-east of here. Please man I gotta have it')
    print('Your inventory: ', str(user_character['Inventory']))


def location_two():
    """
    Initiate dialogue for location three.

    PARAM: user_character, a dictionary
    PRE-CONDITION: user_character must be a complete character dictionary
    POST-CONDITION: Depending on what the user types, initiates different dialogue and prints it
    RETURN: None
    """
    print("\nYou have entered the large ruins of a library, in the middle of the room stands a studious "
          "looking cat wearing glasses with the word 'Google' written on them.")
    print("\n^⨀ᴥ⨀^")
    print("Hello welcome to the library, I can use my state of art technology to "
          " help you access information about this world")
    choice = input('If if you would like to view information about the monsters of this world type 1,'
                   ' and type anything else to be left alone: ').strip()
    if choice == '1':
        monster.monster_about()  # Calls a function that gives information about monsters to the user
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
    print('\nYou see the ruins of a grocery store. On top of a cash register is a fat cat smoking a cigarette!')
    if 'Cigarettes' in user_character['Inventory']:   # Dialogue option if user has cigarettes in inventory
        print('\n^(,,Ծ O Ծ,,)^')
        print('Wow ya got em thanks Bub! I put the CatNip in your inventory ;)')
        inventory_modify('Cigarettes', 'CatNip', user_character)
    elif 'Me0w M1x: Binary Edition!' in user_character['Inventory'] or 'CatNip' in user_character['Inventory']:
        print('\n^(,,Ծ__Ծ,,)^')                 # Makes it so NPC does not give CatNip to the player multiple times
        print('NO CIGARETTES, NO CATNIP. Sorry Bub.')
    else:
        print('\n^(,,ԾܫԾ,,)^')
        money = input('Hey Bub,I cant sell ya CatNip without money, ya got any money? (yes/no)')
        print('What?', money, '?', "Look I know you don't got any money "  # money does nothing but appears here (joke)
                                   "but can you go to the Human Museum and get me cigarettes? ")
        print("Head north west and take this.")
        user_character['Inventory'].append('Me0w M1x: Binary Edition!')  # Path if user does not have any quest items
        print("You can't figure out how a cat would start smoking cigarettes but you head on your way")
    print('Your inventory:', str(user_character['Inventory']))


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
    print('Did you know', facts[random_fact])  # Will tell the user a random 'fact' from the list each visit
    if 'Me0w M1x: Binary Edition!' in user_character['Inventory']:
        print('\nOh Cigarettes? The fat cat at the grocery store again! Every week with that guy...Fine just take them')
        inventory_modify('Me0w M1x: Binary Edition!', 'Cigarettes', user_character) # Path if Meow mix in inventory
        print('Your inventory:', str(user_character['Inventory']))
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
    if user_character['Cursed']:  # Player gets cursed if they encounter the monster Pax
        print("""Hey you've found me. I'm the developer of this game. You are here because you are one of the lucky
              individuals to find my easter egg. I added this in my game because I love Black Mirror's Bandersnatch.
              If you have not seen it yet, you should. Anyway I'll un-curse you so you can beat the game! 
              Thanks for playing!!!""")  # A note from me for the easter egg, just a fun thing I added,
        # Not a core component of the game
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

    Not sure how to unit or doctest this function
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
    >>> location_normal({'Name': 'Kyla', 'Class': 'Orange Julius', 'Health': 10, 'Dexterity': 6,\
                          'Location': [2, 4], 'Inventory': [], 'Cursed': False})
    You are crossing a bridge leading to the outskirts of the city ruins
    In the distance you spot a large building in good condition surrounded by stacks of burnt books
     """
    if user_character['Location'] != [1, 1] and user_character['Location'] != [2, 3] \
            and user_character['Location'][0] < 4 and user_character['Location'][1] < 4:
        print("You are in the valley, a barren location, that likely used to be a suburb before the war")
        print("In the distance you see a large building with sturdy looking pillars")
    elif user_character['Location'] != [5, 5]\
            and user_character['Location'][0] >= 4 and user_character['Location'][1] >= 4:
        print('You are in the city ruins, a charred location filled with decaying buildings')
        print('In the distance you see the run down remains of a grocery store')
    elif user_character['Location'] != [5, 1] and user_character['Location'][0] >= 4 >= user_character['Location'][1]:
        print('You are in the lake region, green radioactive particles shimmer in the brown coloured waters')
        print('You feel something in the humid air as if this region is the location of an Easter Egg')
        print('Easter Egg? You have no idea what that is or why you thought of it')
    elif user_character['Location'] != [1, 5] and user_character['Location'][0] < 4 <= user_character['Location'][1]:
        print('You are crossing a bridge leading to the outskirts of the city ruins')
        print('In the distance you spot a large building in good condition surrounded by stacks of burnt books')


def monster_encounter_chance():
    """
    Determine if character encounters a monster or heals.

    PARAM: user_character, a dictionary
    PRE-CONDITION: user_character must be a full character dictionary
    POST-CONDITION: Prints output if monster encounter occurs and different output if it does mot
    RETURN: True or False as a boolean
    >>> random.seed(3)
    >>> monster_encounter_chance()
    You have encountered a monster yikes
    True
    >>> random.seed()
    """
    chance = random.randint(1, 10)   # Player has a 10% chance of encountering a monster or 1 in 10
    if chance == 4:
        print('You have encountered a monster yikes')
        return True
    else:
        print('You feel a calm wind blow in the air, At this moment you are truly alone in the wasteland')
        # Lets user know they have not encountered a monster


def save_game(user_character):
    """
    Save a character in a json file.

    PARAM: user_character, a dictionary
    PRE-CONDITION: user_character must be a complete character dictionary
    POST-CONDITION: Saves the character dictionary by writing it into a json file
    RETURN: None

    Not sure how to doctest or unittest this function
    """
    filename = str(user_character['Name']) + 'savefile.json'  # Save files are named from the character's name
    if os.path.isfile(filename):  # If save file already exists gives option to overwrite it or not
        over_write = input('There is already a save file with your name, 1 to overwrite and 2 to create a new file: ')
        if over_write == '1':
            print('Okay your character file will be overwritten')
        elif over_write == '2':  # Creates new file if user does not want to overwrite
            new_filename = input('What would you like your new character file to be called? ') + 'savefile.json'
            with open(new_filename, 'w') as file_object: json.dump(user_character, file_object)
        else:
            return save_game(user_character)  # Recursion : User must overwrite or make a new save
    with open(filename, 'w') as file_object: json.dump(user_character, file_object)  # Saves file
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
            name = input("Input your character's name ").title().strip()  # Loads file based on character's name
            filename = name + 'savefile.json'
            with open(filename) as file_object: my_character = json.load(file_object)
            return my_character
        except FileNotFoundError:  # If file is not found game does not crash
            print('We could not find that character in our system')
    elif choice == 'new':
        print('Okay we will create a new game for you')
        return character.create_character()  # Uses create_character function to create a new game
    return load_game()  # Recursion if user either does not pick load or new or their file is not found


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
        user_character['Location'] = [2, 2]  # Restores characters stats when they die
        survival = input(' Would you like to continue the game? (yes/no) ').lower().strip()
        if survival == 'yes':
            print('You awaken at the center of this world, where you started your journey')
            return False
        elif survival == 'no':
            return True
        else:
            print('Please choose yes or no')
            return is_character_dead(user_character)  # Recursion: user must pick yes or no


def game_loop():
    """
    Run the game.

    Cannot unit test or doctest. However game was play tested by several people and bugs were patched accordingly.
    """
    my_character = load_game()
    game_map(my_character)   # Shows the user the initial game map and their position
    while True:
        command = input('Input North,East,South, or West to move. Input quit to exit the game: ').title().strip()
        if command == 'Quit':
            break              # On quitting saves the users game and quits the program
        if movement_conditions(my_character, command):  # If character move is valid moves the character on the map
            movement(my_character, command)   # Updates character coordinates
            game_map(my_character)  # Updates the game map
            if monster_encounter_chance():   # 10% chance of running into a monster
                my_monster = monster.generate_monster()
                monster.monster_fight(my_character, my_monster)  # User can run or fight from a monster
            else:
                character.character_healing(my_character)  # If user health < 10 and no monster encounter they heal
            if is_character_dead(my_character):
                break                        # If character is dead they get a choice to continue or exit/save the game
            location_special(my_character)  # Checks if user at special quest location
            location_normal(my_character)  # Checks what printed output to give user based on region on the map
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
    (_/ (_/      ((_/""")  # Ascii art from https://textart.io/art/
    print("""Before the war, technology ruled the lives of humans so much so that they even decided to incorporate this
    technology into their beloved pets, creating android like creatures. Little did they know this technology would give 
    their feline friends special resistant to radioactive war fare, and when the ashes settled they remained 
    the sole survivors. Welcome! We wish you luck on your post-apocalyptic journey. We suggest you head East from your
    start position but its up to you.""")
    game_loop()
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    main()
