import unittest
from Code.caesar_cipher import caesarCipher

class TestCaesarCipher(unittest.TestCase):
    def test_basic_encryption_positive_shift(self):
        self.assertEqual(caesarCipher("abc", 1), "bcd")

    def test_basic_encryption_negative_shift(self):
        self.assertEqual(caesarCipher("abc", -1), "zab")

    def test_encryption_with_spaces(self):
        self.assertEqual(caesarCipher("A   Z", 1), "b   a")

    def test_large_positive_shift(self):
        self.assertEqual(caesarCipher("abc", 260), "abc")

    def test_large_negative_shift(self):
        self.assertEqual(caesarCipher("abc", -260), "abc")

    def test_empty_string(self):
        self.assertEqual(caesarCipher("", 3), "")

    def test_zero_shift(self):
        self.assertEqual(caesarCipher("abc", 0), "abc")

    def test_large_shift_greater_than_alphabet_numbers(self):
        self.assertEqual(caesarCipher("abC", 1), "bcD")

    def test_symbols(self):
        self.assertEqual(caesarCipher(".:;,][(()}{123_", 20), ".:;,][(()}{123_")

if __name__ == "__main__":
    unittest.main()