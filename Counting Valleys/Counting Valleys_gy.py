#!/bin/python3

import math
import os
import random
import re
import sys


def countingValleys(n, s):
    valley = 0
    count = 0

    for i in range(n):
        if s[i] == 'U':
            count += 1
            
        if s[i] == 'D':
            count -= 1
            
        if count == -1 : #해저에 있을때 
        # 0에서 -1로 : D (valley) // -2에서 -1로 : U (X))        
            if s[i] == 'D': #valley인 경우
                valley += 1
                
    return valley



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
