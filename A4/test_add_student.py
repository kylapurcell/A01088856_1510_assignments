from unittest import TestCase
from unittest.mock import patch
from A4 import crud
from A4 import student
import io


class TestAddStudent(TestCase):
    @patch('builtins.input', side_effect=['kyla', 'purcell', 'A01088856', 'true', '80', '-2'])
    def test_add_student_full(self, mock_input):
        student_clone = student.Student('Kyla', 'Purcell', 'A01088856', True, [80])
        self.assertEqual(student_clone.__repr__(), crud.add_student().__repr__())

    @patch('builtins.input', side_effect=['kyla', 'purcell', 'A01088856', 'true', '80', '-2'])
    def test_add_student_first_name(self, mock_input):
        student_clone = student.Student('Kyla', 'Purcell', 'A01088856', True, [80])
        self.assertEqual(student_clone.get_first_name(), crud.add_student().get_first_name())

    @patch('builtins.input', side_effect=['kyla', 'purcell', 'A01088856', 'true', '80', '-2'])
    def test_add_student_last_name(self, mock_input):
        student_clone = student.Student('Kyla', 'Purcell', 'A01088856', True, [80])
        self.assertEqual(student_clone.get_last_name(), crud.add_student().get_last_name())

    @patch('builtins.input', side_effect=['kyla', 'purcell', 'A01088856', 'true', '80', '-2'])
    def test_add_student_student_number(self, mock_input):
        student_clone = student.Student('Kyla', 'Purcell', 'A01088856', True, [80])
        self.assertEqual(student_clone.get_student_number(), crud.add_student().get_student_number())

    @patch('builtins.input', side_effect=['kyla', 'purcell', 'A01088856', 'true', '80', '-2'])
    def test_add_student_status(self, mock_input):
        student_clone = student.Student('Kyla', 'Purcell', 'A01088856', True, [80])
        self.assertEqual(student_clone.get_status(), crud.add_student().get_status())

    @patch('builtins.input', side_effect=['kyla', 'purcell', 'A01088856', 'true', '80', '-2'])
    def test_add_student_grades(self, mock_input):
        student_clone = student.Student('Kyla', 'Purcell', 'A01088856', True, [80])
        self.assertEqual(student_clone.get_grades_list(), crud.add_student().get_grades_list())

    @patch('builtins.input', side_effect=['kyla', 'purcell', 'A01088856', 'true', '-1'])
    def test_add_student_empty_grades(self, mock_input):
        student_clone = student.Student('Kyla', 'Purcell', 'A01088856', True, [])
        self.assertEqual(student_clone.get_grades_list(), crud.add_student().get_grades_list())

    @patch('builtins.input', side_effect=['kyla', 'purcell', 'B01088856', 'true', '80', '-2'])
    def test_add_student_invalid_student_number(self, mock_input):
        self.assertIsNone(crud.add_student())

    @patch('builtins.input', side_effect=['', 'purcell', 'A01088856', 'true', '80', '-2'])
    def test_add_student_invalid_first_name(self, mock_input):
        self.assertIsNone(crud.add_student())

    @patch('builtins.input', side_effect=['kyla', '', 'A01088856', 'true', '80', '-2'])
    def test_add_student_invalid_last_name(self, mock_input):
        self.assertIsNone(crud.add_student())


