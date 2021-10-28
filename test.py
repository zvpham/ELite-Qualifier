import unittest
import main

class TestCheckErrors(unittest.TestCase):

    def test_odd_num(self):
        self.assertTrue(main.check_errors())

    def test_gibberish_word(self):
        self.assertTrue(main.suggest("sfesfes", main.load_words()) == "")


    # edge case
    def test_zero(self):
        self.assertFalse(is_odd(0))

