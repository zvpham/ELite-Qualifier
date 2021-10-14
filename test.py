import unittest
import main

class TestCheckErrors(unittest.TestCase):

    def test_odd_num(self):
        self.assertTrue(main.check_errors())

    def test_even_num(self):
        self.assertFalse(is_odd(2))

    # edge case
    def test_zero(self):
        self.assertFalse(is_odd(0))

