from unittest import TestCase
from unittest.mock import patch
from A4 import crud
from A4 import student
import io


class TestPrintClassList(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_class_list_one_student(self, mock_stdout):
        new_student = student.Student('Kylo', 'Purcell', 'A01088857', True, [80, 90, 70])
        filename = 'testfile16.txt'
        crud.file_write(new_student, filename)
        student_list = crud.file_read(filename)
        crud.print_class_list('testfile16.txt')
        expected = 'Name: Kylo Purcell Student Number: A01088857 Status: True Grades: 80 90 70\n' \
                   'There are 1 students currently enrolled in this school\n'
        crud.update_file([], filename)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_class_list_two_student(self, mock_stdout):
        new_student = student.Student('Kylo', 'Purcell', 'A01088857', True, [80, 90, 70])
        new_student2 = student.Student('Kyla', 'Purcell', 'A01088856', True, [80])
        filename = 'testfile17.txt'
        crud.file_write(new_student, filename)
        crud.file_write(new_student2, filename)
        student_list = crud.file_read(filename)
        crud.print_class_list(filename)
        expected = 'Name: Kylo Purcell Student Number: A01088857 Status: True Grades: 80 90 70\n' \
                   'Name: Kyla Purcell Student Number: A01088856 Status: True Grades: 80\n'\
                   'There are 2 students currently enrolled in this school\n'
        crud.update_file([], filename)
        self.assertEqual(mock_stdout.getvalue(), expected)




