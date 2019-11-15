#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    L =  len(s)
    row = math.floor(L**(1/2))
    col = math.ceil(L**(1/2))
    
    if row * col < L :
        row = col

    result = ""
    for i in range(col):
        result_= ""
        for j in range(row):
            if i+col*j < L:
                result_ += s[i+col*j]
        result += result_+" "

    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
