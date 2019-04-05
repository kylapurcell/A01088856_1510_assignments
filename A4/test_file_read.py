from unittest import TestCase
from unittest.mock import patch
from unittest.mock import mock_open
from A4 import crud
from A4 import student


class TestFileRead(TestCase):
    @patch('builtins.open', mock_open(read_data="Kyla Purcell A01088856 True 80 90 100"))
    def test_file_read_one_student(self):
        reader = crud.file_read('testfile1.txt')
        student1 = student.Student('Kyla', 'Purcell', 'A01088856', True, [80, 90, 100])
        self.assertEqual(student1.__repr__(), reader[0].__repr__())

    @patch('builtins.open', mock_open(read_data="Kyla Purcell A01088856 True 80 90 100 "
                                                "\n Kaylee Hello A01099967 False "))
    def test_file_read_two_students_equal_list(self):
        reader = crud.file_read('testfile1.txt')
        new_list = []
        student1 = student.Student('Kyla', 'Purcell', 'A01088856', True, [80, 90, 100])
        student2 = student.Student('Kaylee', 'Hello', 'A01099967', False, [])
        for i in reader:
            new_list.append(i.__repr__())
        self.assertEqual([student1.__repr__(), student2.__repr__()], new_list)

    @patch('builtins.open', mock_open(read_data="Kyla Purcell A01088856 True 80 90 100"))
    def test_file_read_is_type_list(self):
        reader = crud.file_read('testfile1.txt')
        self.assertEqual(list, type(reader))

    @patch('builtins.open', mock_open(read_data="Kyla Purcell A01088856 True 80 90 100"))
    def test_file_read_is_list_of_objects(self):
        reader = crud.file_read('testfile1.txt')
        self.assertIsInstance(reader[0], object)

