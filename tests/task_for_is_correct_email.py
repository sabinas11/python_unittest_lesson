from unittest import TestCase

from functions.gcd import gcd
from functions.plus import plus

from functions.email import is_correct_email
class EmailFunctionTestCase(TestCase):
    def test_returns_True_for_correct_email(self):
        self.assertTrue(is_correct_email("maseteralish@gmail.com"))
        self.assertTrue(is_correct_email("themonrealstudio@gmail.com"))

    def test_returns_False_for_correct_email(self):
        self.assertFalse(is_correct_email("themonrea@lstudio@gmail.com"))
        self.assertFalse(is_correct_email("@gmail.com"))
        self.assertFalse(is_correct_email("aidana.yahoo.com"))



