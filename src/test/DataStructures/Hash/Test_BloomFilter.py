import unittest

from src.DataStructures.Hash.BloomFilter import BloomFilter


class TestBloomFilter(unittest.TestCase):
    def test_hash1(self):
        filter = BloomFilter(32)
        self.assertTrue(filter.hash1("0123456789") < filter.filter_len)
        self.assertTrue(filter.hash1("1234567890") < filter.filter_len)
        self.assertTrue(filter.hash1("2345678901") < filter.filter_len)
        self.assertTrue(filter.hash1("3456789012") < filter.filter_len)
        self.assertTrue(filter.hash1("4567890123") < filter.filter_len)
        self.assertTrue(filter.hash1("5678901234") < filter.filter_len)
        self.assertTrue(filter.hash1("6789012345") < filter.filter_len)
        self.assertTrue(filter.hash1("7890123456") < filter.filter_len)
        self.assertTrue(filter.hash1("8901234567") < filter.filter_len)
        self.assertTrue(filter.hash1("9012345678") < filter.filter_len)

    def test_hash2(self):
        filter = BloomFilter(32)
        self.assertTrue(filter.hash2("0123456789") < filter.filter_len)
        self.assertTrue(filter.hash2("1234567890") < filter.filter_len)
        self.assertTrue(filter.hash2("2345678901") < filter.filter_len)
        self.assertTrue(filter.hash2("3456789012") < filter.filter_len)
        self.assertTrue(filter.hash2("4567890123") < filter.filter_len)
        self.assertTrue(filter.hash2("5678901234") < filter.filter_len)
        self.assertTrue(filter.hash2("6789012345") < filter.filter_len)
        self.assertTrue(filter.hash2("7890123456") < filter.filter_len)
        self.assertTrue(filter.hash2("8901234567") < filter.filter_len)
        self.assertTrue(filter.hash2("9012345678") < filter.filter_len)

    def test_add(self):
        filter = BloomFilter(32)
        filter.add("0123456789")
        self.assertEqual(filter.array, filter.hash1("0123456789") | filter.hash2("0123456789"))
        before = filter.array
        filter.add("1234567890")
        self.assertEqual(filter.array, before | filter.hash1("1234567890") | filter.hash2("1234567890"))
        before = filter.array
        filter.add("2345678901")
        self.assertEqual(filter.array, before | filter.hash1("2345678901") | filter.hash2("2345678901"))
        before = filter.array
        filter.add("3456789012")
        self.assertEqual(filter.array, before | filter.hash1("3456789012") | filter.hash2("3456789012"))
        before = filter.array
        filter.add("4567890123")
        self.assertEqual(filter.array, before | filter.hash1("4567890123") | filter.hash2("4567890123"))
        before = filter.array
        filter.add("5678901234")
        self.assertEqual(filter.array, before | filter.hash1("5678901234") | filter.hash2("5678901234"))
        before = filter.array
        filter.add("6789012345")
        self.assertEqual(filter.array, before | filter.hash1("6789012345") | filter.hash2("6789012345"))
        before = filter.array
        filter.add("7890123456")
        self.assertEqual(filter.array, before | filter.hash1("7890123456") | filter.hash2("7890123456"))
        before = filter.array
        filter.add("8901234567")
        self.assertEqual(filter.array, before | filter.hash1("8901234567") | filter.hash2("8901234567"))
        before = filter.array
        filter.add("9012345678")
        self.assertEqual(filter.array, before | filter.hash1("9012345678") | filter.hash2("9012345678"))

    def test_is_value(self):
        filter = BloomFilter(32)
        filter.add("0123456789")
        # filter.add("1234567890")
        filter.add("2345678901")
        # filter.add("3456789012")
        # filter.add("4567890123")
        # filter.add("5678901234")
        # filter.add("6789012345")
        # filter.add("7890123456")
        # filter.add("8901234567")
        # filter.add("9012345678")
        self.assertTrue(filter.is_value("0123456789"))
        self.assertTrue(filter.is_value("2345678901"))

        self.assertFalse(filter.is_value("1234567890"))
        self.assertFalse(filter.is_value("3456789012"))
        self.assertFalse(filter.is_value("7890123456"))

        filter = BloomFilter(32)
        filter.add("0123456789")
        # filter.add("1234567890")
        filter.add("2345678901")
        filter.add("3456789012")
        filter.add("4567890123")
        filter.add("5678901234")
        filter.add("6789012345")
        filter.add("7890123456")
        filter.add("8901234567")
        # filter.add("9012345678")
        self.assertTrue(filter.is_value("0123456789"))
        # self.assertTrue(filter.is_value("1234567890"))
        self.assertTrue(filter.is_value("2345678901"))
        self.assertTrue(filter.is_value("3456789012"))
        self.assertTrue(filter.is_value("4567890123"))
        self.assertTrue(filter.is_value("5678901234"))
        self.assertTrue(filter.is_value("5678901234"))
        self.assertTrue(filter.is_value("6789012345"))
        self.assertTrue(filter.is_value("7890123456"))
        self.assertTrue(filter.is_value("8901234567"))
        # self.assertTrue(filter.is_value("9012345678"))
