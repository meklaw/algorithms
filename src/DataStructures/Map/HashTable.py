class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value: str):
        h = 0
        m = 1
        for c in value:
            x = ord(c)
            h = (h + m * x) % self.size
            m = (m * 91) % self.size
        return h

    def seek_slot(self, value):
        h = self.hash_fun(value)
        step = self.step
        if self.size % step == 0:
            step += 1
        c = 0
        while self.slots[h] is not None:
            h = (h + step) % self.size
            c += 1
            if c > self.size:
                return None
        return h

    def put(self, value):
        h = self.seek_slot(value)
        if h is None:
            return None
        self.slots[h] = value
        return h

    def find(self, value):
        for i in range(self.size):
            if self.slots[i] == value:
                return i
        return None
