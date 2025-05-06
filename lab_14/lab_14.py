class HashTable:
    def __init__(self, size=100003):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return "None"

    def delete(self, key):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx].pop(i)
                return v
        return "None"


def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    table = HashTable()
    
    for line in data[1:]:
        parts = line.strip().split()
        if not parts:
            continue

        command = parts[0].lower()
        if command == 'put':
            key = int(parts[1])
            value = int(parts[2])
            table.put(key, value)
        elif command == 'get':
            key = int(parts[1])
            print(table.get(key))
        elif command == 'delete':
            key = int(parts[1])
            print(table.delete(key))


if __name__ == '__main__':
    main()
