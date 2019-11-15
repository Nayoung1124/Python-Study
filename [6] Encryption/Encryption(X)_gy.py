#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    P = ''
    L = math.sqrt(len(s))
    print(L)
    print(s)
    up = math.ceil(L)
    down = math.floor(L)
    print(up, down)
    
    for i in range(down):
        for j in range(up):
            P += s[i + up*j]
    
    
        print(P)

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
