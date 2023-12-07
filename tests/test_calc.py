"""Unit tests for the calc.py module."""

import unittest
from calc import add_numbers, calculate_average_of_two_lists, multiply_numbers

class TestCalc(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)
        self.assertEqual(add_numbers(-1, -2), -3)
        self.assertEqual(add_numbers(-1, 2), 1)

    def test_calculate_average_of_two_lists(self):
        self.assertEqual(calculate_average_of_two_lists([1, 2], []), 1.5)
        self.assertEqual(calculate_average_of_two_lists([], [3, 4]), 3.5)
        self.assertEqual(calculate_average_of_two_lists([1, 2], [3, 4]), 2.5)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(3, 4), 12)
        self.assertEqual(multiply_numbers(-3, 4), -12)

if __name__ == '__main__':
    unittest.main()
