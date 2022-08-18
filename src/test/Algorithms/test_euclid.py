import math
import unittest

from src.Algorithms.euclid import euclidGCD


class TestEuclid(unittest.TestCase):
    def test_euclidGCD(self):
        self.assertEqual(euclidGCD(0, 0), 0)
        self.assertEqual(euclidGCD(0, 1), 1)
        self.assertEqual(euclidGCD(1, 0), 1)
        self.assertEqual(euclidGCD(1, 2), 1)
        self.assertEqual(euclidGCD(2, 1), 1)
        self.assertEqual(euclidGCD(4, 2), 2)
        self.assertEqual(euclidGCD(2, 4), 2)
        self.assertEqual(euclidGCD(12, 16), 4)
        self.assertEqual(euclidGCD(16, 12), 4)

