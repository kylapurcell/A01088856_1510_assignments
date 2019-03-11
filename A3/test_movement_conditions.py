from unittest import TestCase
import io
from A3 import sud
from unittest.mock import patch


class TestMovementConditions(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_movement_conditions(self,mock_stdout):
        character = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 10,
                     'Dexterity': 0, 'Location': [0, 2], 'Inventory': [], 'Cursed': False}
        expected_output = " You've reached the end of this world please turn back or head east or west\n"
        sud.movement_conditions(character, 'North')
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_movement_conditions2(self, mock_stdout):
        character = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 10,
                     'Dexterity': 0, 'Location': [2, 0], 'Inventory': [], 'Cursed': False}
        expected_output = " You've reached the end of this world please turn back or head north or south\n"
        sud.movement_conditions(character, 'West')
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_movement_conditions3(self, mock_stdout):
        character = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 10,
                     'Dexterity': 0, 'Location': [2, 6], 'Inventory': [], 'Cursed': False}
        expected_output = " You've reached the end of this world please turn back or head north or south\n"
        sud.movement_conditions(character, 'East')
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_movement_conditions4(self, mock_stdout):
        character = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 10,
                     'Dexterity': 0, 'Location': [6, 2], 'Inventory': [], 'Cursed': False}
        expected_output = " You've reached the end of this world please turn back or head east or west\n"
        sud.movement_conditions(character, 'South')
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_movement_conditions5(self, mock_stdout):
        character = {'Name': 'Kyla', 'Class': 'Hello Kitty', 'Health': 10,
                     'Dexterity': 0, 'Location': [6, 2], 'Inventory': [], 'Cursed': False}
        expected_output = "I do not understand that command. Please type North ,West, South, East, or Quit\n"
        sud.movement_conditions(character, 'Sooth')
        self.assertEqual(mock_stdout.getvalue(), expected_output)
