#!/bin/python3

import os
import sys
from itertools import product

def getMoneySpent(keyboards, drives, b):
    prices_ = [keyboards, drives]
    prices = list(product(*prices_))
    
    sum_prices = list(sum(x) for x in prices if sum(x) <= b)
    
    if not sum_prices:
        return -1
    
    return max(sum_prices)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent))
    fptr.close()
