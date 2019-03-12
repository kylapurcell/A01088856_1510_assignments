from unittest import TestCase
from unittest.mock import patch
import io
from A3 import sud


class TestLocationOne(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_one(self, mock_stdout):
        character = {'Name': 'Mew', 'Class': 'Hello Kitty', 'Health': 1,
                     'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}
        expected_output = """\nOh wait, Someone appeared. In front of you, you see a scraggly looking cat with \
red eyes and a robotic arm.
He's wearing a beanie with the phrase 'One Love' on it.

龴ↀ◡ↀ龴 
Hey man. I really need some CatNip. Can you bring me some? Try the store in the city ruins, south-east of here. \
Please man I gotta have it
Your inventory:  []\n"""
        sud.location_one(character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_one2(self, mock_stdout):
        character = {'Name': 'Mew', 'Class': 'Hello Kitty', 'Health': 1,
                     'Dexterity': 0, 'Location': [0, 2], 'Inventory': ['CatNip'], 'Cursed': False}
        expected_output = """\nOh wait, Someone appeared. In front of you, you see a scraggly looking cat \
with red eyes and a robotic arm.
He's wearing a beanie with the phrase 'One Love' on it.

龴ↀ◡ↀ龴 
\nHello again man!
龴ↀ 0 ↀ龴
OMG you found it thank you!! Here take this
Its a golden medal. You're surprised someone like him has something this nice
Your inventory:  ['I Beat Catpocalpse Medal']\n"""
        sud.location_one(character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_one3(self, mock_stdout):
        character = {'Name': 'Mew', 'Class': 'Hello Kitty', 'Health': 1,
                     'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': True}
        expected_output = """\nOh wait, Someone appeared. In front of you, you see a scraggly looking cat with \
red eyes and a robotic arm.
He's wearing a beanie with the phrase 'One Love' on it.

龴ↀ◡ↀ龴 
 
龴ↀ__ↀ龴 
... I'm too scared to accept catnip from you like this...head south west
Your inventory:  []\n"""
        sud.location_one(character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
