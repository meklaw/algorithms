import unittest

from src.Stack.Stack_tail import Stack


class TestStackTail(unittest.TestCase):
    def test_push(self):
        test_stack = Stack()
        test_stack.push(1)
        test_stack.push(5)
        test_stack.push(10)
        self.assertEqual(test_stack.size(), 3)
        self.assertEqual(test_stack.head.next.value, 1)
        self.assertEqual(test_stack.head.next.next.value, 5)
        self.assertEqual(test_stack.head.next.next.next.value, 10)
        self.assertEqual(test_stack.tail.prev.value, 10)
        self.assertEqual(test_stack.tail.prev.prev.value, 5)
        self.assertEqual(test_stack.tail.prev.prev.prev.value, 1)

    def test_pop(self):
        test_stack = Stack()
        test_stack.push(1)
        test_stack.push(5)
        test_stack.push(10)
        self.assertEqual(test_stack.size(), 3)
        self.assertEqual(test_stack.pop(), 10)
        self.assertEqual(test_stack.head.next.value, 1)
        self.assertEqual(test_stack.head.next.next.value, 5)
        self.assertEqual(test_stack.tail.prev.value, 5)
        self.assertEqual(test_stack.tail.prev.prev.value, 1)

        self.assertEqual(test_stack.size(), 2)
        self.assertEqual(test_stack.pop(), 5)
        self.assertEqual(test_stack.head.next.value, 1)
        self.assertEqual(test_stack.tail.prev.value, 1)

        self.assertEqual(test_stack.size(), 1)
        self.assertEqual(test_stack.pop(), 1)
        self.assertEqual(test_stack.head.next, test_stack.tail)
        self.assertEqual(test_stack.tail.prev, test_stack.head)
        self.assertEqual(test_stack.size(), 0)

    def test_peek(self):
        test_stack = Stack()
        test_stack.push(1)
        self.assertEqual(test_stack.peek(), 1)
        test_stack.push(5)
        self.assertEqual(test_stack.peek(), 5)
        test_stack.push(10)
        self.assertEqual(test_stack.peek(), 10)
