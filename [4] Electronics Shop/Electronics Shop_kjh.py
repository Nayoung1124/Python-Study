import os
import sys

def getMoneySpent(keyboards, drives, b):
    sum_kd=[]
    for i in range(n):
        for j in range(m):
            if keyboards[i]+drives[j]<=b:
                sum_kd.append(keyboards[i]+drives[j])
    
    if len(sum_kd)==0:
        return -1
    else :
        return max(sum_kd)
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    bnm = input().split()

    b = int(bnm[0]) #돈  
    n = int(bnm[1]) #키보드
    m = int(bnm[2]) #usb

    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')
    fptr.close()
