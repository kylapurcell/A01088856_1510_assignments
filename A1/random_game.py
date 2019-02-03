import random


def computer_choice():
    """
    Generate a random choice of Rock, Paper, or Scissors

    Generates a random number from 0 to 2 to represent rock, paper, or scissors
    RETURN: a choice of Rock, Paper, or Scissors as a string in title case
    """
    choice = random.randint(0, 2)
    if choice == 0:                   # Returns Rock, Paper, or, Scissors based on random choice of integer [0, 2]
        return "Rock"
    elif choice == 1:
        return "Paper"
    elif choice == 2:
        return "Scissors"


def who_wins(choice1, choice2):
    """
    Decide which choice will win

    PARAM: choice1, a string
    PARAM: choice2, a string
    PRE-CONDITION: choice1 must be a string in title case with no leading or trailing whitespace
    PRE-CONDITION: choice2 must be a string in title case with no leading or trailing whitespace
    POST-CONDITION: returns the winner based on choice1 and choice2
    RETURN: Computer Wins, Draw, Or You Win as a string

    >>> who_wins("Paper","Rock")
    'Computer Wins'
    >>> who_wins("Paper","Paper")
    'Draw'
    >>> who_wins("Paper", "Scissors")
    'You Win'
    """
    if choice1 == "Paper" and choice2 == "Rock":
        return "Computer Wins"
    elif choice1 == "Paper" and choice2 == "Scissors":
        return "You Win"
    elif choice1 == "Paper" and choice2 == "Paper":
        return "Draw"
    elif choice1 == "Rock" and choice2 == "Rock":
        return "Draw"
    elif choice1 == "Rock" and choice2 == "Scissors":
        return "Computer Wins"
    elif choice1 == "Rock" and choice2 == "Paper":
        return "You Win"
    elif choice1 == "Scissors" and choice2 == "Rock":
        return "You Win"
    elif choice1 == "Scissors" and choice2 == "Scissors":
        return "Draw"
    elif choice1 == "Scissors" and choice2 == "Paper":
        return "Computer Wins"


# Kyla Purcell

# A01088856

# February 3rd 2019

# A program that plays a round of Rock, Paper, Scissors with the user


def rock_paper_scissors():
    """
    Play a game of Rock, Paper, Scissors with the user

    Receive the users choice, generates the computer choice then returns the winner
    PRE-CONDITION: user_choice must be a string
    POST-CONDITION: If user choice = Rock, Paper, Or Scissors decides the winner, else returns helpful message
    RETURN: the user choice, the computer choice and the winner as a concatenated string or
    a helpful message to correct user input as a string
    """
    user_choice = input("Input your guess: ").strip().title()  # strips user input and converts to title case
    cpu_choice = computer_choice()  # helper function to get computer's choice
    if user_choice == "Rock" or user_choice == "Paper" or user_choice == "Scissors":
        return "cpu choose " + cpu_choice + ", you choose " + user_choice + ", so " + who_wins(cpu_choice, user_choice)
    else:
        return "Please choose between rock, paper or scissors to play the game"


def main():
    """
    Drive the program
    """
    import doctest
    doctest.testmod()
    print(rock_paper_scissors())


if __name__ == '__main__':
    main()





