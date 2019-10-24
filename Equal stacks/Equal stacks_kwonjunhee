#!/bin/python3

import os
import sys

def equalStacks(h1, h2, h3):
    # h1,h2,h3의 합이 모두 같아야함
    h1_s=sum(h1)
    h2_s=sum(h2)
    h3_s=sum(h3)
    #a=(h1_s,h2_s,h3_s)
    while (h1_s!=h2_s) or(h2_s!=h3_s) or(h3_s!=h1_s):
    #not (h1_s==h2_s==h3_s)
        max_hi=max(h1_s, h2_s, h3_s)
        if h1_s==max_hi:
            h1_s-=h1.pop(0)
        if h2_s==max_hi:
            h2_s-=h2.pop(0)
        if h3_s==max_hi:
            h3_s-=h3.pop(0)
    return h1_s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0]) #5

    n2 = int(n1N2N3[1]) #3

    n3 = int(n1N2N3[2]) #4
    

    h1 = list(map(int, input().rstrip().split())) #3 2 111

    h2 = list(map(int, input().rstrip().split())) #4 3 2

    h3 = list(map(int, input().rstrip().split())) #1 1 4 1

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
