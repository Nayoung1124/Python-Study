class node:
    def __init__(self, data, next_node=None, key=False):
        self.data = data
        self.next_node = next_node
        self.key = key


class c_queue:
    def __init__(self, data=None, key=False):
        self.head = node(data, key=key)
        self.head.next_node = self.head
        self.tail = self.head
        self.priority = [data]
        if data == None:
            self.len = 0
        else:
            self.len = 1

    def sort(self):
        self.priority.sort()

    def enqueue(self, data, key=False):
        if self.len == 0:
            self.__init__(data, key)
            return
        self.tail.next_node = node(data, self.head, key)
        self.tail = self.tail.next_node
        self.len += 1
        self.priority.append(data)

    def dequeue(self):
        if self.len == 1:
            data = self.head.data
            key = self.head.key
            self.__init__()
            return data, key
        data = self.head.data
        key = self.head.key
        self.head = self.head.next_node
        self.tail.next_node = self.head
        self.len -= 1
        self.priority.pop()
        return data, key

    def __len__(self):
        return self.len

    def next(self, n=1):
        for i in range(n):
            self.tail = self.head
            self.head = self.head.next_node
        return self

    def isempty(self):
        if self.len == 0:
            return True
        else:
            return False


Q = int(input())
for _ in range(Q):
    N, M = [int(i) for i in input().split()]
    circle_queue = c_queue()
    for i, x in enumerate(input().split()):
        if i == M:
            circle_queue.enqueue(int(x), True)
        else: circle_queue.enqueue(int(x))
    circle_queue.sort()
    key = False
    return_value = 0
    while not key:
        if circle_queue.head.data == circle_queue.priority[-1]:
            return_value += 1
            data, key = circle_queue.dequeue()
        else: circle_queue.next()
    print(return_value)