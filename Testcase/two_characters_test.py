import unittest
from Code.two_characters import twoCharacters

class Testtwochar(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(twoCharacters(""), 0)

    def test_string_one_character(self):
        self.assertEqual(twoCharacters("a"), 0)

    def test_isamel_characters(self):
        self.assertEqual(twoCharacters("aaaaa"), 0)

    def test_string_unique_characters_no_alternating(self):
        self.assertEqual(twoCharacters("abcabcabc"), 6)

    def test_alternating_characters(self):
        self.assertEqual(twoCharacters("abcabc"), 4)

    def test_string_mixed_characters_alternating(self):
        self.assertEqual(twoCharacters("a1b2c3d4e5"), 2)

    def test_string_special_characters(self):
        self.assertEqual(twoCharacters("!@#$%^&*()"), 2)

    def test_string_numbers(self):
        self.assertEqual(twoCharacters("123456789"), 2)

    def test_string_mix(self):
        self.assertEqual(twoCharacters("AbCdEfGhIjK"), 2)

if __name__ == '__main__':
    unittest.main()