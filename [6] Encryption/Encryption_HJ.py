#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    L = len(s)
    col = math.ceil(math.sqrt(L))
    
    result = ''
    for i in range(col):
        result += s[i:L:col] + ' '

    return result.strip()



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
