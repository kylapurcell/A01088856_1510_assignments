from unittest import TestCase
from unittest.mock import patch
import io
from A3 import sud


class TestLocationThree(TestCase):
    @patch('builtins.input', return_value='yes')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_three(self, mock_stout, mock_input):
        # Tests printed output if character inventory is empty and they select yes
        character_one = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 0,
                         'Dexterity': 0, 'Location': [5, 5], 'Inventory': [], 'Cursed': False}
        expected_output = """\nYou see the ruins of a grocery store. On top of a \
cash register is a fat cat smoking a cigarette!

^(,,ԾܫԾ,,)^
What? yes ? Look I know you don't got any money but can you go to the Human Museum and get me cigarettes? 
Head north west and take this.
You can't figure out how a cat would start smoking cigarettes but you head on your way
Your inventory: ['Me0w M1x: Binary Edition!']\n"""
        sud.location_three(character_one)
        self.assertEqual(mock_stout.getvalue(), expected_output)

    @patch('builtins.input', return_value='whatever')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_three2(self, mock_stout, mock_input):
        # Tests printed output if character inventory is empty and they select anything
        character_one = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 0,
                         'Dexterity': 0, 'Location': [5, 5], 'Inventory': [], 'Cursed': False}
        expected_output = """\nYou see the ruins of a grocery store. On top of a \
cash register is a fat cat smoking a cigarette!

^(,,ԾܫԾ,,)^
What? whatever ? Look I know you don't got any money but can you go to the Human Museum and get me cigarettes? 
Head north west and take this.
You can't figure out how a cat would start smoking cigarettes but you head on your way
Your inventory: ['Me0w M1x: Binary Edition!']\n"""
        sud.location_three(character_one)
        self.assertEqual(mock_stout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_three3(self, mock_stout):
        # Tests printed output if cigarettes are in character inventory
        character_one = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 0,
                         'Dexterity': 0, 'Location': [5, 5], 'Inventory': ['Cigarettes'], 'Cursed': False}
        expected_output = """\nYou see the ruins of a grocery store. On top of a \
cash register is a fat cat smoking a cigarette!

^(,,Ծ O Ծ,,)^
Wow ya got em thanks Bub! I put the CatNip in your inventory ;)
Your inventory: ['CatNip']\n"""
        sud.location_three(character_one)
        self.assertEqual(mock_stout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_three4(self, mock_stout):
        # Tests printed output if Meow mix is in character inventory
        character_one = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 0, 'Dexterity': 0,
                         'Location': [5, 5], 'Inventory': ['Me0w M1x: Binary Edition!'], 'Cursed': False}
        expected_output = """\nYou see the ruins of a grocery store. On top of a \
cash register is a fat cat smoking a cigarette!

^(,,Ծ__Ծ,,)^
NO CIGARETTES, NO CATNIP. Sorry Bub.
Your inventory: ['Me0w M1x: Binary Edition!']\n"""
        sud.location_three(character_one)
        self.assertEqual(mock_stout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_three5(self, mock_stout):
        # Tests printed output if Cat nip is in character inventory
        character_one = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 0, 'Dexterity': 0,
                         'Location': [5, 5], 'Inventory': ['CatNip'], 'Cursed': False}
        expected_output = """\nYou see the ruins of a grocery store. On top of a \
cash register is a fat cat smoking a cigarette!

^(,,Ծ__Ծ,,)^
NO CIGARETTES, NO CATNIP. Sorry Bub.
Your inventory: ['CatNip']\n"""
        sud.location_three(character_one)
        self.assertEqual(mock_stout.getvalue(), expected_output)
