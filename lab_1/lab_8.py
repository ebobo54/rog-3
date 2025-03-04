class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count=0
    
    def get(self):
        if self.head is None:
            print("error")
        else:
            print(self.head.value)
            self.head = self.head.next
            self.count -= 1
            if self.head is None:
                self.tail = None
    def put(self, x):
        new_node = Node(x)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
    def size(self):
        print(self.count)
if __name__ == "__main__":
    n = int(input())
    queue = Queue()
    for _ in range(n):
        command = input().split()
        if command[0] == "get":
            queue.get()
        elif command[0] =="put":
            queue.put(int(command[1]))
        elif command[0] == "size":
            queue.size()