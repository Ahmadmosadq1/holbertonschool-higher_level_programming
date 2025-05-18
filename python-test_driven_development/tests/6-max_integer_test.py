import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for max_integer()."""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_elements(self):
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

if __name__ == "__main__":
    unittest.main()
