class Deque:
    def __init__(self):
        self.deque = []
        self.length = 0

    def addFront(self, item):
        self.deque.insert(0, item)

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.size() == 0:
            return None
        return self.deque.pop(0)

    def removeTail(self):
        if self.size() == 0:
            return None
        return self.deque.pop()

    def size(self):
        return self.deque.__len__()

    @staticmethod
    def is_palindrome(s: str):
        if s.__len__() == 0 or s.__len__() == 1:
            return True
        deq = Deque()
        for i in s:
            deq.addTail(i)
        while deq.size() > 0:
            if deq.size() == 1:
                break
            a = deq.removeFront()
            b = deq.removeTail()
            if a != b:
                return False
        return True
