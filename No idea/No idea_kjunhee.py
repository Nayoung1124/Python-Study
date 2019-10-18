n, m = input().split()
whole = list(map(int ,input().strip().split(' ')))

A = set(map(int , input().split()))
B = set(map(int, input().split()))

score = 0

for i in whole:
    
    if i in A:
        score += 1
        
    if i in B:
        score -= 1 
        
    else :
        pass 
        

print(score)
