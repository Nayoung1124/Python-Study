#!/bin/python3

import math
import os
import random
import re
import sys
import itertools


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    s = list(itertools.chain(*s))
    ANS = []
    ANS2 = []

    ans1 = [8, 1, 6, 3, 5, 7, 4, 9, 2]
    ans2 = [4, 3, 8, 9, 5, 1, 2, 7, 6]
    ans3 = [2, 9, 4, 7, 5, 3, 6, 1, 8]
    ans4 = [6, 7, 2, 1, 5, 9, 8, 3, 4]
    ans5 = [6, 1, 8, 7, 5, 3, 2, 9, 4]
    ans6 = [8, 3, 4, 1, 5, 9, 6, 7, 2]
    ans7 = [2, 7, 6, 9, 5, 1, 4, 3, 8]
    ans8 = [4, 9, 2, 3, 5, 7, 8, 1, 6]

    for i, j in zip(s, ans1):
        ANS.append(abs(i - j))
    ANS2.append(sum(ANS))
    ANS = []
    for i, j in zip(s, ans2):
        ANS.append(abs(i - j))
    ANS2.append(sum(ANS))
    ANS = []

    for i, j in zip(s, ans3):
        ANS.append(abs(i - j))
    ANS2.append(sum(ANS))
    ANS = []

    for i, j in zip(s, ans4):
        ANS.append(abs(i - j))
    ANS2.append(sum(ANS))
    ANS = []

    for i, j in zip(s, ans5):
        ANS.append(abs(i - j))
    ANS2.append(sum(ANS))
    ANS = []

    for i, j in zip(s, ans6):
        ANS.append(abs(i - j))
    ANS2.append(sum(ANS))
    ANS = []

    for i, j in zip(s, ans7):
        ANS.append(abs(i - j))
    ANS2.append(sum(ANS))
    ANS = []

    for i, j in zip(s, ans8):
        ANS.append(abs(i - j))
    ANS2.append(sum(ANS))
    ANS = []

    return min(ANS2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
