class node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class c_queue:
    def __init__(self, data=None):
        self.head = node(data)
        self.head.next_node = self.head
        self.tail = self.head
        if data == None:
            self.len = 0
        else:
            self.len = 1

    def enqueue(self, data):
        if self.len == 0:
            self.__init__(data)
            return
        self.tail.next_node = node(data, self.head)
        self.tail = self.tail.next_node
        self.len += 1

    def dequeue(self):
        if self.len == 1:
            data = self.head.data
            self.__init__(None)
            return data
        data = self.head.data
        self.head = self.head.next_node
        self.tail.next_node = self.head
        self.len -= 1
        return data

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


N, K = [int(i) for i in input().split()]
circle_queue = c_queue()
for i in range(1, N + 1):
    circle_queue.enqueue(str(i))

print('<', end='')
result = [circle_queue.next(K - 1).dequeue()]
while not circle_queue.isempty():
    result.append(circle_queue.next(K - 1).dequeue())
print(*result, end='', sep=', ')
print('>')