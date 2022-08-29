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

    def find(self, val) -> Node | None:
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val) -> []:
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next

        return result

    def delete(self, val, all=False) -> None:
        current_node = self.head
        while current_node is not None:
            if current_node.value == val:
                self.__delete_node(current_node)
                if not all:
                    return
            current_node = current_node.next

    def __delete_node(self, node: Node) -> None:
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

    def insert(self, after_node: Node, new_node: Node) -> None:
        if new_node is None or not isinstance(new_node, Node):
            return
        if after_node is None or after_node == self.tail:
            self.add_in_tail(new_node)
            return
        new_node.next = after_node.next
        new_node.prev = after_node
        new_node.next.prev = new_node
        after_node.next = new_node
        self.size += 1

    def add_in_head(self, new_node: Node) -> None:
        self.size += 1
        if self.tail is None:
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
