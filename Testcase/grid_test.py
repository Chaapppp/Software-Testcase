import unittest
from Code.grid import gridChallenge  

class TestGridChallenge(unittest.TestCase):
    def test_empty_grid(self):
        grid = []
        self.assertEqual(gridChallenge(grid), "YES")

    def test_Yes_grid(self):
        self.assertEqual(gridChallenge(["hijklmn"]), "YES")

    def test_No_grid(self):
        self.assertEqual(gridChallenge(["ebacd", "fghzj", "olmkn", "trpqs", "xywuq"]), "No")

    def test_basic_unsorted_grid(self):
        self.assertEqual(gridChallenge(["a", "f", "d", "o", "e"]), "YES")

    def test_single_row_grid(self):
        self.assertEqual(gridChallenge(["abc", "def", "ghi"]), "YES")

    def test_single_column_grid(self):
        self.assertEqual(gridChallenge(["cba", "fed", "ihg"]), "YES")

    def test_empty_grid(self):
        self.assertEqual(gridChallenge(["DEsom"]), "YES")

    def test_repeated_characters_in_column(self):
        self.assertEqual(gridChallenge(["aed", "bfc", "gih"]), "NO")

    def test_repeated_grid(self):
        self.assertEqual(gridChallenge(["aaaa", "aaaa", "aaaa"]), "YES")

    def test_large_grid_mix(self):
        self.assertEqual(gridChallenge(["eDcBA", "jIhGF", "nMLko", "sqprt", "vUxYw"]), "NO")

if __name__ == "__main__":
    unittest.main()