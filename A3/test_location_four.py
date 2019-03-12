from unittest import TestCase
from unittest.mock import patch
import io
from A3 import sud


class TestLocationFour(TestCase):

    @patch('random.randint', return_value=0)       # Tests printed that first 'fact' is printed when random int = 0
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_four(self, mock_stout, mock_random):
        character_one = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 0,
                         'Dexterity': 0, 'Location': [5, 5], 'Inventory': [], 'Cursed': False}
        expected_output = """You see building with a sign that reads 'Museum', a small robotic cat sits inside 
 
龴ↀ=ↀ龴
Welcome to the Human Museum, your source for the most accurate info about our extinct friends
Did you know Humans used to place items on tables and never get the urge to push them on the floor\n"""
        sud.location_four(character_one)
        self.assertEqual(mock_stout.getvalue(), expected_output)

    @patch('random.randint', return_value=1)        # Tests printed that second 'fact' is printed when random int = 1
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_four2(self, mock_stout, mock_random):
        character_one = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 0,
                         'Dexterity': 0, 'Location': [5, 5], 'Inventory': [], 'Cursed': False}
        expected_output = """You see building with a sign that reads 'Museum', a small robotic cat sits inside 
 
龴ↀ=ↀ龴
Welcome to the Human Museum, your source for the most accurate info about our extinct friends
Did you know Humans had the most comfortable chairs *Holds up a laptop*\n"""
        sud.location_four(character_one)
        self.assertEqual(mock_stout.getvalue(), expected_output)

    @patch('random.randint', return_value=2)       # Tests printed that first 'fact' is printed when random int = 2
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_four3(self, mock_stout, mock_random):
        character_one = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 0,
                         'Dexterity': 0, 'Location': [5, 5], 'Inventory': [], 'Cursed': False}
        expected_output = """You see building with a sign that reads 'Museum', a small robotic cat sits inside 
 
龴ↀ=ↀ龴
Welcome to the Human Museum, your source for the most accurate info about our extinct friends
Did you know Humans always closed the door when in the bathroom...but why?!\n"""
        sud.location_four(character_one)
        self.assertEqual(mock_stout.getvalue(), expected_output)

    @patch('random.randint', return_value=2)      # Tests printed output when user has Meow Mix in inventory
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_four3(self, mock_stout, mock_random):
        character_one = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 0, 'Dexterity': 0,
                         'Location': [5, 5], 'Inventory': ['Me0w M1x: Binary Edition!'], 'Cursed': False}
        expected_output = """You see building with a sign that reads 'Museum', a small robotic cat sits inside 
 
龴ↀ=ↀ龴
Welcome to the Human Museum, your source for the most accurate info about our extinct friends
Did you know Humans always closed the door when in the bathroom...but why?!
\nOh Cigarettes? The fat cat at the grocery store again! Every week with that guy...Fine just take them
Your inventory: ['Cigarettes']
He seems mad. Better be on your way\n"""
        sud.location_four(character_one)
        self.assertEqual(mock_stout.getvalue(), expected_output)
