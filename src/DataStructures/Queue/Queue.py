class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, item):
        newNode = Node(item)
        self.length += 1
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode

    def dequeue(self):
        if self.size() == 0:
            return None
        result = self.head.value
        if self.size() == 1:
            self.tail = None
        self.head = self.head.next
        self.length -= 1
        return result

    def size(self):
        return self.length

    def rotate(self, count):
        for i in range(count % self.size()):
            self.enqueue(self.dequeue())
