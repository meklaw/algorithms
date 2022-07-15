from src.Stack.Stack_head import Stack


class Queue:
    def __init__(self):
        self.input = Stack()
        self.output = Stack()
        self.length = 0

    def enqueue(self, item):
        if self.output.size() != 0:
            self.to_input()
        self.input.push(item)
        self.length += 1

    def dequeue(self):
        if self.size() == 0:
            return None
        if self.input.size() != 0:
            self.to_output()
        self.length -= 1
        return self.output.pop()

    def size(self):
        return self.length

    def rotate(self, count):
        if self.size() == 0 or self.size() == 1 or count == 0:
            return
        for i in range(count % self.size()):
            self.enqueue(self.dequeue())

    def to_input(self):
        while self.output.size() > 0:
            self.input.push(self.output.pop())

    def to_output(self):
        while self.input.size() > 0:
            self.output.push(self.input.pop())
