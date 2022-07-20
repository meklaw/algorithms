class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_in_tail(self, item):
        if not isinstance(item, Node):
            return
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
        current_node = self.head
        while current_node is not None:
            if current_node.value == val:
                self.__delete_node(current_node)
                if not all:
                    return
            current_node = current_node.next

    def __delete_node(self, node: Node):
        if self.len() == 1:
            self.clean()
            return
        self.size -= 1
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
            return
        if node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            return
        node.next.prev = node.prev
        node.prev.next = node.next

    def clean(self):
        self.__init__()

    def len(self):
        return self.size

    def insert(self, afterNode, newNode):
        if newNode is None or not isinstance(newNode, Node):
            return
        if afterNode is None or afterNode == self.tail:
            self.add_in_tail(newNode)
            return
        newNode.next = afterNode.next
        newNode.prev = afterNode
        newNode.next.prev = newNode
        afterNode.next = newNode
        self.size += 1

    def add_in_head(self, newNode):
        if not isinstance(newNode, Node):
            return
        self.size += 1
        if self.tail is None:
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
        self.head = newNode
