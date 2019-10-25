class SimpleTextEditor():
    def __init__(self):
        self.backup = list() 
        self.current = ''

    def save(self):
        self.backup.append(self.current)

    def Append(self, W):
        self.save()
        self.current += W

    def Delete(self, k):
        self.save()
        self.current = self.current[:-k]

    def Print(self, k):
        print(self.current[k-1])
    
    def Undo(self):
        self.current = self.backup.pop()


if __name__=='__main__':
    Q = int(input().strip())
    
    TE = SimpleTextEditor()
    
    for i in range(Q):
        t = input().strip().split()
        if t[0] == '1':
            TE.Append(t[1])
        elif t[0] == '2':
            TE.Delete(int(t[1]))
        elif t[0] == '3':
            TE.Print(int(t[1]))
        else:
            TE.Undo()
        
