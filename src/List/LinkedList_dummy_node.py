class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    size = 0

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_tail(self, newNode):
        self.size += 1
        newNode.next = self.tail
        newNode.prev = self.tail.prev
        newNode.prev.next = newNode
        self.tail.prev = newNode

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        if self.len() != 0:
            node = self.head
            while node is not None:
                if node.value == val:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    self.size -= 1
                    if not all:
                        return None
                node = node.next

    def clean(self):
        self.size = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self):
        return self.size

    def insert(self, afterNode, newNode):
        if newNode is None:
            return None
        if afterNode is None or afterNode == self.tail.prev:
            return self.add_in_tail(newNode)
        newNode.next = afterNode.next
        newNode.prev = afterNode
        newNode.next.prev = newNode
        afterNode.next = newNode
        self.size += 1

    def add_in_head(self, newNode):
        self.size += 1
        newNode.next = self.head.next
        newNode.prev = self.head
        newNode.next.prev = newNode
        self.head.next = newNode
