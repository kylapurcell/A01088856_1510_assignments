from unittest import TestCase
from A4 import crud
from A4 import student
from unittest.mock import patch
import io


class TestFileWrite(TestCase):
    def test_file_write_normal_case(self):
        new_student = student.Student('Kylo', 'Purcell', 'A01088857', True, [80, 90, 70])
        filename = 'testfile1.txt'
        crud.file_write(new_student, filename)
        student_list = crud.file_read('testfile1.txt')
        self.assertEqual(new_student.__repr__(), student_list[len(student_list)-1].__repr__())

    def test_file_write_no_grades(self):
        new_student = student.Student('Kylo', 'Purcell', 'A01088857', True, [])
        filename = 'testfile1.txt'
        crud.file_write(new_student, filename)
        student_list = crud.file_read('testfile1.txt')
        self.assertEqual(new_student.__repr__(), student_list[len(student_list) - 1].__repr__())

    def test_file_write_returns_true(self):
        new_student = student.Student('Kylo', 'Purcell', 'A01088857', True, [80, 90, 70])
        filename = 'testfile1.txt'
        self.assertTrue(crud.file_write(new_student, filename))

    def test_file_write_returns_false(self):
        new_student = None
        filename = 'testfile1.txt'
        self.assertFalse(crud.file_write(new_student, filename))








