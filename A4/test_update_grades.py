from unittest import TestCase
from A4 import crud
from A4 import student
from unittest.mock import patch
import io


class TestUpdateGrades(TestCase):
    @patch('builtins.input', return_value='85')
    def test_update_grades_valid_grade(self, mock_input):
        new_student = student.Student('Kylo', 'Purcell', 'A01088857', True, [80, 90, 70])
        crud.file_write(new_student, 'testfile9.txt')
        crud.update_grades('A01088857', 'testfile9.txt')
        student_list = crud.file_read('testfile9.txt')
        crud.update_file([], 'testfile9.txt')
        self.assertEqual([80, 90, 70, 85], student_list[0].get_grades_list())

    @patch('builtins.input', return_value='101')
    def test_update_grades_invalid_grade_high(self, mock_input):
        new_student = student.Student('Kylee', 'Purcell', 'A01088859', True, [60, 90, 40])
        crud.file_write(new_student, 'testfile10.txt')
        crud.update_grades('A01088859', 'testfile10.txt')
        student_list = crud.file_read('testfile10.txt')
        crud.update_file([], 'testfile10.txt')
        self.assertEqual([60, 90, 40], student_list[0].get_grades_list())

    @patch('builtins.input', return_value='-3')
    def test_update_grades_invalid_grade_low(self, mock_input):
        new_student = student.Student('Kylee', 'Purcell', 'A01088859', True, [60, 90, 40])
        crud.file_write(new_student, 'testfile11.txt')
        crud.update_grades('A01088859', 'testfile11.txt')
        student_list = crud.file_read('testfile11.txt')
        crud.update_file([], 'testfile11.txt')
        self.assertEqual([60, 90, 40], student_list[0].get_grades_list())

    @patch('builtins.input', return_value='85')
    def test_update_grades_is_true(self, mock_input):
        new_student = student.Student('Kylo', 'Purcell', 'A01088857', True, [80, 90, 70])
        crud.file_write(new_student, 'testfile12.txt')
        self.assertTrue(crud.update_grades('A01088857', 'testfile12.txt'))

    @patch('builtins.input', return_value='85')
    def test_update_grades_is_false(self, mock_input):
        new_student = student.Student('Kylo', 'Purcell', 'A01088857', True, [80, 90, 70])
        crud.file_write(new_student, 'testfile13.txt')
        self.assertFalse(crud.update_grades('A01088888', 'testfile13.txt'))

    @patch('builtins.input', return_value='85')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_printed_student_does_not_exist(self, mock_stdout, mock_input):
        new_student = student.Student('Kylo', 'Purcell', 'A01088857', True, [80, 90, 70])
        crud.file_write(new_student, 'testfile14.txt')
        crud.update_grades('A01088888', 'testfile14.txt')
        expected = 'We could not find that student in our file or grade could not be added\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('builtins.input', return_value='185')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_printed_student_grade_invalid(self, mock_stdout, mock_input):
        new_student = student.Student('Kylo', 'Purcell', 'A01088857', True, [80, 90, 70])
        crud.file_write(new_student, 'testfile15.txt')
        crud.update_grades('A01088857', 'testfile15.txt')
        crud.update_file([], 'testfile15.txt')
        expected = 'Grades cannot include numbers below zero or above 100\n'\
                   'We could not find that student in our file or grade could not be added\n'
        self.assertEqual(mock_stdout.getvalue(), expected)






