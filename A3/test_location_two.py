from unittest import TestCase
from unittest.mock import patch
import io
import random
from A3 import sud


class TestLocationTwo(TestCase):
    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_two(self, mock_stdout, mock_input):
        expected_output = """\nYou have entered the large ruins of a library, in the middle of the room stands a \
studious looking cat wearing glasses with the word 'Google' written on them.

^⨀ᴥ⨀^
Hello welcome to the library, I can use my state of art technology to  help you access information about this world
The Monster Encyclopedia:
      Ghoul: Radioactive, humanoid creature with green flesh. Rumored to be whats left of humans.
      Radioactive Rat : An over sized rat. Sometimes a tasty snack for certain cat species.
      Rogue Robot: A robot with glitched programming. 
      Mutated Creature: Mutated beyond belief. Hard to tell what this creature is. 
      Pax: The demon thief of destiny. Feared by all and said to curse those unlucky enough to meet him.
Thanks for coming. If you require my service again please visit this location again\n"""
        sud.location_two()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', return_value='any output')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_location_two2(self, mock_stdout, mock_input):
        expected_output = """\nYou have entered the large ruins of a library, in the middle of the room stands a \
studious looking cat wearing glasses with the word 'Google' written on them.

^⨀ᴥ⨀^
Hello welcome to the library, I can use my state of art technology to  help you access information about this world
Thanks for coming. If you require my service again please visit this location again\n"""
        sud.location_two()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

