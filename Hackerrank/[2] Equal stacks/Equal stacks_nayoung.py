#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    a1, a2, a3 = 0, 0, 0
    b1, b2, b3 = [], [], []

    h1.reverse()
    h2.reverse()
    h3.reverse()

    for i in range(n1):
        a1+=h1[i]
        b1.append(a1)
    
    for j in range(n2):
        a2+=h2[j]
        b2.append(a2)

    for k in range(n3):
        a3+=h3[k]
        b3.append(a3)

    s1,s2,s3=set(b1),set(b2),set(b3)
    max_vlaue=max((s1&s2&s3),default=0)
    return max_vlaue




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
