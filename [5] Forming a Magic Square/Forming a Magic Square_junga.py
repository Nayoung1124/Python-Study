#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    c = 0
    x = [1,2,3,4,5,6,7,8,9] #마방진에 1~9까지 다 있어함
    r = []
    for i in range(3):#가로
        for j in range(3):#세로
            if s[i][j] in x: 
                index_= x.index(s[i][j])
                x.pop(index_)   #추가되야할 
            else:
                r.append(s[i][j])   #원래의 s
    r.sort()
    for i in range(len(r)):
        c += abs(r[i] - x[i])
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
