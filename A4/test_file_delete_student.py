from unittest import TestCase
from A4 import student
from A4 import crud
from unittest.mock import patch
import io


class TestFileDeleteStudent(TestCase):
    def test_file_delete_student_added_student_deleted(self):
        new_list = []
        student1 = student.Student('Kylo', 'Ren', 'A01077789', False, [40, 50])
        crud.file_write(student1, 'testfile3.txt')
        crud.file_delete_student('A01077789', 'testfile3.txt')
        for i in crud.file_read('testfile3.txt'):
            new_list.append(i.__repr__())
        self.assertNotIn(student1.__repr__(), new_list)

    def test_file_delete_student_in_file_with_multiple_students(self):
        new_list = []
        student1 = student.Student('Kylo', 'Ren', 'A01077789', False, [40, 50])
        student2 = student.Student('Delete', 'Me', 'A01099985', True, [])
        crud.file_write(student1, 'testfile4.txt')
        crud.file_write(student2, 'testfile4.txt')
        crud.file_delete_student('A01099985', 'testfile4.txt')
        for i in crud.file_read('testfile3.txt'):
            new_list.append(i.__repr__())
        self.assertNotIn(student2.__repr__(), new_list)

    def test_file_delete_student_does_not_exist(self):
        student1 = student.Student('Kyla', 'Ren', 'A01077789', False, [40, 50])
        crud.file_write(student1, 'testfile5.txt')
        self.assertFalse(crud.file_delete_student('A01099985', 'testfile5.txt'))

    def test_file_delete_student_does_exist(self):
        student1 = student.Student('Kyla', 'Ren', 'A01077789', False, [40, 50])
        crud.file_write(student1, 'testfile6.txt')
        self.assertTrue(crud.file_delete_student('A01077789', 'testfile6.txt'))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_printed_output_true(self, mock_stdout):
        expected = 'We successfully deleted the student\n'
        student1 = student.Student('Kyla', 'Ren', 'A01077789', False, [40, 50])
        crud.file_write(student1, 'testfile7.txt')
        crud.file_delete_student('A01077789', 'testfile7.txt')
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_printed_output_false(self, mock_stdout):
        expected = 'We could not remove that student because they do not exist in the database\n'
        student1 = student.Student('Kyla', 'Ren', 'A01077789', False, [40, 50])
        crud.file_write(student1, 'testfile8.txt')
        crud.file_delete_student('A01011111', 'testfile8.txt')
        self.assertEqual(mock_stdout.getvalue(), expected)








