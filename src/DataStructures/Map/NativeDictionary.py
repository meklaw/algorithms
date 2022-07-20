class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        h = 0
        m = 1
        for c in key:
            x = ord(c)
            h = (h + m * x) % self.size
            m = (m * 91) % self.size

        return h

    def seek_slot(self, value):
        h = self.hash_fun(value)
        step = 3
        if self.size % step == 0:
            step += 1
        c = 0
        while self.slots[h] is not None:
            h = (h + step) % self.size
            c += 1
            if c > self.size:
                return None

        return h

    def is_key(self, key):
        for i in self.slots:
            if i == key:
                return True

        return False

    def put(self, key, value):
        if self.is_key(key):
            h = self.__get_id(key)
            self.values[h] = value
            return None

        h = self.seek_slot(key)
        if h is None:
            return None
        self.slots[h] = key
        self.values[h] = value

    def get(self, key):
        if not self.is_key(key):
            return None

        h = self.__get_id(key)
        return self.values[h]

    def __get_id(self, key):
        h = self.hash_fun(key)
        if self.slots[h] == key:
            return h

        step = 3
        if self.size % step == 0:
            step += 1
        c = 0
        while self.slots[h] != key:
            h = (h + step) % self.size
            c += 1
            if c > self.size:
                return None
        return h
