import unittest

from src.Algorithms.recursion.recursion_1 import power
from src.Algorithms.recursion.recursion_2 import sum_of_nums


class TestRecursion(unittest.TestCase):
    def test_power(self):
        self.assertEqual(1, power(1, 0))
        self.assertEqual(1, power(1, 1))
        self.assertEqual(1, power(1, -1))
        self.assertEqual(1, power(1, 100))
        self.assertEqual(1, power(1, -100))
        self.assertEqual(1, power(100, 0))
        self.assertEqual(100, power(100, 1))
        self.assertEqual(10000, power(100, 2))
        self.assertEqual(1000000, power(100, 3))
        self.assertEqual(125, power(5, 3))
        self.assertEqual(1/125, power(5, -3))

    def test_sum_of_nums(self):
        self.assertEqual(1, sum_of_nums(1))
        self.assertEqual(1, sum_of_nums(10))
        self.assertEqual(1, sum_of_nums(100))
        self.assertEqual(6, sum_of_nums(105))
        self.assertEqual(6, sum_of_nums(-105))