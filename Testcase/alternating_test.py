import unittest
from Code.alternating import alternatingCharacters

class TestAlternatingCharacters(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(alternatingCharacters(""), 0)

    def test_one_characters(self):
        self.assertEqual(alternatingCharacters("a"), 0)

    def test_all_characters_repeated_once(self):
        self.assertEqual(alternatingCharacters("aabbcc"), 3)

    def test_same_character(self):
        self.assertEqual(alternatingCharacters("aaaaaaaaaaaaaaaa"), 3)

    def test_multiple_repeated_characters(self):
        self.assertEqual(alternatingCharacters("aabbaccbaccc"), 5)

    def test_alternating_characters(self):
        self.assertEqual(alternatingCharacters("abababab"), 0)

    def test_saparate_pair_alternating_characters(self):
        self.assertEqual(alternatingCharacters("abcdeabcde"), 0)

if __name__ == '__main__':
    unittest.main()