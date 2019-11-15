#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    l = len(s)
    rows = int(math.floor(l**(0.5)))
    colums = int(math.ceil(l**(0.5)))
    output = ''

    for i in range(colums):
        k = i
        for j in range(k, l,colums):
            output += s[j]
        output += ' '
    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
