#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#

def equalStacks(h1, h2, h3):
    s_h1 = sum(h1)
    s_h2 = sum(h2)
    s_h3 = sum(h3)
    while 1:
        s_m = min(s_h1, s_h2, s_h3) #세개의 stacks중 최소값

        while s_h1 > s_m:#최솟값보다 크다면 반복
            s_h1 -= h1.pop(0)
        while s_h2 > s_m:
            s_h2 -= h2.pop(0)
        while s_h3 > s_m:
            s_h3 -= h3.pop(0)

        if s_h1 == s_h2 == s_h3: #pop함수를 사용했을때 세개가 같다면 s_h1을 반환
            return s_h1
        else : 
            pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
