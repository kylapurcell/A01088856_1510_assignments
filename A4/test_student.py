from unittest import TestCase
from A4 import student
from unittest.mock import patch
import io

class TestStudent(TestCase):

    def setUp(self):
        self.test_student = student.Student('Kyla', 'Purcell', 'A01088856', True, [80, 90, 75])
        self.test_student2 = student.Student('Dahlia', 'Billings', 'A01099976', False, [])

    def test_get_first_name(self):
        expected = "Kyla"
        actual = self.test_student.get_first_name()
        self.assertEqual(expected, actual)

    def test_get_last_name(self):
        expected = 'Purcell'
        actual = self.test_student.get_last_name()
        self.assertEqual(expected, actual)

    def test_get_student_number(self):
        expected = 'A01088856'
        actual = self.test_student.get_student_number()
        self.assertEqual(expected, actual)

    def test_get_status(self):
        expected = True
        actual = self.test_student.get_status()
        self.assertEqual(expected, actual)

    def test_get_grades_list(self):
        expected = [80, 90, 75]
        actual = self.test_student.get_grades_list()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_student_info(self, mock_stdout):
        expected = 'Kyla Purcell A01088856 True 80 90 75\n'
        self.test_student.print_student_info()
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_calculate_student_gpa(self):
        expected = 81.66666666666667
        actual = self.test_student.calculate_student_gpa()
        self.assertEqual(expected, actual)

    def test_calculate_student_gpa_empty(self):
        expected = 0
        actual = self.test_student2.calculate_student_gpa()
        self.assertEqual(expected, actual)


    #def test_set_student_grades(self,[]):


    #def test_set_student_first_name(self):

    #def test_set_student_last_name(self):


    #def test_set_student_status(self):

