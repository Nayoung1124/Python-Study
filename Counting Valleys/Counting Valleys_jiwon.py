#!/bin/python3

import os
import sys

def countingValleys(n, s):
    count = 0
    high = 0
    for x in s:
        if x == 'U':
            high += 1
        elif x == 'D':
            high -= 1
        
        # 'U'로 끝나야 계곡
        if (high == 0) and x == 'U':
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
