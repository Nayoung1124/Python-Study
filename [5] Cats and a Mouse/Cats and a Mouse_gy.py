#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(cat_1, cat_2, mouse):
    D1 = mouse - cat_1
    D2 = mouse - cat_2
    D1 = abs(D1)
    D2 = abs(D2)
    
    if D1 == D2:
        return 'Mouse C'
    
    else:
        ans = max(D1, D2)
        
        if ans == D1:
            return 'Cat B'
        
        else:
            return 'Cat A'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
