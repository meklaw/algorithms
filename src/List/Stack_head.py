class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class Stack:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def size(self):
        return self.length

    def pop(self):
        if self.size() == 0:
            return None
        result = self.head.value
        if self.size() == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        self.length -= 1
        return result

    def push(self, value):
        newNode = Node(value)
        self.length += 1
        if self.tail is None:
            self.tail = newNode
        else:
            newNode.next = self.head
        self.head = newNode

    def peek(self):
        if self.size() == 0:
            return None
        return self.head.value

    @staticmethod
    def check_parenthesis(string):
        if string is None:
            return None
        stack = Stack()
        for i in string:
            if i == '(':
                stack.push(i)
            elif i == ')':
                if stack.pop() != '(':
                    return False
        if stack.size() == 0:
            return True
        return False

    @staticmethod
    def postfix_calc(first_stack):
        if first_stack is None or not isinstance(first_stack, Stack):
            return None
        second_stack = Stack()
        while first_stack.size() != 0:
            i = first_stack.pop()
            if i.isdigit():
                second_stack.push(int(i))
            elif i == '=':
                return second_stack.pop()
            elif i == '+':
                second_stack.push(second_stack.pop() + second_stack.pop())
            elif i == '-':
                b = second_stack.pop()
                a = second_stack.pop()
                second_stack.push(a - b)
            elif i == '*':
                second_stack.push(second_stack.pop() * second_stack.pop())
            elif i == '/':
                b = second_stack.pop()
                a = second_stack.pop()
                second_stack.push(a / b)
        return second_stack.pop()