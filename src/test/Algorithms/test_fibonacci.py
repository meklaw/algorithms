import unittest

from src.Algorithms.fibonacci import fib, fib_digit, fib_mod


class TestFib(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(7), 13)
        self.assertEqual(fib(8), 21)
        self.assertEqual(fib(9), 34)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(20), 6765)

    def test_fib_digit(self):
        self.assertEqual(fib_digit(0), 0)
        self.assertEqual(fib_digit(1), 1)
        self.assertEqual(fib_digit(2), 1)
        self.assertEqual(fib_digit(3), 2)
        self.assertEqual(fib_digit(4), 3)
        self.assertEqual(fib_digit(5), 5)
        self.assertEqual(fib_digit(6), 8)
        self.assertEqual(fib_digit(7), 3)
        self.assertEqual(fib_digit(8), 1)
        self.assertEqual(fib_digit(9), 4)
        self.assertEqual(fib_digit(10), 5)
        self.assertEqual(fib_digit(20), 5)

    def test_fib_mod(self):
        self.assertEqual(fib_mod(10, 2), 1)
        self.assertEqual(fib_mod(11, 4), 1)
        self.assertEqual(fib_mod(15, 4), 2)
        self.assertEqual(fib_mod(18, 4), 0)
        self.assertEqual(fib_mod(1025, 55), 5)
        self.assertEqual(fib_mod(20, 1000), 20)
        self.assertEqual(fib_mod(12589, 369), 89)
        self.assertEqual(fib_mod(1598753, 25897), 20305)
        self.assertEqual(fib_mod(60282445765134413, 2263), 974)
