import math
import os
import random
import re
import sys
from collections import defaultdict

def pickingNumbers(a):
    d=defaultdict(int)
    b=0
    for i in a:
        d[i]+=1
        b=max(b, d[i]+d[i+1], d[i]+d[i-1])
    return b
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
