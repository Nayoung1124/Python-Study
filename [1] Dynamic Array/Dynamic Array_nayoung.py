#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    last_answer=0
    for_output=[]
    seq_list =[[] for i in range(n)]
    for j in queries:
        if j[0] == 1:
            k = (j[1]^last_answer)%n
            seq_list[k].append(j[2])
        if j[0] == 2:
            k = (j[1]^last_answer)%n
            last_answer = seq_list[k][j[2]%len(seq_list[k])]
            for_output.append(last_answer)
    return for_output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))


    fptr.close()
