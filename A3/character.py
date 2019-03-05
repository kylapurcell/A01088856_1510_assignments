import random


def create_character():
    character = {'Name': input('What is your name? '), 'Health': 10, 'Damage': 0,
                 'Dexterity': 0, 'Location': [0, 0], 'Inventory': []}
    return character

