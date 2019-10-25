# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
p = []
history=[]
whole = []
for k in range(n):
    line = input().split()
    #print(line)
    f = int(line[0])
    #print(f)

    if f != 4:
        
        c = list(line[1])
        
        
        if f == 1:
            data = c
            #print(data,"지금 저장하는 data")
            history.append(f)
            p.extend(c)
            #print(p)
        if f == 2:
            history.append(f)
            dataaa = p.pop()
            #print(p)
        if f == 3:
            #print(p[-1])
            pass
            #print(p, "현재 p")
    whole.append(p)
    print(whole,"whole")
    

    if f == 4:
        whole.pop()
        print(whole)
        
    
 


            


