from unittest import TestCase
from A4 import crud
from A4 import student
from unittest.mock import patch
import io


class TestFileWrite(TestCase):
    def test_file_write(self):
        new_student = student.Student('Kylo', 'Purcell', 'A01088857', True, [80, 90, 70])
        crud.file_write(new_student)
        student_list = crud.file_read()
        for i in student_list:
            if i == new_student:
                self.assertEqual(i, new_student)
        crud.file_delete_student('A01088857')








