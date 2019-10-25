class STE:
    def __init__(self):
        self.do = []
        self.S = ''

    def add(self, data):
        self.S += data
        self.do.append(len(data))

    def delt(self, data):
        data = int(data)
        self.S = self.S[:-data]
        self.do.append(self.S[-data:])

    def view(self, data):
        print(self.S[int(data)-1])

    def undo(self):
        last = self.do.pop()
        if type(last) == int:
            self.S = self.S[:-last]
        
        else:
            self.S += last


n = int(input())
S = STE()

for i in range(n):
    temp = input().split()

    if temp[0] == '1':
        S.add(temp[1])

    elif temp[0] == '2':
        S.delt(temp[1])

    elif temp[0] == '3':
        S.view(temp[1])

    else:
        S.undo()
