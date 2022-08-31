import unittest

from src.Algorithms.recursion.recursion_1 import power
from src.Algorithms.recursion.recursion_2 import sum_of_nums
from src.Algorithms.recursion.recursion_3 import len_of_list
from src.Algorithms.recursion.recursion_4 import is_str_palindrome
from src.Algorithms.recursion.recursion_5 import print_even_elements
from src.Algorithms.recursion.recursion_6 import print_every_second


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
        self.assertEqual(1 / 125, power(5, -3))

    def test_sum_of_nums(self):
        self.assertEqual(1, sum_of_nums(1))
        self.assertEqual(1, sum_of_nums(10))
        self.assertEqual(1, sum_of_nums(100))
        self.assertEqual(6, sum_of_nums(105))
        self.assertEqual(6, sum_of_nums(-105))

    def test_len_of_list(self):
        self.assertEqual(3, len_of_list([1, 4, 5]))
        self.assertEqual(0, len_of_list([]))
        self.assertEqual(1, len_of_list([1]))
        self.assertEqual(3, len_of_list([1, "3", [1, 2]]))

    def test_is_str_palindrome(self):
        self.assertEqual(True, is_str_palindrome("aba"))
        self.assertEqual(True, is_str_palindrome("a"))
        self.assertEqual(True, is_str_palindrome("abbba"))
        self.assertEqual(True, is_str_palindrome("abccba"))
        self.assertEqual(False, is_str_palindrome("abc"))
        self.assertEqual(False, is_str_palindrome("ab"))

    def test_print_even_elements(self):
        print_even_elements([1, 2, 3, 4, 5, 6, 8, 10, 10])
        print_even_elements([])
        print_even_elements(['fas', 'asdf', 26])

    def test_print_every_second(self):
        print_every_second([1, 2, 3, 4, 5, 6])
