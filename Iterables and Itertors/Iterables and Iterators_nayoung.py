# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
def calculate(n, q, k):
    score = 0
    num = 0
    a = list(combinations(q,k))
    total = len(a)
    for i in a:
        if 'a' in i:
            num +=1
    score = num/total    
    print(round(score, 3))





if __name__ == '__main__':
    n = int(input())
    q = input().split()
    k = a = int(input())
    calculate(n, q, k)
