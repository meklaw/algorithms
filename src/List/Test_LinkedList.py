import unittest

from src.List.LinkedList import Node, LinkedList


class TestLinkedList(unittest.TestCase):
    def test_delete(self):
        correct_list = LinkedList()
        correct_list.add_in_tail(Node(-5))
        correct_list.add_in_tail(Node(0))

        test_list = LinkedList()
        test_list.add_in_tail(Node(-5))
        test_list.add_in_tail(Node(0))
        test_list.add_in_tail(Node(128))
        test_list.delete(128)

        self.assertTrue(correct_list.equals(test_list))
        self.assertEqual(test_list.len(), 2)

        correct_list = LinkedList()

        test_list = LinkedList()
        test_list.add_in_tail(Node(0))
        test_list.delete(0)

        self.assertTrue(correct_list.equals(test_list))
        self.assertEqual(test_list.len(), 0)

        correct_list = LinkedList()
        correct_list.add_in_tail(Node(0))

        test_list = LinkedList()
        test_list.add_in_tail(Node(0))
        test_list.add_in_tail(Node(1))
        test_list.delete(1)

        self.assertIsNotNone(test_list.head)
        self.assertIsNotNone(test_list.tail)
        self.assertTrue(correct_list.equals(test_list))
        self.assertEqual(test_list.len(), 1)

        correct_list = LinkedList()
        correct_list.add_in_tail(Node(0))
        correct_list.add_in_tail(Node(10))

        test_list = LinkedList()
        test_list.add_in_tail(Node(0))
        test_list.add_in_tail(Node(5))
        test_list.add_in_tail(Node(10))
        test_list.delete(5)

        self.assertTrue(correct_list.equals(test_list))

        correct_list = LinkedList()
        correct_list.add_in_tail(Node(0))

        test_list = LinkedList()
        test_list.add_in_tail(Node(0))
        test_list.add_in_tail(Node(0))
        test_list.delete(0)

        self.assertTrue(correct_list.equals(test_list))

        correct_list = LinkedList()
        correct_list.add_in_tail(Node(1))

        test_list = LinkedList()
        test_list.add_in_tail(Node(0))
        test_list.add_in_tail(Node(1))
        test_list.add_in_tail(Node(0))
        test_list.add_in_tail(Node(0))
        test_list.add_in_tail(Node(0))
        test_list.delete(0, True)

        self.assertTrue(correct_list.equals(test_list))

    def test_clean(self):
        correct_list = LinkedList()

        test_list = LinkedList()
        test_list.add_in_tail(Node(0))
        test_list.add_in_tail(Node(5))
        test_list.add_in_tail(Node(0))
        test_list.clean()

        self.assertTrue(correct_list.equals(test_list))

    def test_find_all(self):
        a = Node(0)
        b = Node(5)
        c = Node(0)

        test_list = LinkedList()
        test_list.add_in_tail(a)
        test_list.add_in_tail(b)
        test_list.add_in_tail(c)

        self.assertEqual(test_list.find_all(0), [a, c])
        self.assertEqual(test_list.find_all(0)[0], a)
        self.assertEqual(test_list.find_all(0)[1], c)

    def test_len(self):
        test_list = LinkedList()
        test_list.add_in_tail(Node(1))
        test_list.add_in_tail(Node(5))
        test_list.delete(1)
        test_list.insert(test_list.find(5), Node(8))
        self.assertEqual(test_list.len(), 2)

    def test_insert(self):
        test_list = LinkedList()
        test_list.add_in_tail(Node(1))
        test_list.add_in_tail(Node(5))
        test_list.add_in_tail(Node(10))
        test_list.insert(test_list.find(5), Node(8))

        correct_list = LinkedList()
        correct_list.add_in_tail(Node(1))
        correct_list.add_in_tail(Node(5))
        correct_list.add_in_tail(Node(8))
        correct_list.add_in_tail(Node(10))
        self.assertTrue(correct_list.equals(test_list))

        node = Node(5)
        test_list = LinkedList()
        test_list.insert(None, node)
        self.assertEqual(test_list.head, node)
        self.assertEqual(test_list.tail, node)
        self.assertEqual(test_list.len(), 1)

        node1 = Node(5)
        node2 = Node(7)
        test_list = LinkedList()
        test_list.insert(None, node2)
        test_list.insert(None, node1)
        self.assertEqual(test_list.head, node1)
        self.assertEqual(test_list.tail, node2)
        self.assertEqual(test_list.len(), 2)

        node = Node(5)
        test_list = LinkedList()
        test_list.add_in_tail(Node(1))
        test_list.insert(test_list.find(1), node)
        self.assertEqual(test_list.head.value, 1)
        self.assertEqual(test_list.tail.value, 5)

        node = Node(5)
        test_list = LinkedList()
        test_list.add_in_tail(Node(1))
        test_list.add_in_tail(Node(10))
        test_list.insert(test_list.find(1), node)
        self.assertEqual(test_list.head.value, 1)
        self.assertEqual(test_list.tail.value, 10)

        node = Node(5)
        test_list = LinkedList()
        test_list.add_in_tail(Node(1))
        test_list.insert(None, node)
        self.assertEqual(test_list.head.value, 5)
        self.assertEqual(test_list.tail.value, 1)

        node = Node(5)
        test_list = LinkedList()
        test_list.insert(None, node)
        self.assertEqual(test_list.head.value, 5)
        self.assertEqual(test_list.tail.value, 5)

    def test_equals(self):
        test_list = LinkedList()
        test_list.add_in_tail(Node(1))
        test_list.add_in_tail(Node(5))
        test_list.add_in_tail(Node(10))

        correct_list = LinkedList()
        correct_list.add_in_tail(Node(1))
        correct_list.add_in_tail(Node(5))
        correct_list.add_in_tail(Node(10))
        self.assertTrue(correct_list.equals(test_list))

        test_list = LinkedList()

        correct_list = LinkedList()
        self.assertTrue(correct_list.equals(test_list))

        test_list = LinkedList()
        test_list.add_in_tail(Node(5))

        correct_list = LinkedList()
        self.assertFalse(correct_list.equals(test_list))

    def test_sum_list(self):
        test_list = LinkedList()
        test_list.add_in_tail(Node(1))

        correct_list = LinkedList()
        self.assertIsNone(LinkedList.sum_list(test_list, correct_list))

        test_list = LinkedList()

        correct_list = LinkedList()
        self.assertIsNotNone(LinkedList.sum_list(test_list, correct_list))

        test_list = LinkedList()
        test_list.add_in_tail(Node(15))

        correct_list = LinkedList()
        correct_list.add_in_tail(Node(30))
        self.assertEqual(LinkedList.sum_list(test_list, correct_list).head.value, 45)
        self.assertEqual(LinkedList.sum_list(test_list, correct_list).tail.value, 45)
        self.assertEqual(LinkedList.sum_list(test_list, correct_list).len(), 1)

        test_list = LinkedList()
        test_list.add_in_tail(Node(15))
        test_list.add_in_tail(Node(20))
        test_list.add_in_tail(Node(-100))

        correct_list = LinkedList()
        correct_list.add_in_tail(Node(30))
        correct_list.add_in_tail(Node(60))
        correct_list.add_in_tail(Node(80))
        self.assertEqual(LinkedList.sum_list(test_list, correct_list).head.value, 45)
        self.assertEqual(LinkedList.sum_list(test_list, correct_list).head.next.value, 80)
        self.assertEqual(LinkedList.sum_list(test_list, correct_list).tail.value, -20)
        self.assertEqual(LinkedList.sum_list(test_list, correct_list).len(), 3)
