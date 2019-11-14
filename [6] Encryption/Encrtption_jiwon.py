#!/bin/python3

import os
import math

def encryption(input_s):
    L = len(input_s)
    root_L = math.sqrt(L)

    col = math.ceil(root_L)
    # row = math.floor(root_L) if math.floor(root_L) * col >= L else math.ceil(root_L)

    output_s = ''
    for i in range(col):
        output_s += ' ' + input_s[i:L:col]
    
    return output_s.strip()



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = encryption(s)
    fptr.write(result )
    fptr.close()
