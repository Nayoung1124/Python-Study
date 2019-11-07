#!/bin/python3

import os
import sys

#3/16 failed

def getMoneySpent(K, D, b): #키보드, 드라이브, 예산

    can = [] #예산(b)보다 저렴한 두제품 가격의 합

    for i in range(n): #전체 경우의 수(키보드 + 드라이브)
        for j in range(m):

            element = K[i] + D[j]

            if element < b: #값이 예산보다 작으면
                can.append(element) #살수있어(can)list에 
            else: # 더 크면 x
                continue  

    if len(can) == 0: #살수있는 리스트에 아무것도 없으면
        ans = -1
        return ans # -1반환
        
    if len(can) >= 1: #리스트에 있으면
        ans = max(can) #가장 큰값
        return ans  #반환
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
