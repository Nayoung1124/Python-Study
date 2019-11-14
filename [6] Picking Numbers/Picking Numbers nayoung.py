#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict



def pickingNumbers(a):
    # Write your code here
    dic = defaultdict(int)
    b = 0
    for i in a:
        dic[i] += 1
        b = max(b,dic[i]+dic[i-1], dic[i]+dic[i+1])
    return b
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
