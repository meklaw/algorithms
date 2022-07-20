import unittest

from src.DataStructures.Map.NativeDictionary import NativeDictionary


class TestNativeDictionary(unittest.TestCase):

    def test_hash_fun(self):
        table = NativeDictionary(17)
        self.assertTrue(table.hash_fun("aaa") < table.size)
        self.assertTrue(table.hash_fun("aaaagadgadgadgadfgergerge43534525") < table.size)
        self.assertTrue(table.hash_fun("aaaagadgasdgfdg4dgadgadfgergerge43534525") < table.size)
        self.assertTrue(table.hash_fun("534525") < table.size)
        self.assertTrue(table.hash_fun("z") < table.size)
        self.assertTrue(table.hash_fun("b") < table.size)
        # collision
        # print(table.hash_fun("z"))
        # print(table.hash_fun("434525"))

    def test_is_key(self):
        table = NativeDictionary(3)
        table.slots[0] = "a"
        table.values[0] = "aaaaa"
        # table.slots[1] = "b"
        # table.values[1] = "bbbbb"
        table.slots[2] = "c"
        table.values[2] = "ccccc"
        self.assertTrue(table.is_key("a"))
        self.assertFalse(table.is_key("b"))

    def test_put(self):
        table = NativeDictionary(3)
        table.put("a", "aaa")
        table.put("b", "bbb")
        table.put("c", "ccc")
        self.assertTrue(table.is_key("a"))
        self.assertTrue(table.is_key("b"))
        self.assertTrue(table.is_key("c"))
        self.assertEqual(table.put("a", "z"), None)

    def test_get(self):
        table = NativeDictionary(3)
        table.put("a", "aaa")
        table.put("b", "bbb")
        table.put("c", "ccc")
        self.assertEqual(table.get("a"), "aaa")
        self.assertEqual(table.get("b"), "bbb")
        self.assertEqual(table.get("c"), "ccc")

        table.put("a", "abba")
        self.assertEqual(table.get("a"), "abba")
        self.assertEqual(table.get("z"), None)
