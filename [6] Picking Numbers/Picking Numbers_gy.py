#!/bin/python3

import math
import os
import random
import re
import sys



def pickingNumbers(a):
    a.sort()
    ans = []
    for i in range(len(a)-1):
        count = 0
        for j in range(i+1,len(a)):
            if a[j] - a[i] > 1: 
                break
            count+=1
            ans.append(count)
    return max(ans) + 1
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
