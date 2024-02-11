import unittest
from Code.funny_str import funnyString

class TestFunnyString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(funnyString(""), "Funny")

    def test_one_character(self):
        self.assertEqual(funnyString("a"), "Funny")
    
    def test_characters_funny(self):
        self.assertEqual(funnyString("acxz"), "Funny")

    def test_characters_not_funny(self):
        self.assertEqual(funnyString("bdgk"), "Not Funny")

    def test_funny_string_repeated_characters(self):
        self.assertEqual(funnyString("aaaa"), "Funny")

    def test_characters_mix(self):
        self.assertEqual(funnyString("CdEfGhIjKlMnOpQrStUvWxYzaA"), "Funny")

    def test_special_characters(self):
        self.assertEqual(funnyString("!@#(__'!a@b^&*(c)_')[{$'", "Not Funny"))

    def test_numbers(self):
        self.assertEqual(funnyString("3456"), "Funny")

if __name__ == "__main__":
    unittest.main()