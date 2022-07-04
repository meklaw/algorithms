class Node:
    def __init__(self, v=None):
        self.value = v
        self.prev = None
        self.next = None


class DummyNode(Node):
    def __int__(self):
        Node.__init__(self, None)


class LinkedList2:

    def __init__(self):
        self.size = 0
        self.head = DummyNode()
        self.tail = DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_tail(self, newNode):
        if not isinstance(newNode, Node) or isinstance(newNode, DummyNode):
            return
        self.size += 1
        newNode.next = self.tail
        newNode.prev = self.tail.prev
        newNode.prev.next = newNode
        self.tail.prev = newNode

    def find(self, val):
        node = self.head.next
        while node is not None:
            if node.value == val and not isinstance(node, DummyNode):
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head.next
        while node is not None:
            if node.value == val and not isinstance(node, DummyNode):
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        if self.len() == 0:
            return
        node = self.head.next
        while node is not None:
            if node.value == val and not isinstance(node, DummyNode):
                node.prev.next = node.next
                node.next.prev = node.prev
                self.size -= 1
                if not all:
                    return
            node = node.next

    def clean(self):
        self.__init__()

    def len(self):
        return self.size

    def insert(self, afterNode, newNode):
        if newNode is None or not isinstance(newNode, Node) or isinstance(newNode, DummyNode):
            return
        if afterNode is None or afterNode == self.tail.prev:
            self.add_in_tail(newNode)
            return
        newNode.next = afterNode.next
        newNode.prev = afterNode
        newNode.next.prev = newNode
        afterNode.next = newNode
        self.size += 1

    def add_in_head(self, newNode):
        if not isinstance(newNode, Node) or isinstance(newNode, DummyNode):
            return
        self.size += 1
        newNode.next = self.head.next
        newNode.prev = self.head
        newNode.next.prev = newNode
        self.head.next = newNode
