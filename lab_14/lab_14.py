class HashMap:
    def __init__(self):
        self.size = 10**5
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        h = self._hash(key)
        for i, (k, v) in enumerate(self.table[h]):
            if k == key:
                self.table[h][i] = (key, value)
                return
        self.table[h].append((key, value))

    def get(self, key):
        h = self._hash(key)
        for k, v in self.table[h]:
            if k == key:
                return v
        return "None"

    def delete(self, key):
        h = self._hash(key)
        for i, (k, v) in enumerate(self.table[h]):
            if k == key:
                del self.table[h][i]
                return v
        return "None"

