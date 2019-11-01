#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count = 0
    level = 0

    for i in range(n):
        if(s[i]=='U'):
            level+=1
            if(level==0):
                count+=1
        else:
            level-=1

    return count


    # print(s_)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
