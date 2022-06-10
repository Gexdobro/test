import unittest
from src.utilities import add

class TestHelpers(unittest.TestCase):
    def test_1_should_equal_1(self):
        self.assertEqual(1, 1)
    def test_add_1_and_1_should_equal_2(self):
        self.assertEqual(2, add(1, 1))

if __name__ == "__main__":
    unittest.main()