import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        if self.count == i:
            self.append(itm)
            return
        a = self.array[i]
        for index in range(i + 1, self.count):
            b = self.array[index]
            self.array[index] = a
            a = b
        self.array[self.count] = a
        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        self.array[i] = None
        for index in range(i + 1, self.count):
            self.array[index - 1] = self.array[index]
        self.count -= 1
        if self.count < self.capacity * 0.5 and self.capacity != 16:
            newSize = self.capacity * 10 // 15
            if newSize < 16:
                newSize = 16
            self.resize(newSize)

    def print(self):
        for i in range(self.count):
            print(self.array[i])
