class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class DummyNode(Node):
    def __init__(self):
        super().__init__(None)


class OrderedList:
    def __init__(self, asc: bool):
        self.head = DummyNode()
        self.tail = DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.__ascending = asc
        self.__size = 0

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0

        return 1

    def add(self, value):
        new_node = Node(value)
        self.__size += 1
        if self.len() == 1:
            self.__add_before_node(self.tail, new_node)
            return
        current_node = self.head.next
        while not isinstance(current_node, DummyNode):
            if self.__ascending and self.compare(current_node.value, value) >= 0:
                self.__add_before_node(current_node, new_node)
                return
            if not self.__ascending and self.compare(current_node.value, value) <= 0:
                self.__add_before_node(current_node, new_node)
                return
            current_node = current_node.next
        self.__add_before_node(self.tail, new_node)

    def find(self, val):
        current_node = self.head.next
        while not isinstance(current_node, DummyNode):
            if self.__ascending and current_node.value > val:
                return None
            if not self.__ascending and current_node.value < val:
                return None
            if current_node.value == val:
                return current_node
            current_node = current_node.next

        return None

    def delete(self, val):
        current_node = self.head.next
        while not isinstance(current_node, DummyNode):
            if self.__ascending and current_node.value > val:
                return
            if not self.__ascending and current_node.value < val:
                return
            if current_node.value == val:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                self.__size -= 1
                return
            current_node = current_node.next

    def clean(self, asc):
        self.__init__(asc)

    def len(self):
        return self.__size

    def get_all(self):
        r = []
        current_node = self.head.next
        while not isinstance(current_node, DummyNode):
            r.append(current_node)
            current_node = current_node.next
        return r

    def __add_after_node(self, after_node: Node, new_node: Node):
        if after_node is None:
            after_node = self.head
        new_node.prev = after_node
        new_node.next = after_node.next
        after_node.next.prev = new_node
        after_node.next = new_node

    def __add_before_node(self, before_node: Node, new_node: Node):
        if before_node is None:
            before_node = self.tail
        new_node.next = before_node
        new_node.prev = before_node.prev
        before_node.prev.next = new_node
        before_node.prev = new_node


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1: str, v2: str):
        v1 = v1.strip()
        v2 = v2.strip()
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0

        return 1
