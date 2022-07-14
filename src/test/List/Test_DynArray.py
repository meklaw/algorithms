import unittest

from src.List.DynArray import DynArray


class TestDynArray(unittest.TestCase):

    def test_insert(self):
        list = DynArray()
        list.append(10)
        list.append(20)
        list.append(30)
        list.insert(0, 5)
        list.insert(2, 15)
        self.assertEqual(list.__len__(), 5)
        self.assertEqual(list.capacity, 16)
        self.assertEqual(list.__getitem__(0), 5)
        self.assertEqual(list.__getitem__(1), 10)
        self.assertEqual(list.__getitem__(2), 15)
        self.assertEqual(list.__getitem__(3), 20)
        self.assertEqual(list.__getitem__(4), 30)
        self.assertRaises(IndexError, list.insert, 8, 1000)

        list = DynArray()
        for i in range(16):
            list.append(i)
        self.assertEqual(list.__len__(), 16)
        list.insert(16, 20)
        self.assertEqual(list.__getitem__(15), 15)
        self.assertEqual(list.__getitem__(16), 20)
        self.assertEqual(list.capacity, 32)
        self.assertEqual(list.__len__(), 17)

        list.insert(16, 10)
        self.assertEqual(list.__getitem__(16), 10)
        self.assertEqual(list.__getitem__(17), 20)
        self.assertEqual(list.__len__(), 18)
        self.assertEqual(list.capacity, 32)

        # недоступные позиции
        self.assertRaises(IndexError, list.insert, -2, 2)
        self.assertRaises(IndexError, list.insert, 30, 2)
        self.assertEqual(list.__len__(), 18)

    def test_delete(self):
        list = DynArray()
        list.append(5)
        list.delete(0)
        self.assertEqual(list.__len__(), 0)
        self.assertEqual(list.array[0], None)
        self.assertEqual(list.array[0], None)
        self.assertRaises(IndexError, list.__getitem__, 0)

        list = DynArray()
        list.append(5)
        list.append(10)
        list.append(15)
        list.delete(1)
        self.assertEqual(list.__len__(), 2)
        self.assertEqual(list.__getitem__(0), 5)
        self.assertEqual(list.__getitem__(1), 15)
        self.assertRaises(IndexError, list.delete, 100)
        self.assertRaises(IndexError, list.delete, list.__len__())
        self.assertRaises(IndexError, list.delete, -2)

        list = DynArray()
        for i in range(16):
            list.append(i)
        list.delete(15)
        self.assertEqual(list.__len__(), 15)
        self.assertEqual(list.__getitem__(14), 14)
        self.assertRaises(IndexError, list.__getitem__, 15)


        list = DynArray()
        for i in range(40):
            list.append(i)
        self.assertEqual(list.capacity, 64)
        for i in range(32, 40):
            list.delete(32)
        self.assertEqual(list.__len__(), 32)
        self.assertEqual(list.capacity, 64)
        list.delete(31)
        self.assertEqual(list.capacity, 42)
        for i in range(11):
            list.delete(0)
        for i in range(6):
            list.delete(0)
        self.assertEqual(list.__len__(), 14)
        self.assertEqual(list.capacity, 28)
        list.delete(0)
        self.assertEqual(list.__len__(), 13)
        self.assertEqual(list.capacity, 18)
        for i in range(5):
            list.delete(0)
        self.assertEqual(list.__len__(), 8)
        self.assertEqual(list.capacity, 16)