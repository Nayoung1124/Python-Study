#!/bin/python3

import os
import sys
def mk_sum_list(lis):
    result = [0]
    for i in lis[::-1]:
        result.append(result[-1]+i)
    return set(result)

def equalStacks(h1, h2, h3):
    sum1 = mk_sum_list(h1)
    sum2 = mk_sum_list(h2)
    sum3 = mk_sum_list(h3)
    result = sum1 & sum2 & sum3
    return max(result)

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
