from unittest import TestCase
from A4 import crud
from unittest.mock import patch
import io

class TestPrintMenuOptions(TestCase):

    @patch('builtins.input', return_value='1')
    def test_print_menu_options_one_case(self, mock_input):
        self.assertEqual(1, crud.print_menu_options())

    @patch('builtins.input', return_value='2')
    def test_print_menu_options_two_case(self, mock_input):
        self.assertEqual(2, crud.print_menu_options())

    @patch('builtins.input', return_value='3')
    def test_print_menu_options_three_case(self, mock_input):
        self.assertEqual(3, crud.print_menu_options())

    @patch('builtins.input', return_value='4')
    def test_print_menu_options_four_case(self, mock_input):
        self.assertEqual(4, crud.print_menu_options())

    @patch('builtins.input', return_value='5')
    def test_print_menu_options_five_case(self, mock_input):
        self.assertEqual(5, crud.print_menu_options())

    @patch('builtins.input', return_value='6')
    def test_print_menu_options_six_case(self, mock_input):
        self.assertEqual(6, crud.print_menu_options())

    @patch('builtins.input', return_value='6')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_menu_options_printed_output(self, mock_stdout, mock_input):
        crud.print_menu_options()
        expected = (' 1.Add Student \n 2.Delete Student \n 3.Calculate Class Average \n'
                    ' 4.Print Class List \n 5.Add Grade To Student Record \n 6.Quit\n')
        self.assertEqual(mock_stdout.getvalue(), expected)
