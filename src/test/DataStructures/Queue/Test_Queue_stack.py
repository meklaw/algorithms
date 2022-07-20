import unittest

from src.DataStructures.Queue.Queue_stack import Queue


class TestQueueStack(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(5)
        queue.enqueue(10)
        self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(25)
        self.assertEqual(queue.dequeue(), 5)
        queue.enqueue(50)
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), 25)
        self.assertEqual(queue.dequeue(), 50)


    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(5)
        queue.enqueue(10)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), None)

    def test_size(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(5)
        queue.enqueue(10)
        self.assertEqual(queue.size(), 3)
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        self.assertEqual(queue.size(), 0)

    def test_rotate(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(5)
        queue.enqueue(10)
        queue.enqueue(25)
        queue.enqueue(50)
        queue.rotate(5)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), 25)
        self.assertEqual(queue.dequeue(), 50)

        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(5)
        queue.enqueue(10)
        queue.enqueue(25)
        queue.enqueue(50)
        queue.rotate(3)
        self.assertEqual(queue.dequeue(), 25)
        self.assertEqual(queue.dequeue(), 50)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(queue.dequeue(), 10)

        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(5)
        queue.enqueue(10)
        queue.enqueue(25)
        queue.enqueue(50)
        queue.rotate(8)
        self.assertEqual(queue.dequeue(), 25)
        self.assertEqual(queue.dequeue(), 50)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(queue.dequeue(), 10)


