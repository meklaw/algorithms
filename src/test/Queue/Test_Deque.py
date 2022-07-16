import unittest

from src.Queue.Deque import Deque


class TestDeque(unittest.TestCase):
    def test_addFront(self):
        deque = Deque()
        deque.addFront(1)
        self.assertEqual(deque.size(), 1)
        self.assertEqual(deque.deque[0], 1)
        deque.addFront(5)
        self.assertEqual(deque.size(), 2)
        self.assertEqual(deque.deque[0], 5)
        self.assertEqual(deque.deque[1], 1)
        deque.addFront(10)
        self.assertEqual(deque.size(), 3)
        self.assertEqual(deque.deque[0], 10)
        self.assertEqual(deque.deque[1], 5)
        self.assertEqual(deque.deque[2], 1)

    def test_addTail(self):
        deque = Deque()
        deque.addTail(1)
        self.assertEqual(deque.size(), 1)
        self.assertEqual(deque.deque[0], 1)
        deque.addTail(5)
        self.assertEqual(deque.size(), 2)
        self.assertEqual(deque.deque[0], 1)
        self.assertEqual(deque.deque[1], 5)
        deque.addTail(10)
        self.assertEqual(deque.size(), 3)
        self.assertEqual(deque.deque[0], 1)
        self.assertEqual(deque.deque[1], 5)
        self.assertEqual(deque.deque[2], 10)

    def test_removeFront(self):
        deque = Deque()
        deque.addTail(1)
        deque.addTail(5)
        deque.addTail(10)
        self.assertEqual(deque.size(), 3)
        self.assertEqual(deque.removeFront(), 1)
        self.assertEqual(deque.size(), 2)
        self.assertEqual(deque.removeFront(), 5)
        self.assertEqual(deque.size(), 1)
        self.assertEqual(deque.removeFront(), 10)
        self.assertEqual(deque.size(), 0)
        self.assertEqual(deque.removeFront(), None)
        self.assertEqual(deque.size(), 0)

    def test_removeTail(self):
        deque = Deque()
        deque.addTail(1)
        deque.addTail(5)
        deque.addTail(10)
        self.assertEqual(deque.size(), 3)
        self.assertEqual(deque.removeTail(), 10)
        self.assertEqual(deque.size(), 2)
        self.assertEqual(deque.removeTail(), 5)
        self.assertEqual(deque.size(), 1)
        self.assertEqual(deque.removeTail(), 1)
        self.assertEqual(deque.size(), 0)
        self.assertEqual(deque.removeTail(), None)
        self.assertEqual(deque.size(), 0)
