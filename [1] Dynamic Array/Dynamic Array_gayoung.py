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
    s = [0] * 2
    s_0 = []
    s_1 = []

    array = []
    lastAnswer = 0
    for i in range(len(queries)):
        # print(queries[i],"요거하는중")
        # print(i,"번째 문제")
        if queries[i][0] == 1:
            # print("방법1")
            xor = queries[i][1]
            # print("xor값 [1]",xor)
            # print(lastAnswer,"비교")

            val = xor ^ lastAnswer
            element = val % 2
            # print(queries[i][2])
            # print(element,"리스트선택 0 or 1")
            # print(queries[i][2],"이값이 들어가야 함")
            if element == 0:
                s_0.append(queries[i][2])
            else:
                s_1.append(queries[i][2])
            # s[element] = queries[i][2]
            # print(s_0)
            # print(s_1)

        else:
            # querie2
            # print("방법2")

            xor = queries[i][1]
            val = xor ^ lastAnswer
            element = val % 2
            # print(element,"리스트선택 0 or 1")
            # print(queries[i][2],"이값이 들어가야 함")
            # print(s)
            if element == 0:
                lastAnswer = s_0[-1]
            else:
                lastAnswer = s_1[-1]
            array.append(lastAnswer)

    return array


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])  # N나눌수 %n

    q = int(first_multiple_input[1])  # 문제개수

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    # print(queries)
    result = dynamicArray(n, queries)
    # print(type(result))

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
