import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_elements(self):
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 9, 2, 3]), 9)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([-1, 0, 1, 2]), 2)

    def test_only_negative_numbers(self):
        self.assertEqual(max_integer([-5, -2, -8, -3]), -2)

if __name__ == "__main__":
    unittest.main()
