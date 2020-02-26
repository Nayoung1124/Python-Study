#!/bin/python3

import os
import sys
from itertools import product as pd
#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    if min(keyboards) + min(drives) > b: return -1
    arr = list(pd(keyboards, drives))
    price = set()
    for i in arr:
        if sum(i) <= b:
            price.add(sum(i))
    return max(price)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
