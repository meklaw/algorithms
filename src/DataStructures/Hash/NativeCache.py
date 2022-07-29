class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, value: str):
        h = 0
        m = 1
        for c in value:
            x = ord(c)
            h = (h + m * x) % self.size
            m = (m * 91) % self.size
        return h

    def clear(self):
        index = -1
        minimum = self.hits[0]
        for i in range(self.size):
            if self.hits[i] < minimum:
                index = i
                minimum = self.hits[i]

        self.slots[index] = None
        self.values[index] = None
        self.hits[index] = 0
        return index

    def seek_slot(self, value):
        h = self.hash_fun(value)
        c = 0
        while self.slots[h] is not None:
            h = (h + 1) % self.size
            c += 1
            if c == self.size:
                h = self.clear()
                break
        return h

    def put(self, key, value):
        if self.is_key(key):
            h = self.get_id(key)
            self.values[h] = value
            return
        h = self.seek_slot(key)
        self.slots[h] = key
        self.values[h] = value
        self.hits[h] = 1

    def is_key(self, key):
        for i in self.slots:
            if i == key:
                return True

        return False

    def get(self, key):
        if not self.is_key(key):
            return None

        h = self.get_id(key)
        self.hits[h] += 1
        return self.values[h]

    def get_id(self, key):
        h = self.hash_fun(key)
        if self.slots[h] == key:
            return h

        c = 0
        while self.slots[h] != key:
            h = (h + 1) % self.size
            c += 1
            if c == self.size:
                return None
        return h
