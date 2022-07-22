class PowerSet:

    def __init__(self):
        self.__len = 0
        self.__capacity = 20_000
        self.slots = [None] * self.__capacity

    def hash_fun(self, value: str):
        h = 0
        m = 1
        for c in value:
            x = ord(c)
            h = (h + m * x) % self.__capacity
            m = (m * 91) % self.__capacity
        return h

    def seek_slot(self, value):
        h = self.hash_fun(value)
        if self.slots[h] == value:
            return None
        step = 3
        if self.__capacity % step == 0:
            step += 1
        c = 0
        while self.slots[h] is not None:
            h = (h + step) % self.__capacity
            c += 1
            if c > self.__capacity:
                return None
        return h

    def size(self):
        return self.__len

    def put(self, key):
        h = self.seek_slot(key)
        if h is None:
            return None
        self.slots[h] = key
        self.__len += 1

    def get(self, value):
        if self.__get_id(value) >= 0:
            return True
        return False

    def __get_id(self, value):
        h = self.hash_fun(value)
        if self.slots[h] == value:
            return h

        step = 3
        if self.__capacity % step == 0:
            step += 1
        c = 0
        while self.slots[h] != value:
            h = (h + step) % self.__capacity
            c += 1
            if c > self.__capacity:
                return -1
        return h

    def remove(self, value):
        h = self.__get_id(value)
        if h >= 0:
            self.slots[h] = None
            self.__len -= 1
            return True
        return False

    def get_values(self):
        res = []
        if self.size() == 0:
            return res
        for i in self.slots:
            if i is not None:
                res.append(i)
        return res

    def intersection(self, set2):
        result = PowerSet()
        if self.size() == 0 and set2.size() == 0:
            return result
        a = self.get_values()
        b = set2.get_values()
        for i in a:
            for k in b:
                if i == k:
                    result.put(i)
                    break
        return result

    def union(self, set2):
        result = PowerSet()
        if self.size() == 0 and set2.size() == 0:
            return result
        a = self.get_values()
        b = set2.get_values()
        for i in a:
            result.put(i)
        for i in b:
            result.put(i)
        return result

    def difference(self, set2):
        result = PowerSet()
        if self.size() == 0 and set2.size() == 0:
            return result
        a = self.get_values()
        b = set2.get_values()
        for i in a:
            if set2.__get_id(i) == -1:
                result.put(i)
        for i in b:
            if self.__get_id(i) == -1:
                result.put(i)
        return result

    def issubset(self, set2):
        b = set2.get_values()
        for i in b:
            if self.__get_id(i) == -1:
                return False
        return True
