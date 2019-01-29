import random


def computer_choice():
    choice = random.randrange(0,3)
    if choice == 0:
        return "Rock"
    elif choice == 1:
        return "Paper"
    elif choice == 2:
        return "Scissors"


def who_wins(choice1,choice2):
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


def rock_paper_scissors():
    user_choice = input("Input your guess: ").strip().title()
    cpu_choice = computer_choice()
    if user_choice == "Rock" or user_choice == "Paper" or user_choice == "Scissors":
        return "cpu choose " + cpu_choice + ", you choose " + user_choice + ", so " + who_wins(cpu_choice,user_choice)
    else:
        return "Please choose between rock, paper or scissors to play the game"


print(rock_paper_scissors())




