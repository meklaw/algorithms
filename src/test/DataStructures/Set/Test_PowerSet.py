import unittest

from src.DataStructures.Set.PowerSet import PowerSet


class TestPowerSet(unittest.TestCase):
    def test_put(self):
        set = PowerSet()
        a = "123"
        set.put("123")
        set.put("123")
        self.assertEqual(set.slots[set.hash_fun(a)], "123")
        self.assertEqual(set.size(), 1)

    def test_get(self):
        set = PowerSet()
        a = "123"
        set.put("123")
        self.assertEqual(set.slots[set.hash_fun(a)], "123")
        self.assertTrue(set.get(a))
        self.assertFalse(set.get("gfadfg"))

    def test_remove(self):
        set = PowerSet()
        a = "123"
        set.put(a)
        self.assertEqual(set.slots[set.hash_fun(a)], a)
        self.assertEqual(set.size(), 1)
        self.assertTrue(set.remove(a))
        self.assertFalse(set.remove("gfadfg"))
        self.assertFalse(set.remove(a))
        self.assertEqual(set.size(), 0)

    def test_intersection(self):
        set1 = PowerSet()
        set2 = PowerSet()
        self.assertEqual(set1.intersection(set2).size(), 0)
        set1.put("123")
        set1.put("12345")
        res = set1.intersection(set2)
        self.assertEqual(res.size(), 0)
        self.assertFalse(res.get("123"))
        self.assertFalse(res.get("12345"))
        set2.put("123")
        set2.put("555")
        res = set1.intersection(set2)
        self.assertEqual(res.size(), 1)
        self.assertTrue(res.get("123"))
        self.assertFalse(res.get("12345"))
        self.assertFalse(res.get("555"))

    def test_union(self):
        set1 = PowerSet()
        set2 = PowerSet()
        self.assertEqual(set1.union(set2).size(), 0)
        set1.put("123")
        set1.put("12345")
        res = set1.union(set2)
        self.assertEqual(res.size(), 2)
        self.assertTrue(res.get("123"))
        self.assertTrue(res.get("12345"))
        set2.put("123")
        set2.put("555")
        res = set1.union(set2)
        self.assertEqual(res.size(), 3)
        self.assertTrue(res.get("123"))
        self.assertTrue(res.get("12345"))
        self.assertTrue(res.get("555"))

    def test_difference(self):
        set1 = PowerSet()
        set2 = PowerSet()
        self.assertEqual(set1.difference(set2).size(), 0)
        set1.put("123")
        set1.put("12345")
        res = set1.difference(set2)
        self.assertEqual(res.size(), 2)
        self.assertTrue(res.get("123"))
        self.assertTrue(res.get("12345"))

        set1 = PowerSet()
        set1.put("123")
        set1.put("12345")

        set2 = PowerSet()
        set2.put("123")
        set2.put("555")

        res = set1.difference(set2)
        self.assertEqual(res.size(), 2)
        self.assertTrue(res.get("555"))
        self.assertTrue(res.get("12345"))
        self.assertFalse(res.get("123"))

    def test_issubset(self):
        set1 = PowerSet()
        set2 = PowerSet()
        set1.put("123")
        set1.put("12345")
        set2.put("123")
        self.assertEqual(set1.issubset(set2), True)

