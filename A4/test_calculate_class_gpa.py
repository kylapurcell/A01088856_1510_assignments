from unittest import TestCase
from A4 import crud
from unittest.mock import patch
from unittest.mock import mock_open
import io


class TestCalculateClassGpa(TestCase):

    @patch('builtins.open', mock_open(read_data="Kyla Purcell A01088856 True 80 90 100 \n Kyla Burcell A01077787 False"
                                                "60 72 65"))
    def test_calculate_class_gpa_with_graded_students(self):
        self.assertEqual(79.25, crud.calculate_class_gpa('testfile1.txt'))

    @patch('builtins.open', mock_open(read_data="Kyla Purcell A01088856 True 80 90 100 "
                                                "\n Kyla Burcell A01077787 False"))
    def test_calculate_class_gpa_with_one_no_grades(self):
        self.assertEqual(90.0, crud.calculate_class_gpa('testfile1.txt'))

    @patch('builtins.open', mock_open(read_data="Kyla Purcell A01088856 True 80 90 100 "
                                                "\n Kyla Burcell A01077787 False"))
    def test_is_type_float(self):
        self.assertEqual(float, type(crud.calculate_class_gpa('testfile1.txt')))

    @patch('builtins.open', mock_open(read_data="Kyla Purcell A01088856 True 80 90 100 "
                                                "\n Kyla Burcell A01077787 False"))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_printed_output_no_grades(self, mock_stdout):
        expected = 'Students with no final grades yet (GPA = -1) will not be counted in this calculation\n' \
                   'Kyla Burcell has no final grades yet so their gpa is currently -1\n'
        crud.calculate_class_gpa('testfile1.txt')
        self.assertEqual(mock_stdout.getvalue(), expected)






