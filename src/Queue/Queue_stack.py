from src.Stack.Stack_head import Stack


class Queue:
    def __init__(self):
        self.input = Stack()
        self.output = Stack()
        self.length = 0

    def enqueue(self, item):
        self.input.push(item)
        self.length += 1

    def dequeue(self):
        if self.size() == 0:
            return None
        if self.output.size() == 0:
            self.to_output()
        self.length -= 1
        return self.output.pop()

    def size(self):
        return self.length

    def rotate(self, count):
        for i in range(count % self.size()):
            self.enqueue(self.dequeue())

    def to_output(self):
        while self.input.size() > 0:
            self.output.push(self.input.pop())
