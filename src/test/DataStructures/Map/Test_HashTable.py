import unittest

from src.DataStructures.Map.HashTable import HashTable


class TestHashTable(unittest.TestCase):
    def test___init__(self):
        table = HashTable(17, 3)

    def test_hash_fun(self):
        table = HashTable(17, 3)
        self.assertTrue(table.hash_fun("aaa") < table.size)
        self.assertTrue(table.hash_fun("aaaagadgadgadgadfgergerge43534525") < table.size)
        self.assertTrue(table.hash_fun("aaaagadgasdgfdg4dgadgadfgergerge43534525") < table.size)
        self.assertTrue(table.hash_fun("534525") < table.size)
        self.assertTrue(table.hash_fun("z") < table.size)
        self.assertTrue(table.hash_fun("b") < table.size)
        # collision
        # print(table.hash_fun("z"))
        # print(table.hash_fun("434525"))

    def test_seek_slot(self):
        table = HashTable(7, 3)
        table.slots[0] = "a"
        table.slots[1] = "a"
        table.slots[2] = "a"
        table.slots[3] = "a"
        # table.slots[4] = "a"
        table.slots[5] = "a"
        table.slots[6] = "a"
        self.assertEqual(table.seek_slot("b"), 4)
        table.slots[4] = "a"
        self.assertEqual(table.seek_slot("b"), None)

        table = HashTable(9, 3)
        table.slots[0] = "a"
        # table.slots[1] = "a"
        table.slots[2] = "a"
        table.slots[3] = "a"
        table.slots[4] = "a"
        table.slots[5] = "a"
        table.slots[6] = "a"
        table.slots[7] = "a"
        table.slots[8] = "a"
        self.assertEqual(table.seek_slot("b"), 1)

    def test_put(self):
        table = HashTable(7, 3)
        for c in "abcdefz":
            self.assertIsNotNone(table.put(c))

        self.assertIsNone(table.put("safasf"))

    def test_find(self):
        table = HashTable(7, 3)
        for c in "abcdefz":
            table.put(c)

        self.assertIsNotNone(table.find("z"))
        self.assertIsNone(table.find("zzz"))
