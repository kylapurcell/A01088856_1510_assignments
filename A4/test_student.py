from unittest import TestCase
from A4 import student
from unittest.mock import patch
import io


class TestStudent(TestCase):

    def setUp(self):
        self.test_student = student.Student('Kyla', 'Purcell', 'A01088856', True, [80, 90, 75])
        self.test_student2 = student.Student('dahlia', 'billings', 'A01099976', False, [])

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
        expected = 'Name: Kyla Purcell Student Number: A01088856 Status: True Grades: 80 90 75\n'
        self.test_student.print_student_info()
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_calculate_student_gpa(self):
        expected = 81.66666666666667
        actual = self.test_student.calculate_student_gpa()
        self.assertEqual(expected, actual)

    def test_calculate_student_gpa_empty(self):
        expected = -1
        actual = self.test_student2.calculate_student_gpa()
        self.assertEqual(expected, actual)

    def test_set_student_grades(self):
        self.test_student.set_student_grades([70, 60, 100])
        self.assertEqual([70, 60, 100], self.test_student.get_grades_list())

    def test_set_student_first_name(self):
        self.test_student.set_student_first_name('Kylo')
        self.assertEqual('Kylo', self.test_student.get_first_name())

    def test_set_student_last_name(self):
        self.test_student.set_student_last_name('Purcel')
        self.assertEqual('Purcel', self.test_student.get_last_name())

    def test_set_student_status(self):
        self.test_student.set_student_status(False)
        self.assertEqual(False, self.test_student.get_status())

    def test_format_first_name(self):
        self.test_student2.format_first_name()
        self.assertEqual('Dahlia', self.test_student2.get_first_name())

    def test_format_last_name(self):
        self.test_student2.format_last_name()
        self.assertEqual('Billings', self.test_student2.get_last_name())

    def test_repr_(self):
        expected = 'Kyla Purcell A01088856 True 80 90 75'
        self.assertEqual(expected, self.test_student.__repr__())



