#!/bin/python3

import os

def hurdleRace(k, height):
    max_h = max(height)
    if max_h > k:
        return max_h - k
    return 0
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    height = list(map(int, input().rstrip().split()))
    result = hurdleRace(k, height)
    fptr.write(str(result))
    fptr.close()
