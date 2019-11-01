#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    current = 0
    n_vally = 0
    temp = False
    for i in s:
        if i is 'U': current += 1
        else : current -= 1
        if current > 0:
            temp = True
            continue
        if current is 0 and temp is False: n_vally += 1
        temp = False
    return n_vally


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
