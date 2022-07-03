class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_in_tail(self, item):
        if not isinstance(item, Node):
            return None
        self.size += 1
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

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
        if self.size != 0:
            last_node = self.head
            if last_node.value == val:
                if self.size == 1:
                    self.clean()
                    return None
                else:
                    self.head = last_node.next
                    self.size -= 1
                    if not all:
                        return None
                    else:
                        return self.delete(val, all)
            node = last_node.next
            while node is not None:
                if node.value == val:
                    if node == self.tail:
                        self.tail = last_node
                        last_node.next = None
                    else:
                        last_node.next = node.next
                    self.size -= 1
                    if not all:
                        return None
                    else:
                        return self.delete(val, all)
                last_node = node
                node = node.next

    def clean(self):
        self.head = None
        self.tail = None
        self.size = 0

    def len(self):
        return self.size

    def insert(self, afterNode, newNode):
        if not isinstance(newNode, Node):
            return None
        if newNode is not None:
            if afterNode is not None:
                newNode.next = afterNode.next
                afterNode.next = newNode
                if afterNode == self.tail:
                    self.tail = newNode
            else:
                newNode.next = self.head
                self.head = newNode
                if self.size == 0:
                    self.tail = newNode
            self.size += 1

    def equals(self, another):
        if self.size != another.size:
            return False
        if self.size == 0 and another.size == 0:
            return True
        if self.head.value != another.head.value:
            return False
        if self.tail.value != another.tail.value:
            return False
        a_node = self.head
        b_node = another.head
        while a_node is not None and b_node is not None:
            if a_node.value != b_node.value:
                return False
            a_node = a_node.next
            b_node = b_node.next
        return True

    @staticmethod
    def sum_list(a_list, b_list):
        if a_list.len() != b_list.len():
            return None
        result = LinkedList()
        a_node = a_list.head
        b_node = b_list.head
        while a_node is not None:
            result.add_in_tail(Node(a_node.value + b_node.value))
            a_node = a_node.next
            b_node = b_node.next
        return result
