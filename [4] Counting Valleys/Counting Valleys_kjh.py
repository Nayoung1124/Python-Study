
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s): # 8, UDDDUDUU
    valley=0
    sealevel=0
    for i in range(n):
        if (s[i]=='U'):
            sealevel+=1
            if (sealevel==0):
                valley+=1
        elif (s[i]=='D'):
            sealevel-=1
            
    
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
