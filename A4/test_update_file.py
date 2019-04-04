from unittest import TestCase
from A4 import crud
from A4 import student


class TestUpdateFile(TestCase):
    def test_update_file_normal_case(self):
        student1 = student.Student('Kylo', 'Ren', 'A01077789', False, [40, 50])
        crud.update_file([student1], 'testfile2.txt')
        read = crud.file_read('testfile2.txt')
        self.assertEqual([student1][0].__repr__(), read[0].__repr__())

    def test_update_file_returns_none(self):
        student1 = student.Student('Kylo', 'Ren', 'A01077789', False, [40, 50])
        self.assertIsNone(crud.update_file([student1], 'testfile2.txt'))




