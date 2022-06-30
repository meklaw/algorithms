class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    size = 0

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        self.size += 1
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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
                    if self.len() == 1:
                        self.clean()
                        return None
                    elif self.head == node:
                        self.head = node.next
                        self.head.prev = None
                    elif self.tail == node:
                        self.tail = node.prev
                        self.tail.next = None
                    else:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                    self.size -= 1
                    if not all:
                        return None
                node = node.next

    def clean(self):
        self.size = 0
        self.head = None
        self.tail = None

    def len(self):
        return self.size

    def insert(self, afterNode, newNode):
        if newNode is None:
            return None
        if afterNode is None or afterNode == self.tail:
            return self.add_in_tail(newNode)
        newNode.next = afterNode.next
        newNode.prev = afterNode
        newNode.next.prev = newNode
        afterNode.next = newNode
        self.size += 1

    def add_in_head(self, newNode):
        self.size += 1
        if self.tail is None:
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
        self.head = newNode
