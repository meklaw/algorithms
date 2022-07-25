class PowerSet:

    def __init__(self):
        self.slots = []

    def size(self):
        return len(self.slots)

    def put(self, value):
        if self.size() == 0:
            self.slots.append(value)
            return
        if self.get(value):
            return
        if value < self.slots[0]:
            self.slots.insert(0, value)
            return
        if self.slots[self.size() - 1] < value:
            self.slots.append(value)
            return
        a = 0
        b = self.size() - 1
        medium = self.size() // 2
        while True:
            if value < self.slots[medium]:
                b = medium
            if self.slots[medium] < value:
                a = medium
            if (b - a) == 1:
                self.slots.insert(b, value)
                return
            medium = (a + b) // 2

    def get(self, value):
        if self.size() == 0:
            return False
        if value == self.slots[0]:
            return True
        if self.slots[self.size() - 1] == value:
            return True
        if value < self.slots[0]:
            return False
        if self.slots[self.size() - 1] < value:
            return False
        a = 0
        b = self.size() - 1
        medium = self.size() // 2
        while True:
            if value < self.slots[medium]:
                b = medium
            if self.slots[medium] < value:
                a = medium
            if self.slots[medium] == value:
                return True
            if (b - a) == 1:
                if self.slots[a] == value:
                    return True
                if self.slots[b] == value:
                    return True
                if self.slots[medium] == value:
                    return True
                return False
            medium = (a + b) // 2

    def remove(self, value):
        if self.size() == 0:
            return False
        if value == self.slots[0]:
            self.slots.pop(0)
            return True
        if self.slots[self.size() - 1] == value:
            self.slots.pop(self.size() - 1)
            return True
        if value < self.slots[0]:
            return False
        if self.slots[self.size() - 1] < value:
            return False
        a = 0
        b = self.size() - 1
        medium = self.size() // 2
        while True:
            if value < self.slots[medium]:
                b = medium
            if self.slots[medium] < value:
                a = medium
            if self.slots[medium] == value:
                self.slots.pop(medium)
                return True
            if (b - a) == 1:
                if self.slots[a] == value:
                    self.slots.pop(a)
                    return True
                if self.slots[b] == value:
                    self.slots.pop(b)
                    return True
                if self.slots[medium] == value:
                    self.slots.pop(medium)
                    return True
                return False
            medium = (a + b) // 2

    def intersection(self, set2):
        result = PowerSet()
        for i in self.slots:
            if set2.get(i):
                result.put(i)
        return result

    def union(self, set2):
        result = PowerSet()
        for i in self.slots:
            result.put(i)
        for i in set2.slots:
            result.put(i)
        return result

    def difference(self, set2):
        result = PowerSet()
        for i in self.slots:
            if not set2.get(i):
                result.put(i)
        for i in set2.slots:
            if not self.get(i):
                result.put(i)
        return result

    def issubset(self, set2):
        for i in set2.slots:
            if not self.get(i):
                return False
        return True
