from unittest import TestCase
from A4 import crud


class TestMakeBoolean(TestCase):
    def test_make_boolean_true_lower(self):
        self.assertTrue(crud.make_boolean('true'))

    def test_make_boolean_true_upper(self):
        self.assertTrue(crud.make_boolean('True'))

    def test_make_boolean_false_lower(self):
        self.assertFalse(crud.make_boolean('false'))

    def test_make_boolean_false_upper(self):
        self.assertFalse(crud.make_boolean('False'))

    def test_make_boolean_normal_string(self):
        self.assertFalse(crud.make_boolean('hello'))
