import unittest

from src.DataStructures.List.LinkedList_dummy_node import Node, LinkedList2, DummyNode


class TestLinkedList2DummyNode(unittest.TestCase):

    def test_add_in_tail(self):
        test_list = LinkedList2()
        test_list.add_in_tail(Node(10))
        test_list.add_in_tail(Node(20))
        test_list.add_in_tail(Node(30))
        self.assertEqual(test_list.head.next.value, 10)
        self.assertEqual(test_list.head.next.next.value, 20)
        self.assertEqual(test_list.head.next.next.next.value, 30)
        self.assertEqual(test_list.tail.prev.value, 30)
        self.assertEqual(test_list.tail.prev.prev.value, 20)
        self.assertEqual(test_list.tail.prev.prev.prev.value, 10)

    def test_find(self):
        test_list = LinkedList2()
        a_node = Node(5)
        b_node = Node(5)
        test_list.add_in_tail(Node(11))
        test_list.add_in_tail(a_node)
        test_list.add_in_tail(Node(10))
        test_list.add_in_tail(b_node)
        self.assertEqual(test_list.find(5), a_node)
        self.assertNotEqual(test_list.find(5), b_node)

    def test_find_all(self):
        test_list = LinkedList2()
        a_node = Node(5)
        b_node = Node(5)
        test_list.add_in_tail(Node(11230))
        test_list.add_in_tail(a_node)
        test_list.add_in_tail(Node(10))
        test_list.add_in_tail(b_node)
        self.assertEqual(test_list.find_all(5)[0], a_node)
        self.assertEqual(test_list.find_all(5)[1], b_node)
        self.assertEqual(test_list.find_all(5).__len__(), 2)

        test_list = LinkedList2()
        test_list.add_in_tail(Node(11230))
        test_list.add_in_tail(Node(3))
        test_list.add_in_tail(Node(10))
        self.assertEqual(test_list.find_all(5).__len__(), 0)
        self.assertEqual(test_list.find_all(5), [])

    def test_delete(self):
        test_list = LinkedList2()
        a_node = Node(10)
        b_node = Node(20)
        c_node = Node(30)
        test_list.add_in_tail(a_node)
        test_list.add_in_tail(b_node)
        test_list.add_in_tail(c_node)
        test_list.delete(b_node.value)
        self.assertEqual(test_list.head.next, a_node)
        self.assertEqual(a_node.next, c_node)
        self.assertEqual(a_node.prev.value, None)
        self.assertEqual(c_node.prev, a_node)
        self.assertEqual(c_node.next.value, None)
        self.assertEqual(test_list.tail.prev, c_node)
        self.assertEqual(test_list.len(), 2)

        test_list = LinkedList2()
        a_node = Node(10)
        test_list.add_in_tail(a_node)
        test_list.delete(a_node.value)
        self.assertIsNone(test_list.head.value)
        self.assertIsNone(test_list.head.next.value)
        self.assertIsNone(test_list.tail.value)
        self.assertIsNone(test_list.tail.prev.value)
        self.assertEqual(test_list.len(), 0)

        test_list = LinkedList2()
        a_node = Node(10)
        b_node = Node(20)
        test_list.add_in_tail(a_node)
        test_list.add_in_tail(b_node)
        test_list.delete(a_node.value)
        self.assertEqual(test_list.head.next, b_node)
        self.assertEqual(test_list.tail.prev, b_node)
        self.assertIsNone(b_node.next.value)
        self.assertIsNone(b_node.prev.value)

        test_list = LinkedList2()
        a_node = Node(10)
        b_node = Node(20)
        test_list.add_in_tail(a_node)
        test_list.add_in_tail(b_node)
        test_list.delete(b_node.value)
        self.assertEqual(test_list.head.next, a_node)
        self.assertEqual(test_list.tail.prev, a_node)
        self.assertIsNone(a_node.next.value)
        self.assertIsNone(a_node.prev.value)

        test_list = LinkedList2()
        test_list.add_in_tail(Node(10))
        test_list.add_in_tail(Node(10))
        test_list.add_in_tail(Node(20))
        test_list.add_in_tail(Node(10))
        test_list.add_in_tail(Node(10))
        test_list.delete(10, True)
        self.assertEqual(test_list.head.next.value, 20)
        self.assertEqual(test_list.tail.prev.value, 20)
        self.assertIsNone(test_list.head.next.next.value)
        self.assertIsNone(test_list.head.prev)
        self.assertEqual(test_list.len(), 1)

        test_list = LinkedList2()
        test_list.add_in_tail(Node(10))
        test_list.add_in_tail(Node(10))
        test_list.add_in_tail(Node(10))
        test_list.add_in_tail(Node(10))
        test_list.delete(10, True)
        self.assertIsNone(test_list.head.next.value)
        self.assertIsNone(test_list.tail.prev.value)
        self.assertEqual(test_list.len(), 0)

    def test_clean(self):
        test_list = LinkedList2()
        list = test_list
        test_list.add_in_tail(Node(10))
        test_list.add_in_tail(Node(20))
        test_list.add_in_tail(Node(30))
        test_list.clean()
        self.assertIsNone(test_list.head.value)
        self.assertIsNone(test_list.head.next.value)
        self.assertIsNone(test_list.tail.value)
        self.assertIsNone(test_list.tail.prev.value)
        self.assertEqual(test_list.len(), 0)
        self.assertEqual(test_list, list)

    def test_len(self):
        test_list = LinkedList2()
        test_list.add_in_tail(Node(11230))
        test_list.add_in_tail(Node(10))
        test_list.add_in_tail(Node(10))
        test_list.add_in_tail(Node(12))
        test_list.delete(10)
        test_list.delete(0)
        self.assertEqual(test_list.len(), 3)

    def test_insert(self):
        test_list = LinkedList2()
        a_node = Node(10)
        test_list.insert(None, a_node)
        self.assertEqual(test_list.head.next.value, 10)
        self.assertEqual(test_list.tail.prev.value, 10)
        self.assertIsNone(test_list.head.next.next.value)
        self.assertIsNone(test_list.head.next.next.next)
        self.assertIsNone(test_list.head.prev)
        self.assertIsNone(test_list.tail.next)
        b_node = Node(20)
        test_list.insert(None, b_node)
        self.assertEqual(test_list.head.next.value, 10)
        self.assertEqual(test_list.head.next.next.value, 20)
        self.assertEqual(test_list.tail.prev.value, 20)
        self.assertEqual(test_list.tail.prev.prev.value, 10)
        c_node = Node(30)
        test_list.insert(a_node, c_node)
        self.assertEqual(test_list.head.next.value, 10)
        self.assertEqual(test_list.head.next.next.value, 30)
        self.assertEqual(test_list.head.next.next.next.value, 20)
        self.assertEqual(test_list.tail.prev.value, 20)
        self.assertEqual(test_list.tail.prev.prev.value, 30)
        self.assertEqual(test_list.tail.prev.prev.prev.value, 10)
        test_list.insert(b_node, Node(100))
        test_list.insert(b_node, 33)
        test_list.insert(b_node, None)
        test_list.insert(b_node, DummyNode())
        self.assertEqual(test_list.tail.prev.value, 100)
        self.assertEqual(test_list.tail.prev.prev.value, 20)
        self.assertEqual(test_list.tail.prev.prev.prev.value, 30)
        self.assertEqual(test_list.tail.prev.prev.prev.prev.value, 10)
        self.assertEqual(test_list.head.next.value, 10)
        self.assertEqual(test_list.head.next.next.value, 30)
        self.assertEqual(test_list.head.next.next.next.value, 20)
        self.assertEqual(test_list.head.next.next.next.next.value, 100)
        self.assertEqual(test_list.len(), 4)

    def test_add_in_head(self):
        test_list = LinkedList2()
        test_list.add_in_head(Node(10))
        self.assertEqual(test_list.head.next.value, 10)
        self.assertEqual(test_list.tail.prev.value, 10)
        self.assertIsNone(test_list.head.next.next.value)
        self.assertIsNone(test_list.tail.prev.prev.value)
        test_list.add_in_head(Node(20))
        self.assertEqual(test_list.head.next.value, 20)
        self.assertEqual(test_list.head.next.next.value, 10)
        self.assertEqual(test_list.tail.prev.value, 10)
        self.assertEqual(test_list.tail.prev.prev.value, 20)
        test_list.add_in_head(Node(30))
        self.assertEqual(test_list.head.next.value, 30)
        self.assertEqual(test_list.head.next.next.value, 20)
        self.assertEqual(test_list.head.next.next.next.value, 10)
        self.assertEqual(test_list.tail.prev.value, 10)
        self.assertEqual(test_list.tail.prev.prev.value, 20)
        self.assertEqual(test_list.tail.prev.prev.prev.value, 30)