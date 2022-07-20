import unittest

from src.DataStructures.Stack.Stack_head import Stack


class TestStackHead(unittest.TestCase):
    def test_push(self):
        test_stack = Stack()
        test_stack.push(1)
        test_stack.push(5)
        test_stack.push(10)
        self.assertEqual(test_stack.size(), 3)
        self.assertEqual(test_stack.head.value, 10)
        self.assertEqual(test_stack.head.next.value, 5)
        self.assertEqual(test_stack.head.next.next.value, 1)

    def test_pop(self):
        test_stack = Stack()
        test_stack.push(1)
        test_stack.push(5)
        test_stack.push(10)
        self.assertEqual(test_stack.size(), 3)
        self.assertEqual(test_stack.pop(), 10)
        self.assertEqual(test_stack.head.value, 5)
        self.assertEqual(test_stack.head.next.value, 1)

        self.assertEqual(test_stack.size(), 2)
        self.assertEqual(test_stack.pop(), 5)
        self.assertEqual(test_stack.head.value, 1)

        self.assertEqual(test_stack.size(), 1)
        self.assertEqual(test_stack.pop(), 1)
        self.assertIsNone(test_stack.head)
        self.assertIsNone(test_stack.tail)
        self.assertEqual(test_stack.size(), 0)

    def test_peek(self):
        test_stack = Stack()
        test_stack.push(1)
        self.assertEqual(test_stack.peek(), 1)
        test_stack.push(5)
        self.assertEqual(test_stack.peek(), 5)
        test_stack.push(10)
        self.assertEqual(test_stack.peek(), 10)

    def test_check_parenthesis(self):
        self.assertFalse(Stack.check_parenthesis("())("))
        self.assertFalse(Stack.check_parenthesis("))(("))
        self.assertFalse(Stack.check_parenthesis("((())"))
        self.assertFalse(Stack.check_parenthesis("())))"))
        self.assertFalse(Stack.check_parenthesis("((("))
        self.assertTrue(Stack.check_parenthesis("((()))"))

    def test_postfix_calc(self):
        test_stack = Stack()
        test_stack.push('=')
        test_stack.push('+')
        test_stack.push('9')
        test_stack.push('*')
        test_stack.push('5')
        test_stack.push('+')
        test_stack.push('2')
        test_stack.push('8')
        self.assertEqual(Stack.postfix_calc(test_stack), 59)

        test_stack = Stack()
        test_stack.push('-')
        test_stack.push('2')
        test_stack.push('8')
        self.assertEqual(Stack.postfix_calc(test_stack), 6)

        test_stack = Stack()
        test_stack.push('/')
        test_stack.push('2')
        test_stack.push('8')
        self.assertEqual(Stack.postfix_calc(test_stack), 4)
