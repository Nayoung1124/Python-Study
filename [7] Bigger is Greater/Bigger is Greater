#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations
import itertools

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    z = []
    w = list(w)
    for i in w:
        z.append(ord(i))  # z는 input 아스키코드 리스트
    y = list(permutations(z, len(w)))
    x = [list(i) for i in y]  # 아스키 코드로 바꾸고, 나올수 있는 조합들을 담은 이중 리스트
    # print(x)
    temp = []
    sub = []
    w_sub = []
    for k in range(len(x)):
        count = 4
        for i, j in zip(z, x[k]):
            temp.append(int(i - j) * (10 ** count))
            count -= 1
        sub.append(temp)

        temp = []

    o=[]
    for i in sub:
        o.append(sum(i))
    ans = o.index(min(o))

    if sub.count([0]*len(sub[ans]))>1:
        return('no answer')
        pass

    else:
        ans = sub.index(min(sub))
        ans_1 = x[ans]
        # print(ans_1)
        a = ''
        for _ in ans_1:
            a += chr(_)
        return (a)
            





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
