class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.array = 0

    def hash1(self, str1):
        h = 0
        for c in str1:
            h *= 17
            code = ord(c)
            h += code

        return h % self.filter_len

    def hash2(self, str1):
        h = 0
        for c in str1:
            h *= 223
            code = ord(c)
            h += code

        return h % self.filter_len

    def add(self, str1):
        self.array |= self.hash1(str1)
        self.array |= self.hash2(str1)

    def is_value(self, str1):
        if self.array & self.hash1(str1) != self.hash1(str1):
            return False
        if self.array & self.hash2(str1) != self.hash2(str1):
            return False

        return True
