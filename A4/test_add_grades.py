from unittest import TestCase
from A4 import crud
from unittest.mock import patch
import io


class TestAddGrades(TestCase):
    @patch('builtins.input', side_effect=['80', '90', '100', '2'])
    def test_add_grades_normal_case(self, mock_input):
        self.assertEqual([80, 90, 100], crud.add_grades())

    @patch('builtins.input', return_value='1')
    def test_add_grades_empty_list(self, mock_input):
        self.assertEqual([], crud.add_grades())

    @patch('builtins.input', side_effect=['80', '90', '400', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_grades_one_invalid_printed(self, mock_stdout, mock_input):
        expected = 'That grade is not valid\n'
        crud.add_grades()
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('builtins.input', side_effect=['80', '90', '400', '2'])
    def test_add_grades_one_invalid_above_100(self, mock_input):
        self.assertEqual([80, 90], crud.add_grades())












