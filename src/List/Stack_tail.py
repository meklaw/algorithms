class Node:
    def __init__(self, v=None):
        self.value = v
        self.prev = None
        self.next = None


class DummyNode(Node):
    def __int__(self):
        Node.__init__(self, None)


class Stack:
    def __init__(self):
        self.length = 0
        self.head = DummyNode()
        self.tail = DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def size(self):
        return self.length

    def pop(self):
        if self.size() == 0:
            return None
        result = self.tail.prev.value
        if self.size() == 1:
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev

        self.length -= 1
        return result

    def push(self, value):
        self.length += 1
        value = Node(value)
        value.next = self.tail
        value.prev = self.tail.prev
        value.prev.next = value
        self.tail.prev = value

    def peek(self):
        if self.size() == 0:
            return None
        return self.tail.prev.value
