from unittest import TestCase
from unittest.mock import patch
import io
from A3 import sud


class TestLocationNormal(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_normal(self, mock_stdout):
        character = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 10,
                     'Dexterity': 0, 'Location': [2, 1], 'Inventory': [], 'Cursed': False}
        expected_output = """You are in the valley, a barren location, that likely used to be a suburb before the war
In the distance you see a large building with sturdy looking pillars\n"""
        sud.location_normal(character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_normal2(self, mock_stdout):
        character = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 10,
                     'Dexterity': 0, 'Location': [4, 4], 'Inventory': [], 'Cursed': False}
        expected_output = """You are in the city ruins, a charred location filled with decaying buildings
In the distance you see the run down remains of a grocery store\n"""
        sud.location_normal(character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_normal3(self, mock_stdout):
        character = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 10,
                     'Dexterity': 0, 'Location': [4, 3], 'Inventory': [], 'Cursed': False}
        expected_output = """You are in the lake region, green radioactive particles shimmer in the brown \
coloured waters
You feel something in the humid air as if this region is the location of an Easter Egg
Easter Egg? You have no idea what that is or why you thought of it\n"""
        sud.location_normal(character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_normal4(self, mock_stdout):
        character = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 10,
                     'Dexterity': 0, 'Location': [3, 4], 'Inventory': [], 'Cursed': False}
        expected_output = """You are crossing a bridge leading to the outskirts of the city ruins
In the distance you spot a large building in good condition surrounded by stacks of burnt books\n"""
        sud.location_normal(character)
        self.assertEqual(mock_stdout.getvalue(), expected_output)


