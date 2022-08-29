class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
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
            self.head = new_node
            self.tail = new_node
            return
        current_node = self.head
        while current_node is not None:
            if self.__ascending and self.compare(current_node.value, value) >= 0:
                self.__add_before_node(current_node, new_node)
                return
            if not self.__ascending and self.compare(current_node.value, value) <= 0:
                self.__add_before_node(current_node, new_node)
                return
            current_node = current_node.next
        self.__add_before_node(None, new_node)

    def find(self, val):
        current_node = self.head
        while current_node is not None:
            if self.__ascending and current_node.value > val:
                return None
            if not self.__ascending and current_node.value < val:
                return None
            if current_node.value == val:
                return current_node
            current_node = current_node.next

        return None

    def delete(self, val):
        current_node = self.head
        while current_node is not None:
            if self.__ascending and self.compare(current_node.value, val) > 0:
                return
            if not self.__ascending and self.compare(current_node.value, val) < 0:
                return
            if self.compare(current_node.value, val) == 0:
                self.__delete_node(current_node)
                return
            current_node = current_node.next

    def clean(self, asc):
        self.__init__(asc)

    def len(self):
        return self.__size

    def get_all(self):
        r = []
        current_node = self.head
        while current_node is not None:
            r.append(current_node)
            current_node = current_node.next
        return r

    def __add_before_node(self, before_node: Node, new_node: Node):
        if before_node is None:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            return
        if self.head == before_node:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        new_node.next = before_node
        new_node.prev = before_node.prev
        before_node.prev.next = new_node
        before_node.prev = new_node

    def __delete_node(self, node: Node):
        if self.len() == 1:
            self.clean(self.__ascending)
            return
        self.__size -= 1
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


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1: str, v2: str) -> int:
        v1 = v1.strip()
        v2 = v2.strip()
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0

        return 1
